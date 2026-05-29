"""
keymap_docgen.py

ZMK keymap (.keymap) の指定した 1 つ以上のレイヤーの全キー割り当てを以下 2 形式で出力する
ドキュメンテーション生成ツール：

  1. Excel ファイル (.xlsx)
       - 単一レイヤー指定時: "動作" シートと "経路" シートを生成（QWERTY 物理配列）
       - 複数レイヤー指定時: 各レイヤーごとに "<layer> 動作"/"<layer> 経路" シートを生成
  2. Markdown ファイル (.md)
       - 同じ内容を Markdown の表で出力（セル内改行に <br> を使用）
       - 複数レイヤー指定時は 1 ファイル内で「## 動作」セクションに全レイヤーを並べた後、
         「## 経路」セクションに全レイヤーを再度並べる構成

それぞれの表は、キーボード物理行ごとに以下の構造を持つ：
  - 左端 1 列: 「操作」 = 単発タップ / ダブルタップ / Shift+ / Ctrl+
  - 右側の列: その物理行のキーを QWERTY 順に並べたもの

mod-morph (LSHIFT/RSHIFT, LCTL/RCTL), tap-dance, layer-tap, momentary-layer
など標準的な ZMK behavior を解析し、再帰的に動作を解決する。

Usage:
    python keymap_docgen.py <keymap_file> <layer_name> [<layer_name> ...] [-o output.xlsx]

出力先：
    -o で指定した .xlsx と同じディレクトリ／同じベース名で .md も生成される
    （-o を省略するとレイヤー単独時は <layer>_keymap.xlsx、複数時は keymap.xlsx）

Examples:
    python tools/keymap_docgen.py config/keymap.keymap VIM_NORMAL_1 -o KEYMAP.xlsx
    python tools/keymap_docgen.py config/keymap.keymap VIM_NORMAL_1 VIM_NORMAL_2 VIM_VISUAL -o KEYMAP.xlsx
"""

import argparse
import re
import sys
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter


# ============================================================================
# Parsing
# ============================================================================

def strip_comments(text: str) -> str:
    text = re.sub(r'//[^\n]*', '', text)
    text = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)
    return text


def find_balanced_block(content: str, start_pos: int) -> tuple[int, int] | None:
    """Find the position of the matching close brace for an open brace at start_pos."""
    if start_pos >= len(content) or content[start_pos] != '{':
        return None
    depth = 1
    i = start_pos + 1
    while i < len(content):
        if content[i] == '{':
            depth += 1
        elif content[i] == '}':
            depth -= 1
            if depth == 0:
                return (start_pos + 1, i)
        i += 1
    return None


def extract_named_block(content: str, name: str) -> str | None:
    """Extract the content of a top-level named block like 'macros { ... }'."""
    # Find 'name {'
    for m in re.finditer(r'\b' + re.escape(name) + r'\s*\{', content):
        brace_pos = m.end() - 1
        range_ = find_balanced_block(content, brace_pos)
        if range_:
            return content[range_[0]:range_[1]]
    return None


def parse_definitions(block_content: str) -> dict:
    """
    Parse 'name: label { ... };' definitions inside a block.
    Returns dict: {name: body_string}
    """
    defs = {}
    i = 0
    while i < len(block_content):
        m = re.search(r'(\w+)\s*:\s*\w+\s*\{', block_content[i:])
        if not m:
            break
        name = m.group(1)
        brace_pos = i + m.end() - 1
        range_ = find_balanced_block(block_content, brace_pos)
        if not range_:
            break
        body = block_content[range_[0]:range_[1]]
        defs[name] = body
        i = range_[1] + 1
    return defs


def parse_bindings_list(body: str) -> list[str]:
    """Extract list of bindings from a 'bindings = <...>, <...>;' style body."""
    m = re.search(r'bindings\s*=\s*([^;]+);', body, re.DOTALL)
    if not m:
        return []
    text = m.group(1)
    return [s.strip() for s in re.findall(r'<([^>]+)>', text)]


def parse_compatible(body: str) -> str | None:
    m = re.search(r'compatible\s*=\s*"([^"]+)"', body)
    return m.group(1) if m else None


def parse_mods(body: str) -> str | None:
    m = re.search(r'mods\s*=\s*<\(?([^>)]+)\)?>', body)
    return m.group(1).strip() if m else None


def parse_macros(content: str) -> dict:
    block = extract_named_block(content, 'macros')
    if not block:
        return {}
    defs = parse_definitions(block)
    return {name: {'bindings': parse_bindings_list(body)} for name, body in defs.items()}


def parse_behaviors(content: str) -> dict:
    block = extract_named_block(content, 'behaviors')
    if not block:
        return {}
    defs = parse_definitions(block)
    out = {}
    for name, body in defs.items():
        out[name] = {
            'compatible': parse_compatible(body),
            'bindings': parse_bindings_list(body),
            'mods': parse_mods(body),
        }
    return out


def parse_layer(content: str, layer_name: str) -> str | None:
    """Extract the raw bindings text of a named layer."""
    keymap_block = extract_named_block(content, 'keymap')
    if not keymap_block:
        return None
    defs = {}
    # layers are 'NAME { ... }' (no label after colon)
    i = 0
    while i < len(keymap_block):
        m = re.search(r'(\w+)\s*\{', keymap_block[i:])
        if not m:
            break
        name = m.group(1)
        brace_pos = i + m.end() - 1
        range_ = find_balanced_block(keymap_block, brace_pos)
        if not range_:
            break
        body = keymap_block[range_[0]:range_[1]]
        if name == layer_name:
            m2 = re.search(r'bindings\s*=\s*<(.+?)>', body, re.DOTALL)
            if m2:
                return m2.group(1)
        i = range_[1] + 1
    return None


def split_layer_bindings(text: str) -> list[str]:
    """Split a layer bindings string into individual binding strings (each starts with '&')."""
    text = re.sub(r'\s+', ' ', text).strip()
    out = []
    i = 0
    n = len(text)
    while i < n:
        if text[i] == '&':
            j = i + 1
            while j < n and text[j] != '&':
                j += 1
            out.append(text[i:j].strip())
            i = j
        else:
            i += 1
    return out


# ============================================================================
# Keycode formatting
# ============================================================================

KEYCODE_LABELS = {
    'LEFT': '←', 'RIGHT': '→', 'UP_ARROW': '↑', 'DOWN': '↓',
    'HOME': 'HOME', 'END': 'END', 'ENTER': 'ENTER', 'DELETE': 'DELETE',
    'BACKSPACE': 'BACKSPACE', 'TAB': 'TAB', 'SPACE': 'SPACE', 'ESCAPE': 'ESC',
    'PAGE_UP': 'PAGE_UP', 'PAGE_DOWN': 'PAGE_DOWN',
    'LCTRL': 'Left Ctrl', 'RCTRL': 'Right Ctrl',
    'LSHIFT': 'Left Shift', 'RSHIFT': 'Right Shift',
    'LEFT_SHIFT': 'Left Shift', 'RIGHT_SHIFT': 'Right Shift',
    'LEFT_CONTROL': 'Left Ctrl', 'RIGHT_CONTROL': 'Right Ctrl',
    'LEFT_ALT': 'Left Alt', 'RIGHT_ALT': 'Right Alt',
    'LEFT_WIN': 'Left Win', 'RIGHT_WIN': 'Right Win',
    'GREATER_THAN': '>', 'LESS_THAN': '<',
}

MOD_PREFIX = {
    'LC': 'Ctrl', 'RC': 'Ctrl',
    'LS': 'Shift', 'RS': 'Shift',
    'LA': 'Alt', 'RA': 'Alt',
    'LG': 'Win', 'RG': 'Win',
}


def format_keycode(kc: str) -> str:
    kc = kc.strip()
    m = re.match(r'(LC|LS|LA|LG|RC|RS|RA|RG)\((.+)\)$', kc)
    if m:
        return f"{MOD_PREFIX[m.group(1)]}+{format_keycode(m.group(2))}"
    return KEYCODE_LABELS.get(kc, kc)


# ============================================================================
# Resolution: binding × operation -> (action_description, path)
# ============================================================================

OPS = ('単発タップ', 'ダブルタップ', 'Shift+', 'Ctrl+')


def resolve(binding: str, behaviors: dict, macros: dict, op: str, depth: int = 0) -> tuple[str, str]:
    """Resolve a binding string for the given operation."""
    if depth > 10:
        return ('再帰深度超過', binding)
    b = binding.strip()

    if b == '&none':
        return ('何もしない', '&none')

    if b == '&trans':
        return ('フォールスルー', '&trans')

    # &kp X
    m = re.match(r'&kp\s+(.+)$', b)
    if m:
        kc = m.group(1).strip()
        label = format_keycode(kc)
        if op == '単発タップ':
            return (f'{label} 入力', f'&kp {kc}')
        if op == 'ダブルタップ':
            return (f'{label} 入力 × 2', f'&kp {kc}（tap-dance 未定義、連打）')
        if op == 'Shift+':
            return (f'Shift + {label}（OS で合成）', f'&kp {kc}（物理 Shift は HID にそのまま伝わる）')
        if op == 'Ctrl+':
            return (f'Ctrl + {label}（OS で合成）', f'&kp {kc}（物理 Ctrl は HID にそのまま伝わる）')

    # &mt MOD KEY
    m = re.match(r'&mt\s+(\S+)\s+(.+)$', b)
    if m:
        mod, key = m.group(1).strip(), m.group(2).strip()
        if op == '単発タップ':
            return (f'{format_keycode(key)} 入力（タップ）', f'&mt {mod} {key}')
        if op == 'ダブルタップ':
            return (f'{format_keycode(key)} 入力 × 2', f'&mt {mod} {key}（連打）')
        if op == 'Shift+':
            return (f'Shift + {format_keycode(key)}（または {format_keycode(mod)} ホールドで修飾）', f'&mt {mod} {key}')
        if op == 'Ctrl+':
            return (f'Ctrl + {format_keycode(key)}', f'&mt {mod} {key}')

    # &lt LAYER KEY
    m = re.match(r'&lt\s+(\d+)\s+(.+)$', b)
    if m:
        layer, key = m.group(1), m.group(2).strip()
        if op == '単発タップ':
            return (f'{format_keycode(key)} 入力（タップ）', f'&lt {layer} {key}')
        if op == 'ダブルタップ':
            return (f'{format_keycode(key)} 入力 × 2', f'&lt {layer} {key}（連打）')
        if op == 'Shift+':
            return (f'Shift + {format_keycode(key)}（ホールドでレイヤー {layer}）', f'&lt {layer} {key}')
        if op == 'Ctrl+':
            return (f'Ctrl + {format_keycode(key)}（ホールドでレイヤー {layer}）', f'&lt {layer} {key}')

    # &mo X
    m = re.match(r'&mo\s+(\d+)$', b)
    if m:
        layer = m.group(1)
        msg = f'レイヤー {layer} を momentary（押下中のみ）有効化'
        return (msg, f'&mo {layer}')

    # &to X
    m = re.match(r'&to\s+(\d+)$', b)
    if m:
        layer = m.group(1)
        return (f'レイヤー {layer} に切替', f'&to {layer}')

    # Custom behavior / macro reference like &mm_vim_g, &td_vim_d, &macro_vim_dd
    if b.startswith('&'):
        name = b[1:].split()[0]
        if name in behaviors:
            return resolve_behavior(name, behaviors, macros, op, depth + 1)
        if name in macros:
            return resolve_macro(name, behaviors, macros, op, depth + 1)

    return (f'未対応: {b}', b)


def resolve_behavior(name: str, behaviors: dict, macros: dict, op: str, depth: int) -> tuple[str, str]:
    beh = behaviors[name]
    compat = beh['compatible']
    bindings = beh['bindings']
    mods = beh['mods'] or ''

    if compat == 'zmk,behavior-mod-morph':
        is_shift = 'LSFT' in mods or 'RSFT' in mods
        is_ctrl = 'LCTL' in mods or 'RCTL' in mods

        if op in ('単発タップ', 'ダブルタップ'):
            sub_a, sub_p = resolve(bindings[0], behaviors, macros, op, depth)
            return (sub_a, f'{name}[0] → {sub_p}')

        if op == 'Shift+':
            if is_shift:
                sub_a, sub_p = resolve(bindings[1], behaviors, macros, '単発タップ', depth)
                return (sub_a, f'{name}[1] (Shift 検知) → {sub_p}')
            else:
                sub_a, sub_p = resolve(bindings[0], behaviors, macros, 'Shift+', depth)
                return (sub_a, f'{name}[0] (Shift は本 mod-morph 検知外) → {sub_p}')

        if op == 'Ctrl+':
            if is_ctrl:
                sub_a, sub_p = resolve(bindings[1], behaviors, macros, '単発タップ', depth)
                return (sub_a, f'{name}[1] (Ctrl 検知) → {sub_p}')
            else:
                sub_a, sub_p = resolve(bindings[0], behaviors, macros, 'Ctrl+', depth)
                return (sub_a, f'{name}[0] (Ctrl は本 mod-morph 検知外) → {sub_p}')

    if compat == 'zmk,behavior-tap-dance':
        if op == '単発タップ':
            sub_a, sub_p = resolve(bindings[0], behaviors, macros, '単発タップ', depth)
            return (sub_a, f'{name}[0] → {sub_p}')
        if op == 'ダブルタップ':
            sub_a, sub_p = resolve(bindings[1], behaviors, macros, '単発タップ', depth)
            return (sub_a, f'{name}[1] → {sub_p}')
        if op == 'Shift+':
            sub_a, sub_p = resolve(bindings[0], behaviors, macros, 'Shift+', depth)
            return (sub_a, f'{name}[0] (tap-dance は mods 検知なし) → {sub_p}')
        if op == 'Ctrl+':
            sub_a, sub_p = resolve(bindings[0], behaviors, macros, 'Ctrl+', depth)
            return (sub_a, f'{name}[0] (tap-dance は mods 検知なし) → {sub_p}')

    return (f'未対応 behavior: {compat}', name)


def resolve_macro(name: str, behaviors: dict, macros: dict, op: str, depth: int) -> tuple[str, str]:
    summary = summarize_macro(macros[name]['bindings'])
    if op == '単発タップ':
        return (summary, name)
    if op == 'ダブルタップ':
        return (f'{summary}（2 回実行）', f'{name}（連打）')
    if op == 'Shift+':
        return (f'{summary}（Shift 物理保持で実行）', name)
    if op == 'Ctrl+':
        return (f'{summary}（Ctrl 物理保持で実行）', name)
    return (summary, name)


def summarize_macro(bindings: list[str]) -> str:
    parts = []
    for b in bindings:
        b = b.strip()
        if b.startswith('&macro_wait_time'):
            continue
        if b.startswith('&kp '):
            parts.append(format_keycode(b[4:].strip()))
        elif b.startswith('&macro_release'):
            inner = re.search(r'&kp\s+(\S+)', b)
            if inner:
                parts.append(f'{format_keycode(inner.group(1))} 解放')
        elif b.startswith('&macro_press'):
            inner = re.search(r'&kp\s+(\S+)', b)
            if inner:
                parts.append(f'{format_keycode(inner.group(1))} 押下')
        elif b.startswith('&macro_tap'):
            inner = re.search(r'&kp\s+(\S+)', b)
            if inner:
                parts.append(format_keycode(inner.group(1)))
        elif b.startswith('&to '):
            parts.append(f'レイヤー {b[4:].strip()} へ')
        else:
            parts.append(b)
    return ' → '.join(parts)


# ============================================================================
# Visual label (depends on layer dimensions in keymap)
# ============================================================================

ROW_LABELS = {
    # row index -> [labels per position]
    0: ['(outer)'] + ['top wing'] * 10 + ['(outer)'],
    1: ['(outer)', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '(outer)'],
    2: ['(outer)', 'A', 'S', 'D', 'F', 'G', '(center L)', '(center R)',
        'H', 'J', 'K', 'L', 'MINUS', '(outer)'],
    3: ['(outer)', 'Z', 'X', 'C', 'V', 'B', '(center L)', '(center R)',
        'N', 'M', 'COMMA', 'PERIOD', 'SLASH', '(outer)'],
    4: ['(outer)', 'mo6 (outer)', 'LEFT_WIN', 'LEFT_ALT',
        'lt2 SPACE', 'lt2 SPACE', '(mo1 center)', '(mo2 center)',
        'lt1 ENTER', '(none)', '(none)', 'mo6', 'mo6 (outer)', '(outer)'],
}

ROW_WIDTHS = {0: 12, 1: 12, 2: 14, 3: 14, 4: 14}


def get_visual_label(row: int, pos: int) -> str:
    labels = ROW_LABELS.get(row, [])
    if pos < len(labels):
        return labels[pos]
    return f'pos {pos}'


# ============================================================================
# Excel output
# ============================================================================

ROW_DESCRIPTIONS = {
    0: 'Row 0 (top wing)',
    1: 'Row 1 (QWERTY 上段)',
    2: 'Row 2 (home row)',
    3: 'Row 3 (Z row)',
    4: 'Row 4 (thumb)',
}


def get_row_layout(total: int) -> list[tuple[int, int]]:
    """Determine the physical row layout based on total binding count."""
    if total == 66:
        return [(0, 12), (1, 12), (2, 14), (3, 14), (4, 14)]
    if total == 44:
        return [(1, 10), (2, 10), (3, 12), (4, 12)]
    return [(0, total)]  # fallback: linear


def write_qwerty_sheet(ws, layer_name: str, bindings: list[str],
                       behaviors: dict, macros: dict, mode: str) -> None:
    """
    Write one sheet in QWERTY layout. mode: 'action' or 'path'.
    Each physical keyboard row gets its own block:
      - Header row: 操作 (label) + key columns (key label + binding)
      - 4 data rows (単発タップ / ダブルタップ / Shift+ / Ctrl+)
    """
    title_font = Font(bold=True, size=14, name='Yu Gothic UI')
    subtitle_font = Font(size=10, italic=True, name='Yu Gothic UI', color='666666')
    section_font = Font(bold=True, size=11, color='FFFFFF', name='Yu Gothic UI')
    section_fill = PatternFill('solid', start_color='4472C4', end_color='4472C4', fill_type='solid')
    header_font = Font(bold=True, size=10, name='Yu Gothic UI')
    header_fill = PatternFill('solid', start_color='D9E1F2', end_color='D9E1F2', fill_type='solid')
    op_font = Font(bold=True, size=10, name='Yu Gothic UI')
    op_fill = PatternFill('solid', start_color='F2F2F2', end_color='F2F2F2', fill_type='solid')
    body_font = Font(size=9, name='Yu Gothic UI')

    thin = Side(style='thin', color='808080')
    border = Border(left=thin, right=thin, top=thin, bottom=thin)

    mode_label = '動作' if mode == 'action' else '経路'

    # Title
    c = ws.cell(1, 1, f'{layer_name} レイヤー - {mode_label} (QWERTY 配列)')
    c.font = title_font
    c.alignment = Alignment(horizontal='left')

    c = ws.cell(2, 1, f'※ 物理キーボード行ごとに 4 操作 × N キーの表を縦に並べて出力。')
    c.font = subtitle_font

    layout = get_row_layout(len(bindings))
    max_cols = max(count for _, count in layout) + 1  # +1 for 操作 column

    # Column widths
    ws.column_dimensions['A'].width = 14
    col_width = 24 if mode == 'action' else 36
    for c_idx in range(2, max_cols + 1):
        ws.column_dimensions[get_column_letter(c_idx)].width = col_width

    current_row = 4
    binding_idx = 0
    for phys_row, count in layout:
        labels = ROW_LABELS.get(phys_row, [])
        desc = ROW_DESCRIPTIONS.get(phys_row, f'Row {phys_row}')

        # Section title bar (spans operation column + all key columns)
        c = ws.cell(current_row, 1, f'■ {desc}')
        c.font = section_font
        c.fill = section_fill
        c.alignment = Alignment(horizontal='left', vertical='center', indent=1)
        ws.merge_cells(start_row=current_row, start_column=1,
                       end_row=current_row, end_column=count + 1)
        ws.row_dimensions[current_row].height = 22
        current_row += 1

        # Header row: 操作 (col 1) + key label + binding (cols 2..)
        c = ws.cell(current_row, 1, '操作')
        c.font = header_font
        c.fill = header_fill
        c.alignment = Alignment(horizontal='center', vertical='center')
        c.border = border

        for p in range(count):
            label = labels[p] if p < len(labels) else f'pos {p}'
            binding = bindings[binding_idx + p]
            c = ws.cell(current_row, 2 + p, f'{label}\n{binding}')
            c.font = header_font
            c.fill = header_fill
            c.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
            c.border = border
        ws.row_dimensions[current_row].height = 42
        current_row += 1

        # 4 data rows (one per operation)
        for op_idx, op in enumerate(OPS):
            r = current_row + op_idx

            # Operation label (col 1)
            c = ws.cell(r, 1, op)
            c.font = op_font
            c.fill = op_fill
            c.alignment = Alignment(horizontal='center', vertical='center')
            c.border = border

            # Key cells
            for p in range(count):
                binding = bindings[binding_idx + p]
                action, path = resolve(binding, behaviors, macros, op)
                value = action if mode == 'action' else path
                c = ws.cell(r, 2 + p, value)
                c.font = body_font
                c.alignment = Alignment(wrap_text=True, vertical='center')
                c.border = border
            ws.row_dimensions[r].height = 38

        current_row += len(OPS) + 1  # 4 data rows + 1 blank
        binding_idx += count


def write_excel(layers_data: list[tuple[str, list[str]]],
                behaviors: dict, macros: dict, output_path: Path) -> None:
    """Generate one Excel file. Single layer => sheets '動作'/'経路'.
    Multiple layers => sheets '<layer> 動作'/'<layer> 経路' per layer."""
    wb = Workbook()
    is_single = len(layers_data) == 1
    first = True
    for layer_name, bindings in layers_data:
        for mode_label, mode in [('動作', 'action'), ('経路', 'path')]:
            sheet_name = mode_label if is_single else f'{layer_name} {mode_label}'
            sheet_name = sheet_name[:31]  # Excel sheet name limit
            if first:
                ws = wb.active
                ws.title = sheet_name
                first = False
            else:
                ws = wb.create_sheet(sheet_name)
            write_qwerty_sheet(ws, layer_name, bindings, behaviors, macros, mode)
    wb.save(output_path)


# ============================================================================
# Markdown output
# ============================================================================

def _escape_md_cell(s) -> str:
    """Escape a value so it can safely appear inside a Markdown table cell."""
    if s is None:
        return ''
    return str(s).replace('|', '\\|').replace('\n', '<br>')


def _markdown_layer_mode_rows(layer_name: str, bindings: list[str],
                              behaviors: dict, macros: dict,
                              mode: str) -> list[str]:
    """Return one consolidated table for a (layer, mode) pair.

    Format: a single table per layer/mode where each physical row appears
    as a section data row (`■ Row N` + key labels/bindings) followed by
    the four operation data rows (単発タップ / ダブルタップ / Shift+ / Ctrl+).
    """
    layout = get_row_layout(len(bindings))
    max_cols = max(count for _, count in layout) if layout else 0
    lines: list[str] = []

    header_cells = ['操作'] + [str(i + 1) for i in range(max_cols)]
    lines.append('| ' + ' | '.join(header_cells) + ' |')
    lines.append('|' + '|'.join(['---'] * (max_cols + 1)) + '|')

    binding_idx = 0
    for phys_row, count in layout:
        desc = ROW_DESCRIPTIONS.get(phys_row, f'Row {phys_row}')
        labels = ROW_LABELS.get(phys_row, [])

        section_cells = [f'■ {_escape_md_cell(desc)}']
        for p in range(count):
            label = labels[p] if p < len(labels) else f'pos {p}'
            binding = bindings[binding_idx + p]
            section_cells.append(
                f'{_escape_md_cell(label)}<br>`{_escape_md_cell(binding)}`'
            )
        section_cells.extend([''] * (max_cols - count))
        lines.append('| ' + ' | '.join(section_cells) + ' |')

        for op in OPS:
            row_cells = [_escape_md_cell(op)]
            for p in range(count):
                binding = bindings[binding_idx + p]
                action, path = resolve(binding, behaviors, macros, op)
                value = action if mode == 'action' else path
                if value == '何もしない':
                    row_cells.append('')
                elif value == 'フォールスルー':
                    row_cells.append('▽')
                else:
                    row_cells.append(_escape_md_cell(value))
            row_cells.extend([''] * (max_cols - count))
            lines.append('| ' + ' | '.join(row_cells) + ' |')

        binding_idx += count

    lines.append('')
    return lines


def write_markdown(layers_data: list[tuple[str, list[str]]],
                   behaviors: dict, macros: dict, output_path: Path) -> None:
    """Generate one Markdown file.
    Single layer  => H1 layer title, then H2 動作 / H2 経路.
    Multi layers  => H1 top title, H2 動作 (each layer at H3), then H2 経路 (each layer at H3)."""
    lines: list[str] = []

    if len(layers_data) == 1:
        layer_name, bindings = layers_data[0]
        lines.append(f'# {layer_name} レイヤー キー割り当て一覧')
        lines.append('')
        lines.append(
            f'※ {len(bindings)} 個のバインディング位置を 1 表に集約。'
            f'物理キーボード行ごとに「■ Row N」セクション行 + 4 操作行を縦に並べる（QWERTY 配列）。'
        )
        lines.append('')
        lines.append('- 各 row セクション行に「キーラベル」と「バインディング (`&...`)」の 2 段表示でキー位置を示す。')
        lines.append('- 各表の左端 1 列が「操作」（単発タップ / ダブルタップ / Shift+ / Ctrl+）または「■ Row N」見出し。')
        lines.append('')
        for mode_label, mode in [('動作', 'action'), ('経路', 'path')]:
            lines.append(f'## {mode_label}')
            lines.append('')
            lines.extend(_markdown_layer_mode_rows(layer_name, bindings,
                                                   behaviors, macros, mode))
    else:
        lines.append('# キー割り当て一覧')
        lines.append('')
        lines.append(
            f'※ {len(layers_data)} 個のレイヤーのキー割り当てを 1 ファイルに集約。'
            f'各レイヤー 66 バインディング位置を「動作」セクションでまとめてから「経路」セクションに進む。'
        )
        lines.append('')
        lines.append('- 各 row セクション行に「キーラベル」と「バインディング (`&...`)」の 2 段表示でキー位置を示す。')
        lines.append('- 各表の左端 1 列が「操作」（単発タップ / ダブルタップ / Shift+ / Ctrl+）または「■ Row N」見出し。')
        lines.append('')
        for mode_label, mode in [('動作', 'action'), ('経路', 'path')]:
            lines.append(f'## {mode_label}')
            lines.append('')
            for layer_name, bindings in layers_data:
                lines.append(f'### {layer_name} レイヤー')
                lines.append('')
                lines.extend(_markdown_layer_mode_rows(layer_name, bindings,
                                                       behaviors, macros, mode))

    output_path.write_text('\n'.join(lines) + '\n', encoding='utf-8')


# ============================================================================
# Main
# ============================================================================

def main() -> int:
    p = argparse.ArgumentParser(
        description='Generate Excel (.xlsx) and Markdown (.md) docs for one or more ZMK keymap layers'
    )
    p.add_argument('keymap', help='Path to .keymap file')
    p.add_argument('layers', nargs='+',
                   help='One or more layer names (e.g., VIM_NORMAL_1 VIM_NORMAL_2 VIM_VISUAL)')
    p.add_argument('-o', '--output', help='Output .xlsx path (default: <layer>_keymap.xlsx or keymap.xlsx)')
    args = p.parse_args()

    keymap_path = Path(args.keymap)
    if not keymap_path.is_file():
        print(f'error: keymap file not found: {keymap_path}', file=sys.stderr)
        return 1

    content = strip_comments(keymap_path.read_text(encoding='utf-8'))

    macros = parse_macros(content)
    behaviors = parse_behaviors(content)

    layers_data: list[tuple[str, list[str]]] = []
    for layer_name in args.layers:
        layer_text = parse_layer(content, layer_name)
        if layer_text is None:
            print(f'error: layer "{layer_name}" not found.', file=sys.stderr)
            return 1
        bindings = split_layer_bindings(layer_text)
        layers_data.append((layer_name, bindings))
        print(f'layer {layer_name}: {len(bindings)} bindings')

    print(f'parsed: {len(macros)} macros, {len(behaviors)} behaviors')

    if args.output:
        output_path = Path(args.output)
    elif len(args.layers) == 1:
        output_path = Path(f'{args.layers[0]}_keymap.xlsx')
    else:
        output_path = Path('keymap.xlsx')

    write_excel(layers_data, behaviors, macros, output_path)
    print(f'saved: {output_path}')

    md_path = output_path.with_suffix('.md')
    write_markdown(layers_data, behaviors, macros, md_path)
    print(f'saved: {md_path}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
