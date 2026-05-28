# VIM_NORMAL_2 レイヤー キー割り当て一覧

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

| 操作 | (outer)<br>`&none` | Q<br>`&trans` | W<br>`&none` | E<br>`&trans` | R<br>`&mm_vim_shift_4` | T<br>`&trans` | Y<br>`&mm_vim_shift_6` | U<br>`&kp PAGE_UP` | I<br>`&trans` | O<br>`&none` | P<br>`&kp HOME` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | PAGE_UP 入力 | 下位レイヤーの同位置にフォールスルー | 何もしない | HOME 入力 | 何もしない |
| ダブルタップ | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | PAGE_UP 入力 × 2 | 下位レイヤーの同位置にフォールスルー | 何もしない | HOME 入力 × 2 | 何もしない |
| Shift+ | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | 下位レイヤーの同位置にフォールスルー | END 入力 | 下位レイヤーの同位置にフォールスルー | HOME 入力 | Shift + PAGE_UP（OS で合成） | 下位レイヤーの同位置にフォールスルー | 何もしない | Shift + HOME（OS で合成） | 何もしない |
| Ctrl+ | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | Ctrl + PAGE_UP（OS で合成） | 下位レイヤーの同位置にフォールスルー | 何もしない | Ctrl + HOME（OS で合成） | 何もしない |

### Row 2 (home row)

| 操作 | (outer)<br>`&none` | A<br>`&kp LCTRL` | S<br>`&trans` | D<br>`&kp PAGE_DOWN` | F<br>`&trans` | G<br>`&none` | (center L)<br>`&none` | (center R)<br>`&none` | H<br>`&trans` | J<br>`&trans` | K<br>`&trans` | L<br>`&trans` | MINUS<br>`&kp RCTRL` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | Left Ctrl 入力 | 下位レイヤーの同位置にフォールスルー | PAGE_DOWN 入力 | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | Right Ctrl 入力 | 何もしない |
| ダブルタップ | 何もしない | Left Ctrl 入力 × 2 | 下位レイヤーの同位置にフォールスルー | PAGE_DOWN 入力 × 2 | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | Right Ctrl 入力 × 2 | 何もしない |
| Shift+ | 何もしない | Shift + Left Ctrl（OS で合成） | 下位レイヤーの同位置にフォールスルー | Shift + PAGE_DOWN（OS で合成） | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | Shift + Right Ctrl（OS で合成） | 何もしない |
| Ctrl+ | 何もしない | Ctrl + Left Ctrl（OS で合成） | 下位レイヤーの同位置にフォールスルー | Ctrl + PAGE_DOWN（OS で合成） | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | Ctrl + Right Ctrl（OS で合成） | 何もしない |

### Row 3 (Z row)

| 操作 | (outer)<br>`&none` | Z<br>`&kp LEFT_SHIFT` | X<br>`&none` | C<br>`&none` | V<br>`&none` | B<br>`&none` | (center L)<br>`&none` | (center R)<br>`&none` | N<br>`&trans` | M<br>`&trans` | COMMA<br>`&trans` | PERIOD<br>`&trans` | SLASH<br>`&kp RIGHT_SHIFT` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | Left Shift 入力 | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | Right Shift 入力 | 何もしない |
| ダブルタップ | 何もしない | Left Shift 入力 × 2 | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | Right Shift 入力 × 2 | 何もしない |
| Shift+ | 何もしない | Shift + Left Shift（OS で合成） | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | Shift + Right Shift（OS で合成） | 何もしない |
| Ctrl+ | 何もしない | Ctrl + Left Shift（OS で合成） | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | Ctrl + Right Shift（OS で合成） | 何もしない |

### Row 4 (thumb)

| 操作 | (outer)<br>`&none` | mo6 (outer)<br>`&none` | LEFT_WIN<br>`&trans` | LEFT_ALT<br>`&trans` | lt2 SPACE<br>`&trans` | lt2 SPACE<br>`&none` | (mo1 center)<br>`&none` | (mo2 center)<br>`&none` | lt1 ENTER<br>`&none` | (none)<br>`&none` | (none)<br>`&none` | mo6<br>`&trans` | mo6 (outer)<br>`&none` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない |
| ダブルタップ | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない |
| Shift+ | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない |
| Ctrl+ | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない |

## 経路

### Row 0 (top wing)

| 操作 | (outer)<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| ダブルタップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| Shift+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| Ctrl+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |

### Row 1 (QWERTY 上段)

| 操作 | (outer)<br>`&none` | Q<br>`&trans` | W<br>`&none` | E<br>`&trans` | R<br>`&mm_vim_shift_4` | T<br>`&trans` | Y<br>`&mm_vim_shift_6` | U<br>`&kp PAGE_UP` | I<br>`&trans` | O<br>`&none` | P<br>`&kp HOME` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &trans | &none | &trans | mm_vim_shift_4[0] → &none | &trans | mm_vim_shift_6[0] → &none | &kp PAGE_UP | &trans | &none | &kp HOME | &none |
| ダブルタップ | &none | &trans | &none | &trans | mm_vim_shift_4[0] → &none | &trans | mm_vim_shift_6[0] → &none | &kp PAGE_UP（tap-dance 未定義、連打） | &trans | &none | &kp HOME（tap-dance 未定義、連打） | &none |
| Shift+ | &none | &trans | &none | &trans | mm_vim_shift_4[1] (Shift 検知) → &kp END | &trans | mm_vim_shift_6[1] (Shift 検知) → &kp HOME | &kp PAGE_UP（物理 Shift は HID にそのまま伝わる） | &trans | &none | &kp HOME（物理 Shift は HID にそのまま伝わる） | &none |
| Ctrl+ | &none | &trans | &none | &trans | mm_vim_shift_4[0] (Ctrl は本 mod-morph 検知外) → &none | &trans | mm_vim_shift_6[0] (Ctrl は本 mod-morph 検知外) → &none | &kp PAGE_UP（物理 Ctrl は HID にそのまま伝わる） | &trans | &none | &kp HOME（物理 Ctrl は HID にそのまま伝わる） | &none |

### Row 2 (home row)

| 操作 | (outer)<br>`&none` | A<br>`&kp LCTRL` | S<br>`&trans` | D<br>`&kp PAGE_DOWN` | F<br>`&trans` | G<br>`&none` | (center L)<br>`&none` | (center R)<br>`&none` | H<br>`&trans` | J<br>`&trans` | K<br>`&trans` | L<br>`&trans` | MINUS<br>`&kp RCTRL` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &kp LCTRL | &trans | &kp PAGE_DOWN | &trans | &none | &none | &none | &trans | &trans | &trans | &trans | &kp RCTRL | &none |
| ダブルタップ | &none | &kp LCTRL（tap-dance 未定義、連打） | &trans | &kp PAGE_DOWN（tap-dance 未定義、連打） | &trans | &none | &none | &none | &trans | &trans | &trans | &trans | &kp RCTRL（tap-dance 未定義、連打） | &none |
| Shift+ | &none | &kp LCTRL（物理 Shift は HID にそのまま伝わる） | &trans | &kp PAGE_DOWN（物理 Shift は HID にそのまま伝わる） | &trans | &none | &none | &none | &trans | &trans | &trans | &trans | &kp RCTRL（物理 Shift は HID にそのまま伝わる） | &none |
| Ctrl+ | &none | &kp LCTRL（物理 Ctrl は HID にそのまま伝わる） | &trans | &kp PAGE_DOWN（物理 Ctrl は HID にそのまま伝わる） | &trans | &none | &none | &none | &trans | &trans | &trans | &trans | &kp RCTRL（物理 Ctrl は HID にそのまま伝わる） | &none |

### Row 3 (Z row)

| 操作 | (outer)<br>`&none` | Z<br>`&kp LEFT_SHIFT` | X<br>`&none` | C<br>`&none` | V<br>`&none` | B<br>`&none` | (center L)<br>`&none` | (center R)<br>`&none` | N<br>`&trans` | M<br>`&trans` | COMMA<br>`&trans` | PERIOD<br>`&trans` | SLASH<br>`&kp RIGHT_SHIFT` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &kp LEFT_SHIFT | &none | &none | &none | &none | &none | &none | &trans | &trans | &trans | &trans | &kp RIGHT_SHIFT | &none |
| ダブルタップ | &none | &kp LEFT_SHIFT（tap-dance 未定義、連打） | &none | &none | &none | &none | &none | &none | &trans | &trans | &trans | &trans | &kp RIGHT_SHIFT（tap-dance 未定義、連打） | &none |
| Shift+ | &none | &kp LEFT_SHIFT（物理 Shift は HID にそのまま伝わる） | &none | &none | &none | &none | &none | &none | &trans | &trans | &trans | &trans | &kp RIGHT_SHIFT（物理 Shift は HID にそのまま伝わる） | &none |
| Ctrl+ | &none | &kp LEFT_SHIFT（物理 Ctrl は HID にそのまま伝わる） | &none | &none | &none | &none | &none | &none | &trans | &trans | &trans | &trans | &kp RIGHT_SHIFT（物理 Ctrl は HID にそのまま伝わる） | &none |

### Row 4 (thumb)

| 操作 | (outer)<br>`&none` | mo6 (outer)<br>`&none` | LEFT_WIN<br>`&trans` | LEFT_ALT<br>`&trans` | lt2 SPACE<br>`&trans` | lt2 SPACE<br>`&none` | (mo1 center)<br>`&none` | (mo2 center)<br>`&none` | lt1 ENTER<br>`&none` | (none)<br>`&none` | (none)<br>`&none` | mo6<br>`&trans` | mo6 (outer)<br>`&none` | (outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &none | &trans | &trans | &trans | &none | &none | &none | &none | &none | &none | &trans | &none | &none |
| ダブルタップ | &none | &none | &trans | &trans | &trans | &none | &none | &none | &none | &none | &none | &trans | &none | &none |
| Shift+ | &none | &none | &trans | &trans | &trans | &none | &none | &none | &none | &none | &none | &trans | &none | &none |
| Ctrl+ | &none | &none | &trans | &trans | &trans | &none | &none | &none | &none | &none | &none | &trans | &none | &none |

