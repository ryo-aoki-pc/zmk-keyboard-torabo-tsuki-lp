# キー割り当て一覧

3 個のレイヤーのキー割り当てを 1 ファイルに集約。

## VIM_NORMAL_1 レイヤー キー割り当て一覧

※ 66 個のバインディング位置。物理キーボード行ごとに 4 操作 × N キーの表で出力（QWERTY 配列）。

- 列ヘッダーは「キーラベル」と「バインディング (`&...`)」の 2 段表示。
- 各表の左端 1 列が「操作」（単発タップ / ダブルタップ / Shift+ / Ctrl+）。

### 動作

#### Row 0 (top wing)

| 操作 | (outer)<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない |
| ダブルタップ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない |
| Shift+ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない |
| Ctrl+ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない |

#### Row 1 (QWERTY 上段)

| 操作 | (outer)<br>`&none` | Q<br>`&mm_vim_q` | W<br>`&mm_vim_w` | E<br>`&kp LC(RIGHT)` | R<br>`&mm_vim_ctrl_r` | T<br>`&none` | Y<br>`&mm_vim_shift_y` | U<br>`&mm_vim_ctrl_u` | I<br>`&kp HOME` | O<br>`&mm_vim_shift_o` | P<br>`&kp LC(V)` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | ESC 入力 | Ctrl+→ 入力 | Ctrl+→ 入力 | 何もしない | 何もしない | Ctrl+C 入力 | Ctrl+Z 入力 | HOME 入力 | END → ENTER | Ctrl+V 入力 | 何もしない |
| ダブルタップ | 何もしない | ESC 入力 × 2 | Ctrl+→ 入力 × 2 | Ctrl+→ 入力 × 2 | 何もしない | 何もしない | HOME → Shift+END → Ctrl+C | Ctrl+Z 入力 × 2 | HOME 入力 × 2 | END → ENTER（2 回実行） | Ctrl+V 入力 × 2 | 何もしない |
| Shift+ | 何もしない | Ctrl+Q 入力 | Shift + Ctrl+→（OS で合成） | Shift + Ctrl+→（OS で合成） | 何もしない | 何もしない | Shift+END → Ctrl+C | Shift + Ctrl+Z（OS で合成） | Shift + HOME（OS で合成） | HOME → ENTER → ↑ | Shift + Ctrl+V（OS で合成） | 何もしない |
| Ctrl+ | 何もしない | Ctrl + ESC（OS で合成） | Ctrl+BACKSPACE 入力 | Ctrl + Ctrl+→（OS で合成） | Ctrl+Y 入力 | 何もしない | Ctrl + Ctrl+C（OS で合成） | PAGE_UP 入力 | Ctrl + HOME（OS で合成） | END → ENTER（Ctrl 物理保持で実行） | Ctrl + Ctrl+V（OS で合成） | 何もしない |

#### Row 2 (home row)

| 操作 | (outer)<br>`&none` | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&mm_vim_ctrl_then_shift_d` | F<br>`&none` | G<br>`&mm_vim_g` | (center L)<br>`&none` | (center R)<br>`&none` | H<br>`&kp LEFT` | J<br>`&mm_vim_j` | K<br>`&kp UP_ARROW` | L<br>`&kp RIGHT` | MINUS<br>`&kp RCTRL` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | Left Ctrl 入力 | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | ← 入力 | ↓ 入力 | ↑ 入力 | → 入力 | Right Ctrl 入力 | 何もしない |
| ダブルタップ | 何もしない | Left Ctrl 入力 × 2 | 何もしない | HOME → Shift+END → Ctrl+X | 何もしない | Ctrl+HOME 入力 | 何もしない | 何もしない | ← 入力 × 2 | ↓ 入力 × 2 | ↑ 入力 × 2 | → 入力 × 2 | Right Ctrl 入力 × 2 | 何もしない |
| Shift+ | 何もしない | Shift + Left Ctrl（OS で合成） | 何もしない | Shift+END → Ctrl+X | 何もしない | Ctrl+END 入力 | 何もしない | 何もしない | Shift + ←（OS で合成） | END → DELETE → SPACE | Shift + ↑（OS で合成） | Shift + →（OS で合成） | Shift + Right Ctrl（OS で合成） | 何もしない |
| Ctrl+ | 何もしない | Ctrl + Left Ctrl（OS で合成） | 何もしない | PAGE_DOWN 入力 | 何もしない | 何もしない | 何もしない | 何もしない | Ctrl + ←（OS で合成） | Ctrl + ↓（OS で合成） | Ctrl + ↑（OS で合成） | Ctrl + →（OS で合成） | Ctrl + Right Ctrl（OS で合成） | 何もしない |

#### Row 3 (Z row)

| 操作 | (outer)<br>`&none` | Z<br>`&kp LEFT_SHIFT` | X<br>`&kp DELETE` | C<br>`&none` | V<br>`&mm_vim_v` | B<br>`&kp LC(LEFT)` | (center L)<br>`&none` | (center R)<br>`&none` | N<br>`&mm_vim_n` | M<br>`&none` | COMMA<br>`&none` | PERIOD<br>`&none` | SLASH<br>`&kp RIGHT_SHIFT` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | Left Shift 入力 | DELETE 入力 | 何もしない | レイヤー 8 に切替 | Ctrl+← 入力 | 何もしない | 何もしない | F3 入力 | 何もしない | 何もしない | 何もしない | Right Shift 入力 | 何もしない |
| ダブルタップ | 何もしない | Left Shift 入力 × 2 | DELETE 入力 × 2 | 何もしない | レイヤー 8 に切替 | Ctrl+← 入力 × 2 | 何もしない | 何もしない | F3 入力 × 2 | 何もしない | 何もしない | 何もしない | Right Shift 入力 × 2 | 何もしない |
| Shift+ | 何もしない | Shift + Left Shift（OS で合成） | Shift + DELETE（OS で合成） | 何もしない | HOME → Shift+↓ → レイヤー 8 へ | Shift + Ctrl+←（OS で合成） | 何もしない | 何もしない | Shift+F3 入力 | 何もしない | 何もしない | 何もしない | Shift + Right Shift（OS で合成） | 何もしない |
| Ctrl+ | 何もしない | Ctrl + Left Shift（OS で合成） | Ctrl + DELETE（OS で合成） | 何もしない | レイヤー 8 に切替 | Ctrl + Ctrl+←（OS で合成） | 何もしない | 何もしない | Ctrl + F3（OS で合成） | 何もしない | 何もしない | 何もしない | Ctrl + Right Shift（OS で合成） | 何もしない |

#### Row 4 (thumb)

| 操作 | (outer)<br>`&none` | mo6 (outer)<br>`&none` | LEFT_WIN<br>`&trans` | LEFT_ALT<br>`&trans` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | (mo1 center)<br>`&mo 3` | (mo2 center)<br>`&none` | lt1 ENTER<br>`&lt 3 ENTER` | (none)<br>`&none` | (none)<br>`&none` | mo6<br>`&trans` | mo6 (outer)<br>`&none` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | レイヤー 3 を momentary（押下中のみ）有効化 | 何もしない | ENTER 入力（タップ） | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない |
| ダブルタップ | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | レイヤー 3 を momentary（押下中のみ）有効化 | 何もしない | ENTER 入力 × 2 | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない |
| Shift+ | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | レイヤー 3 を momentary（押下中のみ）有効化 | 何もしない | Shift + ENTER（ホールドでレイヤー 3） | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない |
| Ctrl+ | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | レイヤー 3 を momentary（押下中のみ）有効化 | 何もしない | Ctrl + ENTER（ホールドでレイヤー 3） | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない |

### 経路

#### Row 0 (top wing)

| 操作 | (outer)<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| ダブルタップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| Shift+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| Ctrl+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |

#### Row 1 (QWERTY 上段)

| 操作 | (outer)<br>`&none` | Q<br>`&mm_vim_q` | W<br>`&mm_vim_w` | E<br>`&kp LC(RIGHT)` | R<br>`&mm_vim_ctrl_r` | T<br>`&none` | Y<br>`&mm_vim_shift_y` | U<br>`&mm_vim_ctrl_u` | I<br>`&kp HOME` | O<br>`&mm_vim_shift_o` | P<br>`&kp LC(V)` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | mm_vim_q[0] → &kp ESCAPE | mm_vim_w[0] → &kp LC(RIGHT) | &kp LC(RIGHT) | mm_vim_ctrl_r[0] → &none | &none | mm_vim_shift_y[0] → td_vim_y[0] → &kp LC(C) | mm_vim_ctrl_u[0] → &kp LC(Z) | &kp HOME | mm_vim_shift_o[0] → macro_vim_o | &kp LC(V) | &none |
| ダブルタップ | &none | mm_vim_q[0] → &kp ESCAPE（tap-dance 未定義、連打） | mm_vim_w[0] → &kp LC(RIGHT)（tap-dance 未定義、連打） | &kp LC(RIGHT)（tap-dance 未定義、連打） | mm_vim_ctrl_r[0] → &none | &none | mm_vim_shift_y[0] → td_vim_y[1] → macro_vim_yy | mm_vim_ctrl_u[0] → &kp LC(Z)（tap-dance 未定義、連打） | &kp HOME（tap-dance 未定義、連打） | mm_vim_shift_o[0] → macro_vim_o（連打） | &kp LC(V)（tap-dance 未定義、連打） | &none |
| Shift+ | &none | mm_vim_q[1] (Shift 検知) → &kp LC(Q) | mm_vim_w[0] (Shift は本 mod-morph 検知外) → &kp LC(RIGHT)（物理 Shift は HID にそのまま伝わる） | &kp LC(RIGHT)（物理 Shift は HID にそのまま伝わる） | mm_vim_ctrl_r[0] (Shift は本 mod-morph 検知外) → &none | &none | mm_vim_shift_y[1] (Shift 検知) → macro_vim_shift_y | mm_vim_ctrl_u[0] (Shift は本 mod-morph 検知外) → &kp LC(Z)（物理 Shift は HID にそのまま伝わる） | &kp HOME（物理 Shift は HID にそのまま伝わる） | mm_vim_shift_o[1] (Shift 検知) → macro_vim_shift_o | &kp LC(V)（物理 Shift は HID にそのまま伝わる） | &none |
| Ctrl+ | &none | mm_vim_q[0] (Ctrl は本 mod-morph 検知外) → &kp ESCAPE（物理 Ctrl は HID にそのまま伝わる） | mm_vim_w[1] (Ctrl 検知) → &kp LC(BACKSPACE) | &kp LC(RIGHT)（物理 Ctrl は HID にそのまま伝わる） | mm_vim_ctrl_r[1] (Ctrl 検知) → &kp LC(Y) | &none | mm_vim_shift_y[0] (Ctrl は本 mod-morph 検知外) → td_vim_y[0] (tap-dance は mods 検知なし) → &kp LC(C)（物理 Ctrl は HID にそのまま伝わる） | mm_vim_ctrl_u[1] (Ctrl 検知) → &kp PAGE_UP | &kp HOME（物理 Ctrl は HID にそのまま伝わる） | mm_vim_shift_o[0] (Ctrl は本 mod-morph 検知外) → macro_vim_o | &kp LC(V)（物理 Ctrl は HID にそのまま伝わる） | &none |

#### Row 2 (home row)

| 操作 | (outer)<br>`&none` | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&mm_vim_ctrl_then_shift_d` | F<br>`&none` | G<br>`&mm_vim_g` | (center L)<br>`&none` | (center R)<br>`&none` | H<br>`&kp LEFT` | J<br>`&mm_vim_j` | K<br>`&kp UP_ARROW` | L<br>`&kp RIGHT` | MINUS<br>`&kp RCTRL` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &kp LCTRL | &none | mm_vim_ctrl_then_shift_d[0] → mm_vim_shift_d[0] → td_vim_d[0] → &none | &none | mm_vim_g[0] → td_vim_g[0] → &none | &none | &none | &kp LEFT | mm_vim_j[0] → &kp DOWN | &kp UP_ARROW | &kp RIGHT | &kp RCTRL | &none |
| ダブルタップ | &none | &kp LCTRL（tap-dance 未定義、連打） | &none | mm_vim_ctrl_then_shift_d[0] → mm_vim_shift_d[0] → td_vim_d[1] → macro_vim_dd | &none | mm_vim_g[0] → td_vim_g[1] → &kp LC(HOME) | &none | &none | &kp LEFT（tap-dance 未定義、連打） | mm_vim_j[0] → &kp DOWN（tap-dance 未定義、連打） | &kp UP_ARROW（tap-dance 未定義、連打） | &kp RIGHT（tap-dance 未定義、連打） | &kp RCTRL（tap-dance 未定義、連打） | &none |
| Shift+ | &none | &kp LCTRL（物理 Shift は HID にそのまま伝わる） | &none | mm_vim_ctrl_then_shift_d[0] (Shift は本 mod-morph 検知外) → mm_vim_shift_d[1] (Shift 検知) → macro_vim_shift_d | &none | mm_vim_g[1] (Shift 検知) → &kp LC(END) | &none | &none | &kp LEFT（物理 Shift は HID にそのまま伝わる） | mm_vim_j[1] (Shift 検知) → macro_vim_join | &kp UP_ARROW（物理 Shift は HID にそのまま伝わる） | &kp RIGHT（物理 Shift は HID にそのまま伝わる） | &kp RCTRL（物理 Shift は HID にそのまま伝わる） | &none |
| Ctrl+ | &none | &kp LCTRL（物理 Ctrl は HID にそのまま伝わる） | &none | mm_vim_ctrl_then_shift_d[1] (Ctrl 検知) → &kp PAGE_DOWN | &none | mm_vim_g[0] (Ctrl は本 mod-morph 検知外) → td_vim_g[0] (tap-dance は mods 検知なし) → &none | &none | &none | &kp LEFT（物理 Ctrl は HID にそのまま伝わる） | mm_vim_j[0] (Ctrl は本 mod-morph 検知外) → &kp DOWN（物理 Ctrl は HID にそのまま伝わる） | &kp UP_ARROW（物理 Ctrl は HID にそのまま伝わる） | &kp RIGHT（物理 Ctrl は HID にそのまま伝わる） | &kp RCTRL（物理 Ctrl は HID にそのまま伝わる） | &none |

#### Row 3 (Z row)

| 操作 | (outer)<br>`&none` | Z<br>`&kp LEFT_SHIFT` | X<br>`&kp DELETE` | C<br>`&none` | V<br>`&mm_vim_v` | B<br>`&kp LC(LEFT)` | (center L)<br>`&none` | (center R)<br>`&none` | N<br>`&mm_vim_n` | M<br>`&none` | COMMA<br>`&none` | PERIOD<br>`&none` | SLASH<br>`&kp RIGHT_SHIFT` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &kp LEFT_SHIFT | &kp DELETE | &none | mm_vim_v[0] → &to 8 | &kp LC(LEFT) | &none | &none | mm_vim_n[0] → &kp F3 | &none | &none | &none | &kp RIGHT_SHIFT | &none |
| ダブルタップ | &none | &kp LEFT_SHIFT（tap-dance 未定義、連打） | &kp DELETE（tap-dance 未定義、連打） | &none | mm_vim_v[0] → &to 8 | &kp LC(LEFT)（tap-dance 未定義、連打） | &none | &none | mm_vim_n[0] → &kp F3（tap-dance 未定義、連打） | &none | &none | &none | &kp RIGHT_SHIFT（tap-dance 未定義、連打） | &none |
| Shift+ | &none | &kp LEFT_SHIFT（物理 Shift は HID にそのまま伝わる） | &kp DELETE（物理 Shift は HID にそのまま伝わる） | &none | mm_vim_v[1] (Shift 検知) → macro_vim_v_line | &kp LC(LEFT)（物理 Shift は HID にそのまま伝わる） | &none | &none | mm_vim_n[1] (Shift 検知) → &kp LS(F3) | &none | &none | &none | &kp RIGHT_SHIFT（物理 Shift は HID にそのまま伝わる） | &none |
| Ctrl+ | &none | &kp LEFT_SHIFT（物理 Ctrl は HID にそのまま伝わる） | &kp DELETE（物理 Ctrl は HID にそのまま伝わる） | &none | mm_vim_v[0] (Ctrl は本 mod-morph 検知外) → &to 8 | &kp LC(LEFT)（物理 Ctrl は HID にそのまま伝わる） | &none | &none | mm_vim_n[0] (Ctrl は本 mod-morph 検知外) → &kp F3（物理 Ctrl は HID にそのまま伝わる） | &none | &none | &none | &kp RIGHT_SHIFT（物理 Ctrl は HID にそのまま伝わる） | &none |

#### Row 4 (thumb)

| 操作 | (outer)<br>`&none` | mo6 (outer)<br>`&none` | LEFT_WIN<br>`&trans` | LEFT_ALT<br>`&trans` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | (mo1 center)<br>`&mo 3` | (mo2 center)<br>`&none` | lt1 ENTER<br>`&lt 3 ENTER` | (none)<br>`&none` | (none)<br>`&none` | mo6<br>`&trans` | mo6 (outer)<br>`&none` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &none | &trans | &trans | &none | &none | &mo 3 | &none | &lt 3 ENTER | &none | &none | &trans | &none | &none |
| ダブルタップ | &none | &none | &trans | &trans | &none | &none | &mo 3 | &none | &lt 3 ENTER（連打） | &none | &none | &trans | &none | &none |
| Shift+ | &none | &none | &trans | &trans | &none | &none | &mo 3 | &none | &lt 3 ENTER | &none | &none | &trans | &none | &none |
| Ctrl+ | &none | &none | &trans | &trans | &none | &none | &mo 3 | &none | &lt 3 ENTER | &none | &none | &trans | &none | &none |

## VIM_NORMAL_2 レイヤー キー割り当て一覧

※ 66 個のバインディング位置。物理キーボード行ごとに 4 操作 × N キーの表で出力（QWERTY 配列）。

- 列ヘッダーは「キーラベル」と「バインディング (`&...`)」の 2 段表示。
- 各表の左端 1 列が「操作」（単発タップ / ダブルタップ / Shift+ / Ctrl+）。

### 動作

#### Row 0 (top wing)

| 操作 | (outer)<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない |
| ダブルタップ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない |
| Shift+ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない |
| Ctrl+ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない |

#### Row 1 (QWERTY 上段)

| 操作 | (outer)<br>`&none` | Q<br>`&trans` | W<br>`&none` | E<br>`&trans` | R<br>`&mm_vim_shift_4` | T<br>`&trans` | Y<br>`&mm_vim_shift_6` | U<br>`&kp PAGE_UP` | I<br>`&trans` | O<br>`&none` | P<br>`&kp HOME` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | PAGE_UP 入力 | 下位レイヤーの同位置にフォールスルー | 何もしない | HOME 入力 | 何もしない |
| ダブルタップ | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | PAGE_UP 入力 × 2 | 下位レイヤーの同位置にフォールスルー | 何もしない | HOME 入力 × 2 | 何もしない |
| Shift+ | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | 下位レイヤーの同位置にフォールスルー | END 入力 | 下位レイヤーの同位置にフォールスルー | HOME 入力 | Shift + PAGE_UP（OS で合成） | 下位レイヤーの同位置にフォールスルー | 何もしない | Shift + HOME（OS で合成） | 何もしない |
| Ctrl+ | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | Ctrl + PAGE_UP（OS で合成） | 下位レイヤーの同位置にフォールスルー | 何もしない | Ctrl + HOME（OS で合成） | 何もしない |

#### Row 2 (home row)

| 操作 | (outer)<br>`&none` | A<br>`&kp LCTRL` | S<br>`&trans` | D<br>`&kp PAGE_DOWN` | F<br>`&trans` | G<br>`&none` | (center L)<br>`&none` | (center R)<br>`&none` | H<br>`&trans` | J<br>`&trans` | K<br>`&trans` | L<br>`&trans` | MINUS<br>`&kp RCTRL` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | Left Ctrl 入力 | 下位レイヤーの同位置にフォールスルー | PAGE_DOWN 入力 | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | Right Ctrl 入力 | 何もしない |
| ダブルタップ | 何もしない | Left Ctrl 入力 × 2 | 下位レイヤーの同位置にフォールスルー | PAGE_DOWN 入力 × 2 | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | Right Ctrl 入力 × 2 | 何もしない |
| Shift+ | 何もしない | Shift + Left Ctrl（OS で合成） | 下位レイヤーの同位置にフォールスルー | Shift + PAGE_DOWN（OS で合成） | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | Shift + Right Ctrl（OS で合成） | 何もしない |
| Ctrl+ | 何もしない | Ctrl + Left Ctrl（OS で合成） | 下位レイヤーの同位置にフォールスルー | Ctrl + PAGE_DOWN（OS で合成） | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | Ctrl + Right Ctrl（OS で合成） | 何もしない |

#### Row 3 (Z row)

| 操作 | (outer)<br>`&none` | Z<br>`&kp LEFT_SHIFT` | X<br>`&none` | C<br>`&none` | V<br>`&none` | B<br>`&none` | (center L)<br>`&none` | (center R)<br>`&none` | N<br>`&trans` | M<br>`&trans` | COMMA<br>`&trans` | PERIOD<br>`&trans` | SLASH<br>`&kp RIGHT_SHIFT` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | Left Shift 入力 | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | Right Shift 入力 | 何もしない |
| ダブルタップ | 何もしない | Left Shift 入力 × 2 | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | Right Shift 入力 × 2 | 何もしない |
| Shift+ | 何もしない | Shift + Left Shift（OS で合成） | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | Shift + Right Shift（OS で合成） | 何もしない |
| Ctrl+ | 何もしない | Ctrl + Left Shift（OS で合成） | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | Ctrl + Right Shift（OS で合成） | 何もしない |

#### Row 4 (thumb)

| 操作 | (outer)<br>`&none` | mo6 (outer)<br>`&none` | LEFT_WIN<br>`&trans` | LEFT_ALT<br>`&trans` | lt2 SPACE<br>`&trans` | lt2 SPACE<br>`&none` | (mo1 center)<br>`&none` | (mo2 center)<br>`&none` | lt1 ENTER<br>`&none` | (none)<br>`&none` | (none)<br>`&none` | mo6<br>`&trans` | mo6 (outer)<br>`&none` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない |
| ダブルタップ | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない |
| Shift+ | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない |
| Ctrl+ | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない |

### 経路

#### Row 0 (top wing)

| 操作 | (outer)<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| ダブルタップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| Shift+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| Ctrl+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |

#### Row 1 (QWERTY 上段)

| 操作 | (outer)<br>`&none` | Q<br>`&trans` | W<br>`&none` | E<br>`&trans` | R<br>`&mm_vim_shift_4` | T<br>`&trans` | Y<br>`&mm_vim_shift_6` | U<br>`&kp PAGE_UP` | I<br>`&trans` | O<br>`&none` | P<br>`&kp HOME` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &trans | &none | &trans | mm_vim_shift_4[0] → &none | &trans | mm_vim_shift_6[0] → &none | &kp PAGE_UP | &trans | &none | &kp HOME | &none |
| ダブルタップ | &none | &trans | &none | &trans | mm_vim_shift_4[0] → &none | &trans | mm_vim_shift_6[0] → &none | &kp PAGE_UP（tap-dance 未定義、連打） | &trans | &none | &kp HOME（tap-dance 未定義、連打） | &none |
| Shift+ | &none | &trans | &none | &trans | mm_vim_shift_4[1] (Shift 検知) → &kp END | &trans | mm_vim_shift_6[1] (Shift 検知) → &kp HOME | &kp PAGE_UP（物理 Shift は HID にそのまま伝わる） | &trans | &none | &kp HOME（物理 Shift は HID にそのまま伝わる） | &none |
| Ctrl+ | &none | &trans | &none | &trans | mm_vim_shift_4[0] (Ctrl は本 mod-morph 検知外) → &none | &trans | mm_vim_shift_6[0] (Ctrl は本 mod-morph 検知外) → &none | &kp PAGE_UP（物理 Ctrl は HID にそのまま伝わる） | &trans | &none | &kp HOME（物理 Ctrl は HID にそのまま伝わる） | &none |

#### Row 2 (home row)

| 操作 | (outer)<br>`&none` | A<br>`&kp LCTRL` | S<br>`&trans` | D<br>`&kp PAGE_DOWN` | F<br>`&trans` | G<br>`&none` | (center L)<br>`&none` | (center R)<br>`&none` | H<br>`&trans` | J<br>`&trans` | K<br>`&trans` | L<br>`&trans` | MINUS<br>`&kp RCTRL` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &kp LCTRL | &trans | &kp PAGE_DOWN | &trans | &none | &none | &none | &trans | &trans | &trans | &trans | &kp RCTRL | &none |
| ダブルタップ | &none | &kp LCTRL（tap-dance 未定義、連打） | &trans | &kp PAGE_DOWN（tap-dance 未定義、連打） | &trans | &none | &none | &none | &trans | &trans | &trans | &trans | &kp RCTRL（tap-dance 未定義、連打） | &none |
| Shift+ | &none | &kp LCTRL（物理 Shift は HID にそのまま伝わる） | &trans | &kp PAGE_DOWN（物理 Shift は HID にそのまま伝わる） | &trans | &none | &none | &none | &trans | &trans | &trans | &trans | &kp RCTRL（物理 Shift は HID にそのまま伝わる） | &none |
| Ctrl+ | &none | &kp LCTRL（物理 Ctrl は HID にそのまま伝わる） | &trans | &kp PAGE_DOWN（物理 Ctrl は HID にそのまま伝わる） | &trans | &none | &none | &none | &trans | &trans | &trans | &trans | &kp RCTRL（物理 Ctrl は HID にそのまま伝わる） | &none |

#### Row 3 (Z row)

| 操作 | (outer)<br>`&none` | Z<br>`&kp LEFT_SHIFT` | X<br>`&none` | C<br>`&none` | V<br>`&none` | B<br>`&none` | (center L)<br>`&none` | (center R)<br>`&none` | N<br>`&trans` | M<br>`&trans` | COMMA<br>`&trans` | PERIOD<br>`&trans` | SLASH<br>`&kp RIGHT_SHIFT` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &kp LEFT_SHIFT | &none | &none | &none | &none | &none | &none | &trans | &trans | &trans | &trans | &kp RIGHT_SHIFT | &none |
| ダブルタップ | &none | &kp LEFT_SHIFT（tap-dance 未定義、連打） | &none | &none | &none | &none | &none | &none | &trans | &trans | &trans | &trans | &kp RIGHT_SHIFT（tap-dance 未定義、連打） | &none |
| Shift+ | &none | &kp LEFT_SHIFT（物理 Shift は HID にそのまま伝わる） | &none | &none | &none | &none | &none | &none | &trans | &trans | &trans | &trans | &kp RIGHT_SHIFT（物理 Shift は HID にそのまま伝わる） | &none |
| Ctrl+ | &none | &kp LEFT_SHIFT（物理 Ctrl は HID にそのまま伝わる） | &none | &none | &none | &none | &none | &none | &trans | &trans | &trans | &trans | &kp RIGHT_SHIFT（物理 Ctrl は HID にそのまま伝わる） | &none |

#### Row 4 (thumb)

| 操作 | (outer)<br>`&none` | mo6 (outer)<br>`&none` | LEFT_WIN<br>`&trans` | LEFT_ALT<br>`&trans` | lt2 SPACE<br>`&trans` | lt2 SPACE<br>`&none` | (mo1 center)<br>`&none` | (mo2 center)<br>`&none` | lt1 ENTER<br>`&none` | (none)<br>`&none` | (none)<br>`&none` | mo6<br>`&trans` | mo6 (outer)<br>`&none` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &none | &trans | &trans | &trans | &none | &none | &none | &none | &none | &none | &trans | &none | &none |
| ダブルタップ | &none | &none | &trans | &trans | &trans | &none | &none | &none | &none | &none | &none | &trans | &none | &none |
| Shift+ | &none | &none | &trans | &trans | &trans | &none | &none | &none | &none | &none | &none | &trans | &none | &none |
| Ctrl+ | &none | &none | &trans | &trans | &trans | &none | &none | &none | &none | &none | &none | &trans | &none | &none |

## VIM_VISUAL レイヤー キー割り当て一覧

※ 66 個のバインディング位置。物理キーボード行ごとに 4 操作 × N キーの表で出力（QWERTY 配列）。

- 列ヘッダーは「キーラベル」と「バインディング (`&...`)」の 2 段表示。
- 各表の左端 1 列が「操作」（単発タップ / ダブルタップ / Shift+ / Ctrl+）。

### 動作

#### Row 0 (top wing)

| 操作 | (outer)<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない |
| ダブルタップ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない |
| Shift+ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない |
| Ctrl+ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない |

#### Row 1 (QWERTY 上段)

| 操作 | (outer)<br>`&none` | Q<br>`&macro_vim_visual_exit` | W<br>`&kp LS(LC(RIGHT))` | E<br>`&kp LS(LC(RIGHT))` | R<br>`&kp LS(END)` | T<br>`&none` | Y<br>`&macro_vim_visual_y` | U<br>`&kp LS(PAGE_UP)` | I<br>`&kp LS(HOME)` | O<br>`&none` | P<br>`&macro_vim_visual_p` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ | Shift+Ctrl+→ 入力 | Shift+Ctrl+→ 入力 | Shift+END 入力 | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+C → → → レイヤー 0 へ | Shift+PAGE_UP 入力 | Shift+HOME 入力 | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+V → レイヤー 0 へ | 何もしない |
| ダブルタップ | 何もしない | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（2 回実行） | Shift+Ctrl+→ 入力 × 2 | Shift+Ctrl+→ 入力 × 2 | Shift+END 入力 × 2 | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+C → → → レイヤー 0 へ（2 回実行） | Shift+PAGE_UP 入力 × 2 | Shift+HOME 入力 × 2 | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+V → レイヤー 0 へ（2 回実行） | 何もしない |
| Shift+ | 何もしない | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（Shift 物理保持で実行） | Shift + Shift+Ctrl+→（OS で合成） | Shift + Shift+Ctrl+→（OS で合成） | Shift + Shift+END（OS で合成） | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+C → → → レイヤー 0 へ（Shift 物理保持で実行） | Shift + Shift+PAGE_UP（OS で合成） | Shift + Shift+HOME（OS で合成） | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+V → レイヤー 0 へ（Shift 物理保持で実行） | 何もしない |
| Ctrl+ | 何もしない | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（Ctrl 物理保持で実行） | Ctrl + Shift+Ctrl+→（OS で合成） | Ctrl + Shift+Ctrl+→（OS で合成） | Ctrl + Shift+END（OS で合成） | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+C → → → レイヤー 0 へ（Ctrl 物理保持で実行） | Ctrl + Shift+PAGE_UP（OS で合成） | Ctrl + Shift+HOME（OS で合成） | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+V → レイヤー 0 へ（Ctrl 物理保持で実行） | 何もしない |

#### Row 2 (home row)

| 操作 | (outer)<br>`&none` | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&macro_vim_visual_cut` | F<br>`&none` | G<br>`&mm_vim_visual_g` | (center L)<br>`&none` | (center R)<br>`&none` | H<br>`&kp LS(LEFT)` | J<br>`&kp LS(DOWN)` | K<br>`&kp LS(UP)` | L<br>`&kp LS(RIGHT)` | MINUS<br>`&kp RCTRL` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | Left Ctrl 入力 | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ | 何もしない | 何もしない | 何もしない | 何もしない | Shift+← 入力 | Shift+↓ 入力 | Shift+UP 入力 | Shift+→ 入力 | Right Ctrl 入力 | 何もしない |
| ダブルタップ | 何もしない | Left Ctrl 入力 × 2 | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ（2 回実行） | 何もしない | Shift+Ctrl+HOME 入力 | 何もしない | 何もしない | Shift+← 入力 × 2 | Shift+↓ 入力 × 2 | Shift+UP 入力 × 2 | Shift+→ 入力 × 2 | Right Ctrl 入力 × 2 | 何もしない |
| Shift+ | 何もしない | Shift + Left Ctrl（OS で合成） | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ（Shift 物理保持で実行） | 何もしない | Shift+Ctrl+END 入力 | 何もしない | 何もしない | Shift + Shift+←（OS で合成） | Shift + Shift+↓（OS で合成） | Shift + Shift+UP（OS で合成） | Shift + Shift+→（OS で合成） | Shift + Right Ctrl（OS で合成） | 何もしない |
| Ctrl+ | 何もしない | Ctrl + Left Ctrl（OS で合成） | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ（Ctrl 物理保持で実行） | 何もしない | 何もしない | 何もしない | 何もしない | Ctrl + Shift+←（OS で合成） | Ctrl + Shift+↓（OS で合成） | Ctrl + Shift+UP（OS で合成） | Ctrl + Shift+→（OS で合成） | Ctrl + Right Ctrl（OS で合成） | 何もしない |

#### Row 3 (Z row)

| 操作 | (outer)<br>`&none` | Z<br>`&kp LEFT_SHIFT` | X<br>`&macro_vim_visual_cut` | C<br>`&macro_vim_visual_cut` | V<br>`&macro_vim_visual_exit` | B<br>`&kp LS(LC(LEFT))` | (center L)<br>`&none` | (center R)<br>`&none` | N<br>`&kp F3` | M<br>`&none` | COMMA<br>`&none` | PERIOD<br>`&none` | SLASH<br>`&kp RIGHT_SHIFT` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | Left Shift 入力 | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ | Shift+Ctrl+← 入力 | 何もしない | 何もしない | F3 入力 | 何もしない | 何もしない | 何もしない | Right Shift 入力 | 何もしない |
| ダブルタップ | 何もしない | Left Shift 入力 × 2 | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ（2 回実行） | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ（2 回実行） | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（2 回実行） | Shift+Ctrl+← 入力 × 2 | 何もしない | 何もしない | F3 入力 × 2 | 何もしない | 何もしない | 何もしない | Right Shift 入力 × 2 | 何もしない |
| Shift+ | 何もしない | Shift + Left Shift（OS で合成） | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ（Shift 物理保持で実行） | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ（Shift 物理保持で実行） | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（Shift 物理保持で実行） | Shift + Shift+Ctrl+←（OS で合成） | 何もしない | 何もしない | Shift + F3（OS で合成） | 何もしない | 何もしない | 何もしない | Shift + Right Shift（OS で合成） | 何もしない |
| Ctrl+ | 何もしない | Ctrl + Left Shift（OS で合成） | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ（Ctrl 物理保持で実行） | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ（Ctrl 物理保持で実行） | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（Ctrl 物理保持で実行） | Ctrl + Shift+Ctrl+←（OS で合成） | 何もしない | 何もしない | Ctrl + F3（OS で合成） | 何もしない | 何もしない | 何もしない | Ctrl + Right Shift（OS で合成） | 何もしない |

#### Row 4 (thumb)

| 操作 | (outer)<br>`&none` | mo6 (outer)<br>`&none` | LEFT_WIN<br>`&none` | LEFT_ALT<br>`&none` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | (mo1 center)<br>`&macro_vim_visual_exit` | (mo2 center)<br>`&macro_vim_visual_exit` | lt1 ENTER<br>`&macro_vim_visual_exit` | (none)<br>`&none` | (none)<br>`&none` | mo6<br>`&none` | mo6 (outer)<br>`&none` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない |
| ダブルタップ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（2 回実行） | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（2 回実行） | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（2 回実行） | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない |
| Shift+ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（Shift 物理保持で実行） | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（Shift 物理保持で実行） | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（Shift 物理保持で実行） | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない |
| Ctrl+ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（Ctrl 物理保持で実行） | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（Ctrl 物理保持で実行） | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（Ctrl 物理保持で実行） | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない |

### 経路

#### Row 0 (top wing)

| 操作 | (outer)<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| ダブルタップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| Shift+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| Ctrl+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |

#### Row 1 (QWERTY 上段)

| 操作 | (outer)<br>`&none` | Q<br>`&macro_vim_visual_exit` | W<br>`&kp LS(LC(RIGHT))` | E<br>`&kp LS(LC(RIGHT))` | R<br>`&kp LS(END)` | T<br>`&none` | Y<br>`&macro_vim_visual_y` | U<br>`&kp LS(PAGE_UP)` | I<br>`&kp LS(HOME)` | O<br>`&none` | P<br>`&macro_vim_visual_p` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | macro_vim_visual_exit | &kp LS(LC(RIGHT)) | &kp LS(LC(RIGHT)) | &kp LS(END) | &none | macro_vim_visual_y | &kp LS(PAGE_UP) | &kp LS(HOME) | &none | macro_vim_visual_p | &none |
| ダブルタップ | &none | macro_vim_visual_exit（連打） | &kp LS(LC(RIGHT))（tap-dance 未定義、連打） | &kp LS(LC(RIGHT))（tap-dance 未定義、連打） | &kp LS(END)（tap-dance 未定義、連打） | &none | macro_vim_visual_y（連打） | &kp LS(PAGE_UP)（tap-dance 未定義、連打） | &kp LS(HOME)（tap-dance 未定義、連打） | &none | macro_vim_visual_p（連打） | &none |
| Shift+ | &none | macro_vim_visual_exit | &kp LS(LC(RIGHT))（物理 Shift は HID にそのまま伝わる） | &kp LS(LC(RIGHT))（物理 Shift は HID にそのまま伝わる） | &kp LS(END)（物理 Shift は HID にそのまま伝わる） | &none | macro_vim_visual_y | &kp LS(PAGE_UP)（物理 Shift は HID にそのまま伝わる） | &kp LS(HOME)（物理 Shift は HID にそのまま伝わる） | &none | macro_vim_visual_p | &none |
| Ctrl+ | &none | macro_vim_visual_exit | &kp LS(LC(RIGHT))（物理 Ctrl は HID にそのまま伝わる） | &kp LS(LC(RIGHT))（物理 Ctrl は HID にそのまま伝わる） | &kp LS(END)（物理 Ctrl は HID にそのまま伝わる） | &none | macro_vim_visual_y | &kp LS(PAGE_UP)（物理 Ctrl は HID にそのまま伝わる） | &kp LS(HOME)（物理 Ctrl は HID にそのまま伝わる） | &none | macro_vim_visual_p | &none |

#### Row 2 (home row)

| 操作 | (outer)<br>`&none` | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&macro_vim_visual_cut` | F<br>`&none` | G<br>`&mm_vim_visual_g` | (center L)<br>`&none` | (center R)<br>`&none` | H<br>`&kp LS(LEFT)` | J<br>`&kp LS(DOWN)` | K<br>`&kp LS(UP)` | L<br>`&kp LS(RIGHT)` | MINUS<br>`&kp RCTRL` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &kp LCTRL | &none | macro_vim_visual_cut | &none | mm_vim_visual_g[0] → td_vim_visual_g[0] → &none | &none | &none | &kp LS(LEFT) | &kp LS(DOWN) | &kp LS(UP) | &kp LS(RIGHT) | &kp RCTRL | &none |
| ダブルタップ | &none | &kp LCTRL（tap-dance 未定義、連打） | &none | macro_vim_visual_cut（連打） | &none | mm_vim_visual_g[0] → td_vim_visual_g[1] → &kp LS(LC(HOME)) | &none | &none | &kp LS(LEFT)（tap-dance 未定義、連打） | &kp LS(DOWN)（tap-dance 未定義、連打） | &kp LS(UP)（tap-dance 未定義、連打） | &kp LS(RIGHT)（tap-dance 未定義、連打） | &kp RCTRL（tap-dance 未定義、連打） | &none |
| Shift+ | &none | &kp LCTRL（物理 Shift は HID にそのまま伝わる） | &none | macro_vim_visual_cut | &none | mm_vim_visual_g[1] (Shift 検知) → &kp LS(LC(END)) | &none | &none | &kp LS(LEFT)（物理 Shift は HID にそのまま伝わる） | &kp LS(DOWN)（物理 Shift は HID にそのまま伝わる） | &kp LS(UP)（物理 Shift は HID にそのまま伝わる） | &kp LS(RIGHT)（物理 Shift は HID にそのまま伝わる） | &kp RCTRL（物理 Shift は HID にそのまま伝わる） | &none |
| Ctrl+ | &none | &kp LCTRL（物理 Ctrl は HID にそのまま伝わる） | &none | macro_vim_visual_cut | &none | mm_vim_visual_g[0] (Ctrl は本 mod-morph 検知外) → td_vim_visual_g[0] (tap-dance は mods 検知なし) → &none | &none | &none | &kp LS(LEFT)（物理 Ctrl は HID にそのまま伝わる） | &kp LS(DOWN)（物理 Ctrl は HID にそのまま伝わる） | &kp LS(UP)（物理 Ctrl は HID にそのまま伝わる） | &kp LS(RIGHT)（物理 Ctrl は HID にそのまま伝わる） | &kp RCTRL（物理 Ctrl は HID にそのまま伝わる） | &none |

#### Row 3 (Z row)

| 操作 | (outer)<br>`&none` | Z<br>`&kp LEFT_SHIFT` | X<br>`&macro_vim_visual_cut` | C<br>`&macro_vim_visual_cut` | V<br>`&macro_vim_visual_exit` | B<br>`&kp LS(LC(LEFT))` | (center L)<br>`&none` | (center R)<br>`&none` | N<br>`&kp F3` | M<br>`&none` | COMMA<br>`&none` | PERIOD<br>`&none` | SLASH<br>`&kp RIGHT_SHIFT` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &kp LEFT_SHIFT | macro_vim_visual_cut | macro_vim_visual_cut | macro_vim_visual_exit | &kp LS(LC(LEFT)) | &none | &none | &kp F3 | &none | &none | &none | &kp RIGHT_SHIFT | &none |
| ダブルタップ | &none | &kp LEFT_SHIFT（tap-dance 未定義、連打） | macro_vim_visual_cut（連打） | macro_vim_visual_cut（連打） | macro_vim_visual_exit（連打） | &kp LS(LC(LEFT))（tap-dance 未定義、連打） | &none | &none | &kp F3（tap-dance 未定義、連打） | &none | &none | &none | &kp RIGHT_SHIFT（tap-dance 未定義、連打） | &none |
| Shift+ | &none | &kp LEFT_SHIFT（物理 Shift は HID にそのまま伝わる） | macro_vim_visual_cut | macro_vim_visual_cut | macro_vim_visual_exit | &kp LS(LC(LEFT))（物理 Shift は HID にそのまま伝わる） | &none | &none | &kp F3（物理 Shift は HID にそのまま伝わる） | &none | &none | &none | &kp RIGHT_SHIFT（物理 Shift は HID にそのまま伝わる） | &none |
| Ctrl+ | &none | &kp LEFT_SHIFT（物理 Ctrl は HID にそのまま伝わる） | macro_vim_visual_cut | macro_vim_visual_cut | macro_vim_visual_exit | &kp LS(LC(LEFT))（物理 Ctrl は HID にそのまま伝わる） | &none | &none | &kp F3（物理 Ctrl は HID にそのまま伝わる） | &none | &none | &none | &kp RIGHT_SHIFT（物理 Ctrl は HID にそのまま伝わる） | &none |

#### Row 4 (thumb)

| 操作 | (outer)<br>`&none` | mo6 (outer)<br>`&none` | LEFT_WIN<br>`&none` | LEFT_ALT<br>`&none` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | (mo1 center)<br>`&macro_vim_visual_exit` | (mo2 center)<br>`&macro_vim_visual_exit` | lt1 ENTER<br>`&macro_vim_visual_exit` | (none)<br>`&none` | (none)<br>`&none` | mo6<br>`&none` | mo6 (outer)<br>`&none` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &none | &none | &none | &none | &none | macro_vim_visual_exit | macro_vim_visual_exit | macro_vim_visual_exit | &none | &none | &none | &none | &none |
| ダブルタップ | &none | &none | &none | &none | &none | &none | macro_vim_visual_exit（連打） | macro_vim_visual_exit（連打） | macro_vim_visual_exit（連打） | &none | &none | &none | &none | &none |
| Shift+ | &none | &none | &none | &none | &none | &none | macro_vim_visual_exit | macro_vim_visual_exit | macro_vim_visual_exit | &none | &none | &none | &none | &none |
| Ctrl+ | &none | &none | &none | &none | &none | &none | macro_vim_visual_exit | macro_vim_visual_exit | macro_vim_visual_exit | &none | &none | &none | &none | &none |

