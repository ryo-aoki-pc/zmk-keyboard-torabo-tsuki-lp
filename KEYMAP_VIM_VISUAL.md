# VIM_VISUAL レイヤー キー割り当て一覧

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

| 操作 | (outer)<br>`&none` | Q<br>`&macro_vim_visual_exit` | W<br>`&kp LS(LC(RIGHT))` | E<br>`&kp LS(LC(RIGHT))` | R<br>`&kp LS(END)` | T<br>`&none` | Y<br>`&macro_vim_visual_y` | U<br>`&kp LS(PAGE_UP)` | I<br>`&kp LS(HOME)` | O<br>`&none` | P<br>`&macro_vim_visual_p` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ | Shift+Ctrl+→ 入力 | Shift+Ctrl+→ 入力 | Shift+END 入力 | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+C → → → レイヤー 0 へ | Shift+PAGE_UP 入力 | Shift+HOME 入力 | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+V → レイヤー 0 へ | 何もしない |
| ダブルタップ | 何もしない | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（2 回実行） | Shift+Ctrl+→ 入力 × 2 | Shift+Ctrl+→ 入力 × 2 | Shift+END 入力 × 2 | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+C → → → レイヤー 0 へ（2 回実行） | Shift+PAGE_UP 入力 × 2 | Shift+HOME 入力 × 2 | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+V → レイヤー 0 へ（2 回実行） | 何もしない |
| Shift+ | 何もしない | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（Shift 物理保持で実行） | Shift + Shift+Ctrl+→（OS で合成） | Shift + Shift+Ctrl+→（OS で合成） | Shift + Shift+END（OS で合成） | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+C → → → レイヤー 0 へ（Shift 物理保持で実行） | Shift + Shift+PAGE_UP（OS で合成） | Shift + Shift+HOME（OS で合成） | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+V → レイヤー 0 へ（Shift 物理保持で実行） | 何もしない |
| Ctrl+ | 何もしない | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（Ctrl 物理保持で実行） | Ctrl + Shift+Ctrl+→（OS で合成） | Ctrl + Shift+Ctrl+→（OS で合成） | Ctrl + Shift+END（OS で合成） | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+C → → → レイヤー 0 へ（Ctrl 物理保持で実行） | Ctrl + Shift+PAGE_UP（OS で合成） | Ctrl + Shift+HOME（OS で合成） | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+V → レイヤー 0 へ（Ctrl 物理保持で実行） | 何もしない |

### Row 2 (home row)

| 操作 | (outer)<br>`&none` | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&macro_vim_visual_cut` | F<br>`&none` | G<br>`&mm_vim_visual_g` | (center L)<br>`&none` | (center R)<br>`&none` | H<br>`&kp LS(LEFT)` | J<br>`&kp LS(DOWN)` | K<br>`&kp LS(UP)` | L<br>`&kp LS(RIGHT)` | MINUS<br>`&kp RCTRL` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | Left Ctrl 入力 | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ | 何もしない | 何もしない | 何もしない | 何もしない | Shift+← 入力 | Shift+↓ 入力 | Shift+UP 入力 | Shift+→ 入力 | Right Ctrl 入力 | 何もしない |
| ダブルタップ | 何もしない | Left Ctrl 入力 × 2 | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ（2 回実行） | 何もしない | Shift+Ctrl+HOME 入力 | 何もしない | 何もしない | Shift+← 入力 × 2 | Shift+↓ 入力 × 2 | Shift+UP 入力 × 2 | Shift+→ 入力 × 2 | Right Ctrl 入力 × 2 | 何もしない |
| Shift+ | 何もしない | Shift + Left Ctrl（OS で合成） | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ（Shift 物理保持で実行） | 何もしない | Shift+Ctrl+END 入力 | 何もしない | 何もしない | Shift + Shift+←（OS で合成） | Shift + Shift+↓（OS で合成） | Shift + Shift+UP（OS で合成） | Shift + Shift+→（OS で合成） | Shift + Right Ctrl（OS で合成） | 何もしない |
| Ctrl+ | 何もしない | Ctrl + Left Ctrl（OS で合成） | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ（Ctrl 物理保持で実行） | 何もしない | 何もしない | 何もしない | 何もしない | Ctrl + Shift+←（OS で合成） | Ctrl + Shift+↓（OS で合成） | Ctrl + Shift+UP（OS で合成） | Ctrl + Shift+→（OS で合成） | Ctrl + Right Ctrl（OS で合成） | 何もしない |

### Row 3 (Z row)

| 操作 | (outer)<br>`&none` | Z<br>`&kp LEFT_SHIFT` | X<br>`&macro_vim_visual_cut` | C<br>`&macro_vim_visual_cut` | V<br>`&macro_vim_visual_exit` | B<br>`&kp LS(LC(LEFT))` | (center L)<br>`&none` | (center R)<br>`&none` | N<br>`&kp F3` | M<br>`&none` | COMMA<br>`&none` | PERIOD<br>`&none` | SLASH<br>`&kp RIGHT_SHIFT` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | Left Shift 入力 | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ | Shift+Ctrl+← 入力 | 何もしない | 何もしない | F3 入力 | 何もしない | 何もしない | 何もしない | Right Shift 入力 | 何もしない |
| ダブルタップ | 何もしない | Left Shift 入力 × 2 | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ（2 回実行） | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ（2 回実行） | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（2 回実行） | Shift+Ctrl+← 入力 × 2 | 何もしない | 何もしない | F3 入力 × 2 | 何もしない | 何もしない | 何もしない | Right Shift 入力 × 2 | 何もしない |
| Shift+ | 何もしない | Shift + Left Shift（OS で合成） | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ（Shift 物理保持で実行） | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ（Shift 物理保持で実行） | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（Shift 物理保持で実行） | Shift + Shift+Ctrl+←（OS で合成） | 何もしない | 何もしない | Shift + F3（OS で合成） | 何もしない | 何もしない | 何もしない | Shift + Right Shift（OS で合成） | 何もしない |
| Ctrl+ | 何もしない | Ctrl + Left Shift（OS で合成） | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ（Ctrl 物理保持で実行） | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ（Ctrl 物理保持で実行） | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（Ctrl 物理保持で実行） | Ctrl + Shift+Ctrl+←（OS で合成） | 何もしない | 何もしない | Ctrl + F3（OS で合成） | 何もしない | 何もしない | 何もしない | Ctrl + Right Shift（OS で合成） | 何もしない |

### Row 4 (thumb)

| 操作 | (outer)<br>`&none` | mo6 (outer)<br>`&none` | LEFT_WIN<br>`&none` | LEFT_ALT<br>`&none` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | (mo1 center)<br>`&macro_vim_visual_exit` | (mo2 center)<br>`&macro_vim_visual_exit` | lt1 ENTER<br>`&macro_vim_visual_exit` | (none)<br>`&none` | (none)<br>`&none` | mo6<br>`&none` | mo6 (outer)<br>`&none` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない |
| ダブルタップ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（2 回実行） | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（2 回実行） | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（2 回実行） | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない |
| Shift+ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（Shift 物理保持で実行） | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（Shift 物理保持で実行） | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（Shift 物理保持で実行） | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない |
| Ctrl+ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（Ctrl 物理保持で実行） | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（Ctrl 物理保持で実行） | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（Ctrl 物理保持で実行） | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない |

## 経路

### Row 0 (top wing)

| 操作 | (outer)<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| ダブルタップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| Shift+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| Ctrl+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |

### Row 1 (QWERTY 上段)

| 操作 | (outer)<br>`&none` | Q<br>`&macro_vim_visual_exit` | W<br>`&kp LS(LC(RIGHT))` | E<br>`&kp LS(LC(RIGHT))` | R<br>`&kp LS(END)` | T<br>`&none` | Y<br>`&macro_vim_visual_y` | U<br>`&kp LS(PAGE_UP)` | I<br>`&kp LS(HOME)` | O<br>`&none` | P<br>`&macro_vim_visual_p` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | macro_vim_visual_exit | &kp LS(LC(RIGHT)) | &kp LS(LC(RIGHT)) | &kp LS(END) | &none | macro_vim_visual_y | &kp LS(PAGE_UP) | &kp LS(HOME) | &none | macro_vim_visual_p | &none |
| ダブルタップ | &none | macro_vim_visual_exit（連打） | &kp LS(LC(RIGHT))（tap-dance 未定義、連打） | &kp LS(LC(RIGHT))（tap-dance 未定義、連打） | &kp LS(END)（tap-dance 未定義、連打） | &none | macro_vim_visual_y（連打） | &kp LS(PAGE_UP)（tap-dance 未定義、連打） | &kp LS(HOME)（tap-dance 未定義、連打） | &none | macro_vim_visual_p（連打） | &none |
| Shift+ | &none | macro_vim_visual_exit | &kp LS(LC(RIGHT))（物理 Shift は HID にそのまま伝わる） | &kp LS(LC(RIGHT))（物理 Shift は HID にそのまま伝わる） | &kp LS(END)（物理 Shift は HID にそのまま伝わる） | &none | macro_vim_visual_y | &kp LS(PAGE_UP)（物理 Shift は HID にそのまま伝わる） | &kp LS(HOME)（物理 Shift は HID にそのまま伝わる） | &none | macro_vim_visual_p | &none |
| Ctrl+ | &none | macro_vim_visual_exit | &kp LS(LC(RIGHT))（物理 Ctrl は HID にそのまま伝わる） | &kp LS(LC(RIGHT))（物理 Ctrl は HID にそのまま伝わる） | &kp LS(END)（物理 Ctrl は HID にそのまま伝わる） | &none | macro_vim_visual_y | &kp LS(PAGE_UP)（物理 Ctrl は HID にそのまま伝わる） | &kp LS(HOME)（物理 Ctrl は HID にそのまま伝わる） | &none | macro_vim_visual_p | &none |

### Row 2 (home row)

| 操作 | (outer)<br>`&none` | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&macro_vim_visual_cut` | F<br>`&none` | G<br>`&mm_vim_visual_g` | (center L)<br>`&none` | (center R)<br>`&none` | H<br>`&kp LS(LEFT)` | J<br>`&kp LS(DOWN)` | K<br>`&kp LS(UP)` | L<br>`&kp LS(RIGHT)` | MINUS<br>`&kp RCTRL` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &kp LCTRL | &none | macro_vim_visual_cut | &none | mm_vim_visual_g[0] → td_vim_visual_g[0] → &none | &none | &none | &kp LS(LEFT) | &kp LS(DOWN) | &kp LS(UP) | &kp LS(RIGHT) | &kp RCTRL | &none |
| ダブルタップ | &none | &kp LCTRL（tap-dance 未定義、連打） | &none | macro_vim_visual_cut（連打） | &none | mm_vim_visual_g[0] → td_vim_visual_g[1] → &kp LS(LC(HOME)) | &none | &none | &kp LS(LEFT)（tap-dance 未定義、連打） | &kp LS(DOWN)（tap-dance 未定義、連打） | &kp LS(UP)（tap-dance 未定義、連打） | &kp LS(RIGHT)（tap-dance 未定義、連打） | &kp RCTRL（tap-dance 未定義、連打） | &none |
| Shift+ | &none | &kp LCTRL（物理 Shift は HID にそのまま伝わる） | &none | macro_vim_visual_cut | &none | mm_vim_visual_g[1] (Shift 検知) → &kp LS(LC(END)) | &none | &none | &kp LS(LEFT)（物理 Shift は HID にそのまま伝わる） | &kp LS(DOWN)（物理 Shift は HID にそのまま伝わる） | &kp LS(UP)（物理 Shift は HID にそのまま伝わる） | &kp LS(RIGHT)（物理 Shift は HID にそのまま伝わる） | &kp RCTRL（物理 Shift は HID にそのまま伝わる） | &none |
| Ctrl+ | &none | &kp LCTRL（物理 Ctrl は HID にそのまま伝わる） | &none | macro_vim_visual_cut | &none | mm_vim_visual_g[0] (Ctrl は本 mod-morph 検知外) → td_vim_visual_g[0] (tap-dance は mods 検知なし) → &none | &none | &none | &kp LS(LEFT)（物理 Ctrl は HID にそのまま伝わる） | &kp LS(DOWN)（物理 Ctrl は HID にそのまま伝わる） | &kp LS(UP)（物理 Ctrl は HID にそのまま伝わる） | &kp LS(RIGHT)（物理 Ctrl は HID にそのまま伝わる） | &kp RCTRL（物理 Ctrl は HID にそのまま伝わる） | &none |

### Row 3 (Z row)

| 操作 | (outer)<br>`&none` | Z<br>`&kp LEFT_SHIFT` | X<br>`&macro_vim_visual_cut` | C<br>`&macro_vim_visual_cut` | V<br>`&macro_vim_visual_exit` | B<br>`&kp LS(LC(LEFT))` | (center L)<br>`&none` | (center R)<br>`&none` | N<br>`&kp F3` | M<br>`&none` | COMMA<br>`&none` | PERIOD<br>`&none` | SLASH<br>`&kp RIGHT_SHIFT` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &kp LEFT_SHIFT | macro_vim_visual_cut | macro_vim_visual_cut | macro_vim_visual_exit | &kp LS(LC(LEFT)) | &none | &none | &kp F3 | &none | &none | &none | &kp RIGHT_SHIFT | &none |
| ダブルタップ | &none | &kp LEFT_SHIFT（tap-dance 未定義、連打） | macro_vim_visual_cut（連打） | macro_vim_visual_cut（連打） | macro_vim_visual_exit（連打） | &kp LS(LC(LEFT))（tap-dance 未定義、連打） | &none | &none | &kp F3（tap-dance 未定義、連打） | &none | &none | &none | &kp RIGHT_SHIFT（tap-dance 未定義、連打） | &none |
| Shift+ | &none | &kp LEFT_SHIFT（物理 Shift は HID にそのまま伝わる） | macro_vim_visual_cut | macro_vim_visual_cut | macro_vim_visual_exit | &kp LS(LC(LEFT))（物理 Shift は HID にそのまま伝わる） | &none | &none | &kp F3（物理 Shift は HID にそのまま伝わる） | &none | &none | &none | &kp RIGHT_SHIFT（物理 Shift は HID にそのまま伝わる） | &none |
| Ctrl+ | &none | &kp LEFT_SHIFT（物理 Ctrl は HID にそのまま伝わる） | macro_vim_visual_cut | macro_vim_visual_cut | macro_vim_visual_exit | &kp LS(LC(LEFT))（物理 Ctrl は HID にそのまま伝わる） | &none | &none | &kp F3（物理 Ctrl は HID にそのまま伝わる） | &none | &none | &none | &kp RIGHT_SHIFT（物理 Ctrl は HID にそのまま伝わる） | &none |

### Row 4 (thumb)

| 操作 | (outer)<br>`&none` | mo6 (outer)<br>`&none` | LEFT_WIN<br>`&none` | LEFT_ALT<br>`&none` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | (mo1 center)<br>`&macro_vim_visual_exit` | (mo2 center)<br>`&macro_vim_visual_exit` | lt1 ENTER<br>`&macro_vim_visual_exit` | (none)<br>`&none` | (none)<br>`&none` | mo6<br>`&none` | mo6 (outer)<br>`&none` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &none | &none | &none | &none | &none | macro_vim_visual_exit | macro_vim_visual_exit | macro_vim_visual_exit | &none | &none | &none | &none | &none |
| ダブルタップ | &none | &none | &none | &none | &none | &none | macro_vim_visual_exit（連打） | macro_vim_visual_exit（連打） | macro_vim_visual_exit（連打） | &none | &none | &none | &none | &none |
| Shift+ | &none | &none | &none | &none | &none | &none | macro_vim_visual_exit | macro_vim_visual_exit | macro_vim_visual_exit | &none | &none | &none | &none | &none |
| Ctrl+ | &none | &none | &none | &none | &none | &none | macro_vim_visual_exit | macro_vim_visual_exit | macro_vim_visual_exit | &none | &none | &none | &none | &none |

