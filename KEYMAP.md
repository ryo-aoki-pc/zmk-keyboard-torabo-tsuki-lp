# VIM_NORMAL_1 レイヤー キー割り当て一覧

※ 66 個のバインディング位置。物理キーボード行ごとに 4 操作 × N キーの表で出力（QWERTY 配列）。

- 列ヘッダーは「キーラベル」と「バインディング (`&...`)」の 2 段表示。
- 各表の左端 1 列が「操作」（単発タップ / ダブルタップ / Shift+ / Ctrl+）。

## 動作

### Row 0 (top wing)

| 操作 | (outer)<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない |
| ダブルタップ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない |
| Shift+ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない |
| Ctrl+ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない |

### Row 1 (QWERTY 上段)

| 操作 | (outer)<br>`&none` | Q<br>`&none` | W<br>`&kp LC(RIGHT)` | E<br>`&kp LC(RIGHT)` | R<br>`&mm_vim_ctrl_r` | T<br>`&none` | Y<br>`&mm_vim_shift_y` | U<br>`&mm_vim_ctrl_u` | I<br>`&none` | O<br>`&mm_vim_shift_o` | P<br>`&kp LC(V)` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | 何もしない | Ctrl+→ 入力 | Ctrl+→ 入力 | 何もしない | 何もしない | Ctrl+C 入力 | Ctrl+Z 入力 | 何もしない | END → ENTER | Ctrl+V 入力 | 何もしない |
| ダブルタップ | 何もしない | 何もしない | Ctrl+→ 入力 × 2 | Ctrl+→ 入力 × 2 | 何もしない | 何もしない | HOME → Shift+END → Ctrl+C | Ctrl+Z 入力 × 2 | 何もしない | END → ENTER（2 回実行） | Ctrl+V 入力 × 2 | 何もしない |
| Shift+ | 何もしない | 何もしない | Shift + Ctrl+→（OS で合成） | Shift + Ctrl+→（OS で合成） | 何もしない | 何もしない | Shift+END → Ctrl+C | Shift + Ctrl+Z（OS で合成） | 何もしない | HOME → ENTER → ↑ | Shift + Ctrl+V（OS で合成） | 何もしない |
| Ctrl+ | 何もしない | 何もしない | Ctrl + Ctrl+→（OS で合成） | Ctrl + Ctrl+→（OS で合成） | Ctrl+Y 入力 | 何もしない | Ctrl + Ctrl+C（OS で合成） | PAGE_UP 入力 | 何もしない | END → ENTER（Ctrl 物理保持で実行） | Ctrl + Ctrl+V（OS で合成） | 何もしない |

### Row 2 (home row)

| 操作 | (outer)<br>`&none` | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&mm_vim_ctrl_then_shift_d` | F<br>`&none` | G<br>`&mm_vim_g` | (center L)<br>`&none` | (center R)<br>`&none` | H<br>`&kp LEFT` | J<br>`&mm_vim_j` | K<br>`&kp UP_ARROW` | L<br>`&kp RIGHT` | MINUS<br>`&kp RCTRL` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | Left Ctrl 入力 | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | ← 入力 | ↓ 入力 | ↑ 入力 | → 入力 | Right Ctrl 入力 | 何もしない |
| ダブルタップ | 何もしない | Left Ctrl 入力 × 2 | 何もしない | HOME → Shift+END → Ctrl+X | 何もしない | Ctrl+HOME 入力 | 何もしない | 何もしない | ← 入力 × 2 | ↓ 入力 × 2 | ↑ 入力 × 2 | → 入力 × 2 | Right Ctrl 入力 × 2 | 何もしない |
| Shift+ | 何もしない | Shift + Left Ctrl（OS で合成） | 何もしない | Shift+END → Ctrl+X | 何もしない | Ctrl+END 入力 | 何もしない | 何もしない | Shift + ←（OS で合成） | END → DELETE → SPACE | Shift + ↑（OS で合成） | Shift + →（OS で合成） | Shift + Right Ctrl（OS で合成） | 何もしない |
| Ctrl+ | 何もしない | Ctrl + Left Ctrl（OS で合成） | 何もしない | PAGE_DOWN 入力 | 何もしない | 何もしない | 何もしない | 何もしない | Ctrl + ←（OS で合成） | Ctrl + ↓（OS で合成） | Ctrl + ↑（OS で合成） | Ctrl + →（OS で合成） | Ctrl + Right Ctrl（OS で合成） | 何もしない |

### Row 3 (Z row)

| 操作 | (outer)<br>`&none` | Z<br>`&kp LEFT_SHIFT` | X<br>`&kp DELETE` | C<br>`&none` | V<br>`&mm_vim_v` | B<br>`&kp LC(LEFT)` | (center L)<br>`&none` | (center R)<br>`&none` | N<br>`&none` | M<br>`&none` | COMMA<br>`&none` | PERIOD<br>`&none` | SLASH<br>`&kp RIGHT_SHIFT` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | Left Shift 入力 | DELETE 入力 | 何もしない | レイヤー 8 に切替 | Ctrl+← 入力 | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Right Shift 入力 | 何もしない |
| ダブルタップ | 何もしない | Left Shift 入力 × 2 | DELETE 入力 × 2 | 何もしない | レイヤー 8 に切替 | Ctrl+← 入力 × 2 | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Right Shift 入力 × 2 | 何もしない |
| Shift+ | 何もしない | Shift + Left Shift（OS で合成） | Shift + DELETE（OS で合成） | 何もしない | HOME → Shift+↓ → レイヤー 8 へ | Shift + Ctrl+←（OS で合成） | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Shift + Right Shift（OS で合成） | 何もしない |
| Ctrl+ | 何もしない | Ctrl + Left Shift（OS で合成） | Ctrl + DELETE（OS で合成） | 何もしない | レイヤー 8 に切替 | Ctrl + Ctrl+←（OS で合成） | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Ctrl + Right Shift（OS で合成） | 何もしない |

### Row 4 (thumb)

| 操作 | (outer)<br>`&none` | mo6 (outer)<br>`&none` | LEFT_WIN<br>`&trans` | LEFT_ALT<br>`&trans` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | (mo1 center)<br>`&mo 3` | (mo2 center)<br>`&none` | lt1 ENTER<br>`&lt 3 ENTER` | (none)<br>`&none` | (none)<br>`&none` | mo6<br>`&trans` | mo6 (outer)<br>`&none` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | レイヤー 3 を momentary（押下中のみ）有効化 | 何もしない | ENTER 入力（タップ） | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない |
| ダブルタップ | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | レイヤー 3 を momentary（押下中のみ）有効化 | 何もしない | ENTER 入力 × 2 | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない |
| Shift+ | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | レイヤー 3 を momentary（押下中のみ）有効化 | 何もしない | Shift + ENTER（ホールドでレイヤー 3） | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない |
| Ctrl+ | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | レイヤー 3 を momentary（押下中のみ）有効化 | 何もしない | Ctrl + ENTER（ホールドでレイヤー 3） | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない |

## 経路

### Row 0 (top wing)

| 操作 | (outer)<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| ダブルタップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| Shift+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| Ctrl+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |

### Row 1 (QWERTY 上段)

| 操作 | (outer)<br>`&none` | Q<br>`&none` | W<br>`&kp LC(RIGHT)` | E<br>`&kp LC(RIGHT)` | R<br>`&mm_vim_ctrl_r` | T<br>`&none` | Y<br>`&mm_vim_shift_y` | U<br>`&mm_vim_ctrl_u` | I<br>`&none` | O<br>`&mm_vim_shift_o` | P<br>`&kp LC(V)` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &none | &kp LC(RIGHT) | &kp LC(RIGHT) | mm_vim_ctrl_r[0] → &none | &none | mm_vim_shift_y[0] → td_vim_y[0] → &kp LC(C) | mm_vim_ctrl_u[0] → &kp LC(Z) | &none | mm_vim_shift_o[0] → macro_vim_o | &kp LC(V) | &none |
| ダブルタップ | &none | &none | &kp LC(RIGHT)（tap-dance 未定義、連打） | &kp LC(RIGHT)（tap-dance 未定義、連打） | mm_vim_ctrl_r[0] → &none | &none | mm_vim_shift_y[0] → td_vim_y[1] → macro_vim_yy | mm_vim_ctrl_u[0] → &kp LC(Z)（tap-dance 未定義、連打） | &none | mm_vim_shift_o[0] → macro_vim_o（連打） | &kp LC(V)（tap-dance 未定義、連打） | &none |
| Shift+ | &none | &none | &kp LC(RIGHT)（物理 Shift は HID にそのまま伝わる） | &kp LC(RIGHT)（物理 Shift は HID にそのまま伝わる） | mm_vim_ctrl_r[0] (Shift は本 mod-morph 検知外) → &none | &none | mm_vim_shift_y[1] (Shift 検知) → macro_vim_shift_y | mm_vim_ctrl_u[0] (Shift は本 mod-morph 検知外) → &kp LC(Z)（物理 Shift は HID にそのまま伝わる） | &none | mm_vim_shift_o[1] (Shift 検知) → macro_vim_shift_o | &kp LC(V)（物理 Shift は HID にそのまま伝わる） | &none |
| Ctrl+ | &none | &none | &kp LC(RIGHT)（物理 Ctrl は HID にそのまま伝わる） | &kp LC(RIGHT)（物理 Ctrl は HID にそのまま伝わる） | mm_vim_ctrl_r[1] (Ctrl 検知) → &kp LC(Y) | &none | mm_vim_shift_y[0] (Ctrl は本 mod-morph 検知外) → td_vim_y[0] (tap-dance は mods 検知なし) → &kp LC(C)（物理 Ctrl は HID にそのまま伝わる） | mm_vim_ctrl_u[1] (Ctrl 検知) → &kp PAGE_UP | &none | mm_vim_shift_o[0] (Ctrl は本 mod-morph 検知外) → macro_vim_o | &kp LC(V)（物理 Ctrl は HID にそのまま伝わる） | &none |

### Row 2 (home row)

| 操作 | (outer)<br>`&none` | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&mm_vim_ctrl_then_shift_d` | F<br>`&none` | G<br>`&mm_vim_g` | (center L)<br>`&none` | (center R)<br>`&none` | H<br>`&kp LEFT` | J<br>`&mm_vim_j` | K<br>`&kp UP_ARROW` | L<br>`&kp RIGHT` | MINUS<br>`&kp RCTRL` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &kp LCTRL | &none | mm_vim_ctrl_then_shift_d[0] → mm_vim_shift_d[0] → td_vim_d[0] → &none | &none | mm_vim_g[0] → td_vim_g[0] → &none | &none | &none | &kp LEFT | mm_vim_j[0] → &kp DOWN | &kp UP_ARROW | &kp RIGHT | &kp RCTRL | &none |
| ダブルタップ | &none | &kp LCTRL（tap-dance 未定義、連打） | &none | mm_vim_ctrl_then_shift_d[0] → mm_vim_shift_d[0] → td_vim_d[1] → macro_vim_dd | &none | mm_vim_g[0] → td_vim_g[1] → &kp LC(HOME) | &none | &none | &kp LEFT（tap-dance 未定義、連打） | mm_vim_j[0] → &kp DOWN（tap-dance 未定義、連打） | &kp UP_ARROW（tap-dance 未定義、連打） | &kp RIGHT（tap-dance 未定義、連打） | &kp RCTRL（tap-dance 未定義、連打） | &none |
| Shift+ | &none | &kp LCTRL（物理 Shift は HID にそのまま伝わる） | &none | mm_vim_ctrl_then_shift_d[0] (Shift は本 mod-morph 検知外) → mm_vim_shift_d[1] (Shift 検知) → macro_vim_shift_d | &none | mm_vim_g[1] (Shift 検知) → &kp LC(END) | &none | &none | &kp LEFT（物理 Shift は HID にそのまま伝わる） | mm_vim_j[1] (Shift 検知) → macro_vim_join | &kp UP_ARROW（物理 Shift は HID にそのまま伝わる） | &kp RIGHT（物理 Shift は HID にそのまま伝わる） | &kp RCTRL（物理 Shift は HID にそのまま伝わる） | &none |
| Ctrl+ | &none | &kp LCTRL（物理 Ctrl は HID にそのまま伝わる） | &none | mm_vim_ctrl_then_shift_d[1] (Ctrl 検知) → &kp PAGE_DOWN | &none | mm_vim_g[0] (Ctrl は本 mod-morph 検知外) → td_vim_g[0] (tap-dance は mods 検知なし) → &none | &none | &none | &kp LEFT（物理 Ctrl は HID にそのまま伝わる） | mm_vim_j[0] (Ctrl は本 mod-morph 検知外) → &kp DOWN（物理 Ctrl は HID にそのまま伝わる） | &kp UP_ARROW（物理 Ctrl は HID にそのまま伝わる） | &kp RIGHT（物理 Ctrl は HID にそのまま伝わる） | &kp RCTRL（物理 Ctrl は HID にそのまま伝わる） | &none |

### Row 3 (Z row)

| 操作 | (outer)<br>`&none` | Z<br>`&kp LEFT_SHIFT` | X<br>`&kp DELETE` | C<br>`&none` | V<br>`&mm_vim_v` | B<br>`&kp LC(LEFT)` | (center L)<br>`&none` | (center R)<br>`&none` | N<br>`&none` | M<br>`&none` | COMMA<br>`&none` | PERIOD<br>`&none` | SLASH<br>`&kp RIGHT_SHIFT` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &kp LEFT_SHIFT | &kp DELETE | &none | mm_vim_v[0] → &to 8 | &kp LC(LEFT) | &none | &none | &none | &none | &none | &none | &kp RIGHT_SHIFT | &none |
| ダブルタップ | &none | &kp LEFT_SHIFT（tap-dance 未定義、連打） | &kp DELETE（tap-dance 未定義、連打） | &none | mm_vim_v[0] → &to 8 | &kp LC(LEFT)（tap-dance 未定義、連打） | &none | &none | &none | &none | &none | &none | &kp RIGHT_SHIFT（tap-dance 未定義、連打） | &none |
| Shift+ | &none | &kp LEFT_SHIFT（物理 Shift は HID にそのまま伝わる） | &kp DELETE（物理 Shift は HID にそのまま伝わる） | &none | mm_vim_v[1] (Shift 検知) → macro_vim_v_line | &kp LC(LEFT)（物理 Shift は HID にそのまま伝わる） | &none | &none | &none | &none | &none | &none | &kp RIGHT_SHIFT（物理 Shift は HID にそのまま伝わる） | &none |
| Ctrl+ | &none | &kp LEFT_SHIFT（物理 Ctrl は HID にそのまま伝わる） | &kp DELETE（物理 Ctrl は HID にそのまま伝わる） | &none | mm_vim_v[0] (Ctrl は本 mod-morph 検知外) → &to 8 | &kp LC(LEFT)（物理 Ctrl は HID にそのまま伝わる） | &none | &none | &none | &none | &none | &none | &kp RIGHT_SHIFT（物理 Ctrl は HID にそのまま伝わる） | &none |

### Row 4 (thumb)

| 操作 | (outer)<br>`&none` | mo6 (outer)<br>`&none` | LEFT_WIN<br>`&trans` | LEFT_ALT<br>`&trans` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | (mo1 center)<br>`&mo 3` | (mo2 center)<br>`&none` | lt1 ENTER<br>`&lt 3 ENTER` | (none)<br>`&none` | (none)<br>`&none` | mo6<br>`&trans` | mo6 (outer)<br>`&none` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &none | &trans | &trans | &none | &none | &mo 3 | &none | &lt 3 ENTER | &none | &none | &trans | &none | &none |
| ダブルタップ | &none | &none | &trans | &trans | &none | &none | &mo 3 | &none | &lt 3 ENTER（連打） | &none | &none | &trans | &none | &none |
| Shift+ | &none | &none | &trans | &trans | &none | &none | &mo 3 | &none | &lt 3 ENTER | &none | &none | &trans | &none | &none |
| Ctrl+ | &none | &none | &trans | &trans | &none | &none | &mo 3 | &none | &lt 3 ENTER | &none | &none | &trans | &none | &none |

