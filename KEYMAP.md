# キー割り当て一覧

※ 9 個のレイヤーのキー割り当てを 1 ファイルに集約。各レイヤー 66 バインディング位置を「動作」セクションでまとめてから「経路」セクションに進む。

- 各 row セクション行に「キーラベル」と「バインディング (`&...`)」の 2 段表示でキー位置を示す。
- 各表の左端 1 列が「操作」（単発タップ / ダブルタップ / Shift+ / Ctrl+）または「■ Row N」見出し。

## 動作

### DEFAULT レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 0 (top wing) | (outer)<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | (outer)<br>`&none` |  |  |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ダブルタップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Shift+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ctrl+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ■ Row 1 (QWERTY 上段) | (outer)<br>`&none` | Q<br>`&kp Q` | W<br>`&kp W` | E<br>`&kp E` | R<br>`&kp R` | T<br>`&kp T` | Y<br>`&kp Y` | U<br>`&kp U` | I<br>`&kp I` | O<br>`&kp O` | P<br>`&kp P` | (outer)<br>`&none` |  |  |
| 単発タップ |  | Q 入力 | W 入力 | E 入力 | R 入力 | T 入力 | Y 入力 | U 入力 | I 入力 | O 入力 | P 入力 |  |  |  |
| ダブルタップ |  | Q 入力 × 2 | W 入力 × 2 | E 入力 × 2 | R 入力 × 2 | T 入力 × 2 | Y 入力 × 2 | U 入力 × 2 | I 入力 × 2 | O 入力 × 2 | P 入力 × 2 |  |  |  |
| Shift+ |  | Shift + Q（OS で合成） | Shift + W（OS で合成） | Shift + E（OS で合成） | Shift + R（OS で合成） | Shift + T（OS で合成） | Shift + Y（OS で合成） | Shift + U（OS で合成） | Shift + I（OS で合成） | Shift + O（OS で合成） | Shift + P（OS で合成） |  |  |  |
| Ctrl+ |  | Ctrl + Q（OS で合成） | Ctrl + W（OS で合成） | Ctrl + E（OS で合成） | Ctrl + R（OS で合成） | Ctrl + T（OS で合成） | Ctrl + Y（OS で合成） | Ctrl + U（OS で合成） | Ctrl + I（OS で合成） | Ctrl + O（OS で合成） | Ctrl + P（OS で合成） |  |  |  |
| ■ Row 2 (home row) | (outer)<br>`&none` | A<br>`&mt LEFT_CONTROL A` | S<br>`&kp S` | D<br>`&kp D` | F<br>`&kp F` | G<br>`&kp G` | (center L)<br>`&none` | (center R)<br>`&none` | H<br>`&kp H` | J<br>`&kp J` | K<br>`&kp K` | L<br>`&kp L` | MINUS<br>`&mt RCTRL MINUS` | (outer)<br>`&none` |
| 単発タップ |  | A 入力（タップ） | S 入力 | D 入力 | F 入力 | G 入力 |  |  | H 入力 | J 入力 | K 入力 | L 入力 | MINUS 入力（タップ） |  |
| ダブルタップ |  | A 入力 × 2 | S 入力 × 2 | D 入力 × 2 | F 入力 × 2 | G 入力 × 2 |  |  | H 入力 × 2 | J 入力 × 2 | K 入力 × 2 | L 入力 × 2 | MINUS 入力 × 2 |  |
| Shift+ |  | Shift + A（または Left Ctrl ホールドで修飾） | Shift + S（OS で合成） | Shift + D（OS で合成） | Shift + F（OS で合成） | Shift + G（OS で合成） |  |  | Shift + H（OS で合成） | Shift + J（OS で合成） | Shift + K（OS で合成） | Shift + L（OS で合成） | Shift + MINUS（または Right Ctrl ホールドで修飾） |  |
| Ctrl+ |  | Ctrl + A | Ctrl + S（OS で合成） | Ctrl + D（OS で合成） | Ctrl + F（OS で合成） | Ctrl + G（OS で合成） |  |  | Ctrl + H（OS で合成） | Ctrl + J（OS で合成） | Ctrl + K（OS で合成） | Ctrl + L（OS で合成） | Ctrl + MINUS |  |
| ■ Row 3 (Z row) | (outer)<br>`&none` | Z<br>`&mt LEFT_SHIFT Z` | X<br>`&kp X` | C<br>`&kp C` | V<br>`&kp V` | B<br>`&kp B` | (center L)<br>`&mo 7` | (center R)<br>`&mo 7` | N<br>`&kp N` | M<br>`&kp M` | COMMA<br>`&kp COMMA` | PERIOD<br>`&kp PERIOD` | SLASH<br>`&mt RIGHT_SHIFT SLASH` | (outer)<br>`&none` |
| 単発タップ |  | Z 入力（タップ） | X 入力 | C 入力 | V 入力 | B 入力 | レイヤー 7 を momentary（押下中のみ）有効化 | レイヤー 7 を momentary（押下中のみ）有効化 | N 入力 | M 入力 | COMMA 入力 | PERIOD 入力 | SLASH 入力（タップ） |  |
| ダブルタップ |  | Z 入力 × 2 | X 入力 × 2 | C 入力 × 2 | V 入力 × 2 | B 入力 × 2 | レイヤー 7 を momentary（押下中のみ）有効化 | レイヤー 7 を momentary（押下中のみ）有効化 | N 入力 × 2 | M 入力 × 2 | COMMA 入力 × 2 | PERIOD 入力 × 2 | SLASH 入力 × 2 |  |
| Shift+ |  | Shift + Z（または Left Shift ホールドで修飾） | Shift + X（OS で合成） | Shift + C（OS で合成） | Shift + V（OS で合成） | Shift + B（OS で合成） | レイヤー 7 を momentary（押下中のみ）有効化 | レイヤー 7 を momentary（押下中のみ）有効化 | Shift + N（OS で合成） | Shift + M（OS で合成） | Shift + COMMA（OS で合成） | Shift + PERIOD（OS で合成） | Shift + SLASH（または Right Shift ホールドで修飾） |  |
| Ctrl+ |  | Ctrl + Z | Ctrl + X（OS で合成） | Ctrl + C（OS で合成） | Ctrl + V（OS で合成） | Ctrl + B（OS で合成） | レイヤー 7 を momentary（押下中のみ）有効化 | レイヤー 7 を momentary（押下中のみ）有効化 | Ctrl + N（OS で合成） | Ctrl + M（OS で合成） | Ctrl + COMMA（OS で合成） | Ctrl + PERIOD（OS で合成） | Ctrl + SLASH |  |
| ■ Row 4 (thumb) | (outer)<br>`&none` | mo6 (outer)<br>`&mo 6` | LEFT_WIN<br>`&kp LEFT_WIN` | LEFT_ALT<br>`&kp LEFT_ALT` | lt2 SPACE<br>`&lt 2 SPACE` | lt2 SPACE<br>`&lt 2 SPACE` | (mo1 center)<br>`&mo 1` | (mo2 center)<br>`&mo 2` | lt1 ENTER<br>`&lt 1 ENTER` | (none)<br>`&none` | (none)<br>`&none` | mo6<br>`&mo 6` | mo6 (outer)<br>`&mo 6` | (outer)<br>`&none` |
| 単発タップ |  | レイヤー 6 を momentary（押下中のみ）有効化 | Left Win 入力 | Left Alt 入力 | SPACE 入力（タップ） | SPACE 入力（タップ） | レイヤー 1 を momentary（押下中のみ）有効化 | レイヤー 2 を momentary（押下中のみ）有効化 | ENTER 入力（タップ） |  |  | レイヤー 6 を momentary（押下中のみ）有効化 | レイヤー 6 を momentary（押下中のみ）有効化 |  |
| ダブルタップ |  | レイヤー 6 を momentary（押下中のみ）有効化 | Left Win 入力 × 2 | Left Alt 入力 × 2 | SPACE 入力 × 2 | SPACE 入力 × 2 | レイヤー 1 を momentary（押下中のみ）有効化 | レイヤー 2 を momentary（押下中のみ）有効化 | ENTER 入力 × 2 |  |  | レイヤー 6 を momentary（押下中のみ）有効化 | レイヤー 6 を momentary（押下中のみ）有効化 |  |
| Shift+ |  | レイヤー 6 を momentary（押下中のみ）有効化 | Shift + Left Win（OS で合成） | Shift + Left Alt（OS で合成） | Shift + SPACE（ホールドでレイヤー 2） | Shift + SPACE（ホールドでレイヤー 2） | レイヤー 1 を momentary（押下中のみ）有効化 | レイヤー 2 を momentary（押下中のみ）有効化 | Shift + ENTER（ホールドでレイヤー 1） |  |  | レイヤー 6 を momentary（押下中のみ）有効化 | レイヤー 6 を momentary（押下中のみ）有効化 |  |
| Ctrl+ |  | レイヤー 6 を momentary（押下中のみ）有効化 | Ctrl + Left Win（OS で合成） | Ctrl + Left Alt（OS で合成） | Ctrl + SPACE（ホールドでレイヤー 2） | Ctrl + SPACE（ホールドでレイヤー 2） | レイヤー 1 を momentary（押下中のみ）有効化 | レイヤー 2 を momentary（押下中のみ）有効化 | Ctrl + ENTER（ホールドでレイヤー 1） |  |  | レイヤー 6 を momentary（押下中のみ）有効化 | レイヤー 6 を momentary（押下中のみ）有効化 |  |

### SYMBOL レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 0 (top wing) | (outer)<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | (outer)<br>`&none` |  |  |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ダブルタップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Shift+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ctrl+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ■ Row 1 (QWERTY 上段) | (outer)<br>`&none` | Q<br>`&kp N1` | W<br>`&kp N2` | E<br>`&kp N3` | R<br>`&kp N4` | T<br>`&kp N5` | Y<br>`&kp N6` | U<br>`&kp N7` | I<br>`&kp N8` | O<br>`&kp N9` | P<br>`&kp N0` | (outer)<br>`&none` |  |  |
| 単発タップ |  | N1 入力 | N2 入力 | N3 入力 | N4 入力 | N5 入力 | N6 入力 | N7 入力 | N8 入力 | N9 入力 | N0 入力 |  |  |  |
| ダブルタップ |  | N1 入力 × 2 | N2 入力 × 2 | N3 入力 × 2 | N4 入力 × 2 | N5 入力 × 2 | N6 入力 × 2 | N7 入力 × 2 | N8 入力 × 2 | N9 入力 × 2 | N0 入力 × 2 |  |  |  |
| Shift+ |  | Shift + N1（OS で合成） | Shift + N2（OS で合成） | Shift + N3（OS で合成） | Shift + N4（OS で合成） | Shift + N5（OS で合成） | Shift + N6（OS で合成） | Shift + N7（OS で合成） | Shift + N8（OS で合成） | Shift + N9（OS で合成） | Shift + N0（OS で合成） |  |  |  |
| Ctrl+ |  | Ctrl + N1（OS で合成） | Ctrl + N2（OS で合成） | Ctrl + N3（OS で合成） | Ctrl + N4（OS で合成） | Ctrl + N5（OS で合成） | Ctrl + N6（OS で合成） | Ctrl + N7（OS で合成） | Ctrl + N8（OS で合成） | Ctrl + N9（OS で合成） | Ctrl + N0（OS で合成） |  |  |  |
| ■ Row 2 (home row) | (outer)<br>`&none` | A<br>`&mt LCTRL TAB` | S<br>`&kp GRAVE` | D<br>`&kp LEFT_BRACKET` | F<br>`&kp RIGHT_BRACKET` | G<br>`&kp DELETE` | (center L)<br>`&none` | (center R)<br>`&none` | H<br>`&kp BACKSPACE` | J<br>`&kp SEMICOLON` | K<br>`&kp SINGLE_QUOTE` | L<br>`&kp BACKSLASH` | MINUS<br>`&trans` | (outer)<br>`&none` |
| 単発タップ |  | TAB 入力（タップ） | GRAVE 入力 | LEFT_BRACKET 入力 | RIGHT_BRACKET 入力 | DELETE 入力 |  |  | BACKSPACE 入力 | SEMICOLON 入力 | SINGLE_QUOTE 入力 | BACKSLASH 入力 | ▽ |  |
| ダブルタップ |  | TAB 入力 × 2 | GRAVE 入力 × 2 | LEFT_BRACKET 入力 × 2 | RIGHT_BRACKET 入力 × 2 | DELETE 入力 × 2 |  |  | BACKSPACE 入力 × 2 | SEMICOLON 入力 × 2 | SINGLE_QUOTE 入力 × 2 | BACKSLASH 入力 × 2 | ▽ |  |
| Shift+ |  | Shift + TAB（または Left Ctrl ホールドで修飾） | Shift + GRAVE（OS で合成） | Shift + LEFT_BRACKET（OS で合成） | Shift + RIGHT_BRACKET（OS で合成） | Shift + DELETE（OS で合成） |  |  | Shift + BACKSPACE（OS で合成） | Shift + SEMICOLON（OS で合成） | Shift + SINGLE_QUOTE（OS で合成） | Shift + BACKSLASH（OS で合成） | ▽ |  |
| Ctrl+ |  | Ctrl + TAB | Ctrl + GRAVE（OS で合成） | Ctrl + LEFT_BRACKET（OS で合成） | Ctrl + RIGHT_BRACKET（OS で合成） | Ctrl + DELETE（OS で合成） |  |  | Ctrl + BACKSPACE（OS で合成） | Ctrl + SEMICOLON（OS で合成） | Ctrl + SINGLE_QUOTE（OS で合成） | Ctrl + BACKSLASH（OS で合成） | ▽ |  |
| ■ Row 3 (Z row) | (outer)<br>`&none` | Z<br>`&mt LEFT_SHIFT ESCAPE` | X<br>`&none` | C<br>`&none` | V<br>`&none` | B<br>`&none` | (center L)<br>`&none` | (center R)<br>`&none` | N<br>`&none` | M<br>`&kp EQUAL` | COMMA<br>`&trans` | PERIOD<br>`&trans` | SLASH<br>`&trans` | (outer)<br>`&none` |
| 単発タップ |  | ESC 入力（タップ） |  |  |  |  |  |  |  | EQUAL 入力 | ▽ | ▽ | ▽ |  |
| ダブルタップ |  | ESC 入力 × 2 |  |  |  |  |  |  |  | EQUAL 入力 × 2 | ▽ | ▽ | ▽ |  |
| Shift+ |  | Shift + ESC（または Left Shift ホールドで修飾） |  |  |  |  |  |  |  | Shift + EQUAL（OS で合成） | ▽ | ▽ | ▽ |  |
| Ctrl+ |  | Ctrl + ESC |  |  |  |  |  |  |  | Ctrl + EQUAL（OS で合成） | ▽ | ▽ | ▽ |  |
| ■ Row 4 (thumb) | (outer)<br>`&none` | mo6 (outer)<br>`&none` | LEFT_WIN<br>`&trans` | LEFT_ALT<br>`&trans` | lt2 SPACE<br>`&lt 3 SPACE` | lt2 SPACE<br>`&lt 3 SPACE` | (mo1 center)<br>`&none` | (mo2 center)<br>`&mo 3` | lt1 ENTER<br>`&none` | (none)<br>`&none` | (none)<br>`&none` | mo6<br>`&trans` | mo6 (outer)<br>`&none` | (outer)<br>`&none` |
| 単発タップ |  |  | ▽ | ▽ | SPACE 入力（タップ） | SPACE 入力（タップ） |  | レイヤー 3 を momentary（押下中のみ）有効化 |  |  |  | ▽ |  |  |
| ダブルタップ |  |  | ▽ | ▽ | SPACE 入力 × 2 | SPACE 入力 × 2 |  | レイヤー 3 を momentary（押下中のみ）有効化 |  |  |  | ▽ |  |  |
| Shift+ |  |  | ▽ | ▽ | Shift + SPACE（ホールドでレイヤー 3） | Shift + SPACE（ホールドでレイヤー 3） |  | レイヤー 3 を momentary（押下中のみ）有効化 |  |  |  | ▽ |  |  |
| Ctrl+ |  |  | ▽ | ▽ | Ctrl + SPACE（ホールドでレイヤー 3） | Ctrl + SPACE（ホールドでレイヤー 3） |  | レイヤー 3 を momentary（押下中のみ）有効化 |  |  |  | ▽ |  |  |

### VIM_NORMAL_1 レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 0 (top wing) | (outer)<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | (outer)<br>`&none` |  |  |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ダブルタップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Shift+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ctrl+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ■ Row 1 (QWERTY 上段) | (outer)<br>`&none` | Q<br>`&mm_vim_q` | W<br>`&mm_vim_w` | E<br>`&kp LC(RIGHT)` | R<br>`&mm_vim_ctrl_r` | T<br>`&none` | Y<br>`&mm_vim_shift_y` | U<br>`&mm_vim_ctrl_u` | I<br>`&none` | O<br>`&mm_vim_shift_o` | P<br>`&kp LC(V)` | (outer)<br>`&none` |  |  |
| 単発タップ |  | ESC 入力 | Ctrl+→ 入力 | Ctrl+→ 入力 |  |  | Ctrl+C 入力 | Ctrl+Z 入力 |  | END → ENTER | Ctrl+V 入力 |  |  |  |
| ダブルタップ |  | ESC 入力 × 2 | Ctrl+→ 入力 × 2 | Ctrl+→ 入力 × 2 |  |  | HOME → Shift+END → Ctrl+C | Ctrl+Z 入力 × 2 |  | END → ENTER（2 回実行） | Ctrl+V 入力 × 2 |  |  |  |
| Shift+ |  | Ctrl+Q 入力 | Shift + Ctrl+→（OS で合成） | Shift + Ctrl+→（OS で合成） |  |  | Shift+END → Ctrl+C | Shift + Ctrl+Z（OS で合成） |  | HOME → ENTER → ↑ | Shift + Ctrl+V（OS で合成） |  |  |  |
| Ctrl+ |  | Ctrl + ESC（OS で合成） | Ctrl+BACKSPACE 入力 | Ctrl + Ctrl+→（OS で合成） | Ctrl+Y 入力 |  | Ctrl + Ctrl+C（OS で合成） | PAGE_UP 入力 |  | END → ENTER（Ctrl 物理保持で実行） | Ctrl + Ctrl+V（OS で合成） |  |  |  |
| ■ Row 2 (home row) | (outer)<br>`&none` | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&mm_vim_ctrl_then_shift_d` | F<br>`&none` | G<br>`&mm_vim_g` | (center L)<br>`&none` | (center R)<br>`&none` | H<br>`&kp LEFT` | J<br>`&mm_vim_j` | K<br>`&kp UP_ARROW` | L<br>`&kp RIGHT` | MINUS<br>`&kp RCTRL` | (outer)<br>`&none` |
| 単発タップ |  | Left Ctrl 入力 |  |  |  |  |  |  | ← 入力 | ↓ 入力 | ↑ 入力 | → 入力 | Right Ctrl 入力 |  |
| ダブルタップ |  | Left Ctrl 入力 × 2 |  | HOME → Shift+END → Ctrl+X |  | Ctrl+HOME 入力 |  |  | ← 入力 × 2 | ↓ 入力 × 2 | ↑ 入力 × 2 | → 入力 × 2 | Right Ctrl 入力 × 2 |  |
| Shift+ |  | Shift + Left Ctrl（OS で合成） |  | Shift+END → Ctrl+X |  | Ctrl+END 入力 |  |  | Shift + ←（OS で合成） | END → DELETE → SPACE | Shift + ↑（OS で合成） | Shift + →（OS で合成） | Shift + Right Ctrl（OS で合成） |  |
| Ctrl+ |  | Ctrl + Left Ctrl（OS で合成） |  | PAGE_DOWN 入力 |  |  |  |  | Ctrl + ←（OS で合成） | Ctrl + ↓（OS で合成） | Ctrl + ↑（OS で合成） | Ctrl + →（OS で合成） | Ctrl + Right Ctrl（OS で合成） |  |
| ■ Row 3 (Z row) | (outer)<br>`&none` | Z<br>`&kp LEFT_SHIFT` | X<br>`&kp DELETE` | C<br>`&none` | V<br>`&mm_vim_v` | B<br>`&kp LC(LEFT)` | (center L)<br>`&none` | (center R)<br>`&none` | N<br>`&mm_vim_n` | M<br>`&none` | COMMA<br>`&none` | PERIOD<br>`&none` | SLASH<br>`&kp RIGHT_SHIFT` | (outer)<br>`&none` |
| 単発タップ |  | Left Shift 入力 | DELETE 入力 |  | レイヤー 8 に切替 | Ctrl+← 入力 |  |  | F3 入力 |  |  |  | Right Shift 入力 |  |
| ダブルタップ |  | Left Shift 入力 × 2 | DELETE 入力 × 2 |  | レイヤー 8 に切替 | Ctrl+← 入力 × 2 |  |  | F3 入力 × 2 |  |  |  | Right Shift 入力 × 2 |  |
| Shift+ |  | Shift + Left Shift（OS で合成） | Shift + DELETE（OS で合成） |  | HOME → Shift+↓ → レイヤー 8 へ | Shift + Ctrl+←（OS で合成） |  |  | Shift+F3 入力 |  |  |  | Shift + Right Shift（OS で合成） |  |
| Ctrl+ |  | Ctrl + Left Shift（OS で合成） | Ctrl + DELETE（OS で合成） |  | レイヤー 8 に切替 | Ctrl + Ctrl+←（OS で合成） |  |  | Ctrl + F3（OS で合成） |  |  |  | Ctrl + Right Shift（OS で合成） |  |
| ■ Row 4 (thumb) | (outer)<br>`&none` | mo6 (outer)<br>`&none` | LEFT_WIN<br>`&trans` | LEFT_ALT<br>`&trans` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | (mo1 center)<br>`&mo 3` | (mo2 center)<br>`&none` | lt1 ENTER<br>`&lt 3 ENTER` | (none)<br>`&none` | (none)<br>`&none` | mo6<br>`&trans` | mo6 (outer)<br>`&none` | (outer)<br>`&none` |
| 単発タップ |  |  | ▽ | ▽ |  |  | レイヤー 3 を momentary（押下中のみ）有効化 |  | ENTER 入力（タップ） |  |  | ▽ |  |  |
| ダブルタップ |  |  | ▽ | ▽ |  |  | レイヤー 3 を momentary（押下中のみ）有効化 |  | ENTER 入力 × 2 |  |  | ▽ |  |  |
| Shift+ |  |  | ▽ | ▽ |  |  | レイヤー 3 を momentary（押下中のみ）有効化 |  | Shift + ENTER（ホールドでレイヤー 3） |  |  | ▽ |  |  |
| Ctrl+ |  |  | ▽ | ▽ |  |  | レイヤー 3 を momentary（押下中のみ）有効化 |  | Ctrl + ENTER（ホールドでレイヤー 3） |  |  | ▽ |  |  |

### VIM_NORMAL_2 レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 0 (top wing) | (outer)<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | (outer)<br>`&none` |  |  |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ダブルタップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Shift+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ctrl+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ■ Row 1 (QWERTY 上段) | (outer)<br>`&none` | Q<br>`&none` | W<br>`&none` | E<br>`&none` | R<br>`&mm_vim_shift_4` | T<br>`&none` | Y<br>`&mm_vim_shift_6` | U<br>`&none` | I<br>`&none` | O<br>`&none` | P<br>`&kp HOME` | (outer)<br>`&none` |  |  |
| 単発タップ |  |  |  |  |  |  |  |  |  |  | HOME 入力 |  |  |  |
| ダブルタップ |  |  |  |  |  |  |  |  |  |  | HOME 入力 × 2 |  |  |  |
| Shift+ |  |  |  |  | END 入力 |  | HOME 入力 |  |  |  | Shift + HOME（OS で合成） |  |  |  |
| Ctrl+ |  |  |  |  |  |  |  |  |  |  | Ctrl + HOME（OS で合成） |  |  |  |
| ■ Row 2 (home row) | (outer)<br>`&none` | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&none` | F<br>`&none` | G<br>`&none` | (center L)<br>`&none` | (center R)<br>`&none` | H<br>`&kp LEFT` | J<br>`&none` | K<br>`&none` | L<br>`&none` | MINUS<br>`&kp RCTRL` | (outer)<br>`&none` |
| 単発タップ |  | Left Ctrl 入力 |  |  |  |  |  |  | ← 入力 |  |  |  | Right Ctrl 入力 |  |
| ダブルタップ |  | Left Ctrl 入力 × 2 |  |  |  |  |  |  | ← 入力 × 2 |  |  |  | Right Ctrl 入力 × 2 |  |
| Shift+ |  | Shift + Left Ctrl（OS で合成） |  |  |  |  |  |  | Shift + ←（OS で合成） |  |  |  | Shift + Right Ctrl（OS で合成） |  |
| Ctrl+ |  | Ctrl + Left Ctrl（OS で合成） |  |  |  |  |  |  | Ctrl + ←（OS で合成） |  |  |  | Ctrl + Right Ctrl（OS で合成） |  |
| ■ Row 3 (Z row) | (outer)<br>`&none` | Z<br>`&kp LEFT_SHIFT` | X<br>`&none` | C<br>`&none` | V<br>`&none` | B<br>`&none` | (center L)<br>`&none` | (center R)<br>`&none` | N<br>`&none` | M<br>`&none` | COMMA<br>`&none` | PERIOD<br>`&none` | SLASH<br>`&kp RIGHT_SHIFT` | (outer)<br>`&none` |
| 単発タップ |  | Left Shift 入力 |  |  |  |  |  |  |  |  |  |  | Right Shift 入力 |  |
| ダブルタップ |  | Left Shift 入力 × 2 |  |  |  |  |  |  |  |  |  |  | Right Shift 入力 × 2 |  |
| Shift+ |  | Shift + Left Shift（OS で合成） |  |  |  |  |  |  |  |  |  |  | Shift + Right Shift（OS で合成） |  |
| Ctrl+ |  | Ctrl + Left Shift（OS で合成） |  |  |  |  |  |  |  |  |  |  | Ctrl + Right Shift（OS で合成） |  |
| ■ Row 4 (thumb) | (outer)<br>`&none` | mo6 (outer)<br>`&none` | LEFT_WIN<br>`&trans` | LEFT_ALT<br>`&trans` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | (mo1 center)<br>`&none` | (mo2 center)<br>`&none` | lt1 ENTER<br>`&none` | (none)<br>`&none` | (none)<br>`&none` | mo6<br>`&trans` | mo6 (outer)<br>`&none` | (outer)<br>`&none` |
| 単発タップ |  |  | ▽ | ▽ |  |  |  |  |  |  |  | ▽ |  |  |
| ダブルタップ |  |  | ▽ | ▽ |  |  |  |  |  |  |  | ▽ |  |  |
| Shift+ |  |  | ▽ | ▽ |  |  |  |  |  |  |  | ▽ |  |  |
| Ctrl+ |  |  | ▽ | ▽ |  |  |  |  |  |  |  | ▽ |  |  |

### MOUSE レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 0 (top wing) | (outer)<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | (outer)<br>`&none` |  |  |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ダブルタップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Shift+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ctrl+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ■ Row 1 (QWERTY 上段) | (outer)<br>`&none` | Q<br>`&none` | W<br>`&none` | E<br>`&none` | R<br>`&none` | T<br>`&none` | Y<br>`&none` | U<br>`&none` | I<br>`&none` | O<br>`&none` | P<br>`&none` | (outer)<br>`&none` |  |  |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ダブルタップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Shift+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ctrl+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ■ Row 2 (home row) | (outer)<br>`&none` | A<br>`&none` | S<br>`&none` | D<br>`&none` | F<br>`&none` | G<br>`&none` | (center L)<br>`&none` | (center R)<br>`&none` | H<br>`&none` | J<br>`&none` | K<br>`&mo 5` | L<br>`&none` | MINUS<br>`&none` | (outer)<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  | レイヤー 5 を momentary（押下中のみ）有効化 |  |  |  |
| ダブルタップ |  |  |  |  |  |  |  |  |  |  | レイヤー 5 を momentary（押下中のみ）有効化 |  |  |  |
| Shift+ |  |  |  |  |  |  |  |  |  |  | レイヤー 5 を momentary（押下中のみ）有効化 |  |  |  |
| Ctrl+ |  |  |  |  |  |  |  |  |  |  | レイヤー 5 を momentary（押下中のみ）有効化 |  |  |  |
| ■ Row 3 (Z row) | (outer)<br>`&none` | Z<br>`&none` | X<br>`&none` | C<br>`&none` | V<br>`&none` | B<br>`&none` | (center L)<br>`&none` | (center R)<br>`&none` | N<br>`&none` | M<br>`&none` | COMMA<br>`&none` | PERIOD<br>`&none` | SLASH<br>`&none` | (outer)<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ダブルタップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Shift+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ctrl+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ■ Row 4 (thumb) | (outer)<br>`&none` | mo6 (outer)<br>`&none` | LEFT_WIN<br>`&none` | LEFT_ALT<br>`&none` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | (mo1 center)<br>`&none` | (mo2 center)<br>`&none` | lt1 ENTER<br>`&none` | (none)<br>`&none` | (none)<br>`&none` | mo6<br>`&none` | mo6 (outer)<br>`&none` | (outer)<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ダブルタップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Shift+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ctrl+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### SCROLL レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 0 (top wing) | (outer)<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | (outer)<br>`&none` |  |  |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ダブルタップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Shift+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ctrl+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ■ Row 1 (QWERTY 上段) | (outer)<br>`&none` | Q<br>`&none` | W<br>`&none` | E<br>`&none` | R<br>`&none` | T<br>`&none` | Y<br>`&none` | U<br>`&none` | I<br>`&none` | O<br>`&none` | P<br>`&none` | (outer)<br>`&none` |  |  |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ダブルタップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Shift+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ctrl+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ■ Row 2 (home row) | (outer)<br>`&none` | A<br>`&none` | S<br>`&none` | D<br>`&none` | F<br>`&none` | G<br>`&none` | (center L)<br>`&none` | (center R)<br>`&none` | H<br>`&none` | J<br>`&mkp MB1` | K<br>`&none` | L<br>`&mkp MB2` | MINUS<br>`&none` | (outer)<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  | 未対応: &mkp MB1 |  | 未対応: &mkp MB2 |  |  |
| ダブルタップ |  |  |  |  |  |  |  |  |  | 未対応: &mkp MB1 |  | 未対応: &mkp MB2 |  |  |
| Shift+ |  |  |  |  |  |  |  |  |  | 未対応: &mkp MB1 |  | 未対応: &mkp MB2 |  |  |
| Ctrl+ |  |  |  |  |  |  |  |  |  | 未対応: &mkp MB1 |  | 未対応: &mkp MB2 |  |  |
| ■ Row 3 (Z row) | (outer)<br>`&none` | Z<br>`&none` | X<br>`&none` | C<br>`&none` | V<br>`&none` | B<br>`&none` | (center L)<br>`&none` | (center R)<br>`&none` | N<br>`&none` | M<br>`&mkp MB4` | COMMA<br>`&none` | PERIOD<br>`&mkp MB5` | SLASH<br>`&none` | (outer)<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  | 未対応: &mkp MB4 |  | 未対応: &mkp MB5 |  |  |
| ダブルタップ |  |  |  |  |  |  |  |  |  | 未対応: &mkp MB4 |  | 未対応: &mkp MB5 |  |  |
| Shift+ |  |  |  |  |  |  |  |  |  | 未対応: &mkp MB4 |  | 未対応: &mkp MB5 |  |  |
| Ctrl+ |  |  |  |  |  |  |  |  |  | 未対応: &mkp MB4 |  | 未対応: &mkp MB5 |  |  |
| ■ Row 4 (thumb) | (outer)<br>`&none` | mo6 (outer)<br>`&none` | LEFT_WIN<br>`&none` | LEFT_ALT<br>`&none` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | (mo1 center)<br>`&none` | (mo2 center)<br>`&none` | lt1 ENTER<br>`&none` | (none)<br>`&none` | (none)<br>`&none` | mo6<br>`&none` | mo6 (outer)<br>`&none` | (outer)<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ダブルタップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Shift+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ctrl+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### FUNCTION レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 0 (top wing) | (outer)<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | (outer)<br>`&none` |  |  |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ダブルタップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Shift+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ctrl+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ■ Row 1 (QWERTY 上段) | (outer)<br>`&none` | Q<br>`&kp F1` | W<br>`&kp F2` | E<br>`&kp F3` | R<br>`&kp F4` | T<br>`&kp F5` | Y<br>`&kp F6` | U<br>`&kp F7` | I<br>`&kp F8` | O<br>`&kp F9` | P<br>`&kp F10` | (outer)<br>`&none` |  |  |
| 単発タップ |  | F1 入力 | F2 入力 | F3 入力 | F4 入力 | F5 入力 | F6 入力 | F7 入力 | F8 入力 | F9 入力 | F10 入力 |  |  |  |
| ダブルタップ |  | F1 入力 × 2 | F2 入力 × 2 | F3 入力 × 2 | F4 入力 × 2 | F5 入力 × 2 | F6 入力 × 2 | F7 入力 × 2 | F8 入力 × 2 | F9 入力 × 2 | F10 入力 × 2 |  |  |  |
| Shift+ |  | Shift + F1（OS で合成） | Shift + F2（OS で合成） | Shift + F3（OS で合成） | Shift + F4（OS で合成） | Shift + F5（OS で合成） | Shift + F6（OS で合成） | Shift + F7（OS で合成） | Shift + F8（OS で合成） | Shift + F9（OS で合成） | Shift + F10（OS で合成） |  |  |  |
| Ctrl+ |  | Ctrl + F1（OS で合成） | Ctrl + F2（OS で合成） | Ctrl + F3（OS で合成） | Ctrl + F4（OS で合成） | Ctrl + F5（OS で合成） | Ctrl + F6（OS で合成） | Ctrl + F7（OS で合成） | Ctrl + F8（OS で合成） | Ctrl + F9（OS で合成） | Ctrl + F10（OS で合成） |  |  |  |
| ■ Row 2 (home row) | (outer)<br>`&none` | A<br>`&none` | S<br>`&sys_reset` | D<br>`&none` | F<br>`&none` | G<br>`&none` | (center L)<br>`&none` | (center R)<br>`&none` | H<br>`&none` | J<br>`&none` | K<br>`&none` | L<br>`&sys_reset` | MINUS<br>`&none` | (outer)<br>`&none` |
| 単発タップ |  |  | 未対応: &sys_reset |  |  |  |  |  |  |  |  | 未対応: &sys_reset |  |  |
| ダブルタップ |  |  | 未対応: &sys_reset |  |  |  |  |  |  |  |  | 未対応: &sys_reset |  |  |
| Shift+ |  |  | 未対応: &sys_reset |  |  |  |  |  |  |  |  | 未対応: &sys_reset |  |  |
| Ctrl+ |  |  | 未対応: &sys_reset |  |  |  |  |  |  |  |  | 未対応: &sys_reset |  |  |
| ■ Row 3 (Z row) | (outer)<br>`&none` | Z<br>`&none` | X<br>`&none` | C<br>`&none` | V<br>`&none` | B<br>`&bootloader` | (center L)<br>`&none` | (center R)<br>`&none` | N<br>`&bootloader` | M<br>`&none` | COMMA<br>`&none` | PERIOD<br>`&none` | SLASH<br>`&none` | (outer)<br>`&none` |
| 単発タップ |  |  |  |  |  | 未対応: &bootloader |  |  | 未対応: &bootloader |  |  |  |  |  |
| ダブルタップ |  |  |  |  |  | 未対応: &bootloader |  |  | 未対応: &bootloader |  |  |  |  |  |
| Shift+ |  |  |  |  |  | 未対応: &bootloader |  |  | 未対応: &bootloader |  |  |  |  |  |
| Ctrl+ |  |  |  |  |  | 未対応: &bootloader |  |  | 未対応: &bootloader |  |  |  |  |  |
| ■ Row 4 (thumb) | (outer)<br>`&none` | mo6 (outer)<br>`&none` | LEFT_WIN<br>`&none` | LEFT_ALT<br>`&none` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | (mo1 center)<br>`&none` | (mo2 center)<br>`&none` | lt1 ENTER<br>`&none` | (none)<br>`&none` | (none)<br>`&none` | mo6<br>`&none` | mo6 (outer)<br>`&none` | (outer)<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ダブルタップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Shift+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ctrl+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### BLUETOOTH レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 0 (top wing) | (outer)<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | (outer)<br>`&none` |  |  |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ダブルタップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Shift+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ctrl+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ■ Row 1 (QWERTY 上段) | (outer)<br>`&none` | Q<br>`&bt BT_SEL 0` | W<br>`&bt BT_SEL 1` | E<br>`&bt BT_SEL 2` | R<br>`&bt BT_SEL 3` | T<br>`&bt BT_SEL 4` | Y<br>`&none` | U<br>`&out OUT_USB` | I<br>`&none` | O<br>`&none` | P<br>`&none` | (outer)<br>`&none` |  |  |
| 単発タップ |  | 未対応: &bt BT_SEL 0 | 未対応: &bt BT_SEL 1 | 未対応: &bt BT_SEL 2 | 未対応: &bt BT_SEL 3 | 未対応: &bt BT_SEL 4 |  | 未対応: &out OUT_USB |  |  |  |  |  |  |
| ダブルタップ |  | 未対応: &bt BT_SEL 0 | 未対応: &bt BT_SEL 1 | 未対応: &bt BT_SEL 2 | 未対応: &bt BT_SEL 3 | 未対応: &bt BT_SEL 4 |  | 未対応: &out OUT_USB |  |  |  |  |  |  |
| Shift+ |  | 未対応: &bt BT_SEL 0 | 未対応: &bt BT_SEL 1 | 未対応: &bt BT_SEL 2 | 未対応: &bt BT_SEL 3 | 未対応: &bt BT_SEL 4 |  | 未対応: &out OUT_USB |  |  |  |  |  |  |
| Ctrl+ |  | 未対応: &bt BT_SEL 0 | 未対応: &bt BT_SEL 1 | 未対応: &bt BT_SEL 2 | 未対応: &bt BT_SEL 3 | 未対応: &bt BT_SEL 4 |  | 未対応: &out OUT_USB |  |  |  |  |  |  |
| ■ Row 2 (home row) | (outer)<br>`&none` | A<br>`&bt BT_CLR_ALL` | S<br>`&none` | D<br>`&none` | F<br>`&none` | G<br>`&none` | (center L)<br>`&none` | (center R)<br>`&none` | H<br>`&none` | J<br>`&none` | K<br>`&none` | L<br>`&none` | MINUS<br>`&none` | (outer)<br>`&none` |
| 単発タップ |  | 未対応: &bt BT_CLR_ALL |  |  |  |  |  |  |  |  |  |  |  |  |
| ダブルタップ |  | 未対応: &bt BT_CLR_ALL |  |  |  |  |  |  |  |  |  |  |  |  |
| Shift+ |  | 未対応: &bt BT_CLR_ALL |  |  |  |  |  |  |  |  |  |  |  |  |
| Ctrl+ |  | 未対応: &bt BT_CLR_ALL |  |  |  |  |  |  |  |  |  |  |  |  |
| ■ Row 3 (Z row) | (outer)<br>`&none` | Z<br>`&none` | X<br>`&none` | C<br>`&bt BT_CLR` | V<br>`&none` | B<br>`&out OUT_BLE` | (center L)<br>`&none` | (center R)<br>`&none` | N<br>`&none` | M<br>`&none` | COMMA<br>`&none` | PERIOD<br>`&none` | SLASH<br>`&none` | (outer)<br>`&none` |
| 単発タップ |  |  |  | 未対応: &bt BT_CLR |  | 未対応: &out OUT_BLE |  |  |  |  |  |  |  |  |
| ダブルタップ |  |  |  | 未対応: &bt BT_CLR |  | 未対応: &out OUT_BLE |  |  |  |  |  |  |  |  |
| Shift+ |  |  |  | 未対応: &bt BT_CLR |  | 未対応: &out OUT_BLE |  |  |  |  |  |  |  |  |
| Ctrl+ |  |  |  | 未対応: &bt BT_CLR |  | 未対応: &out OUT_BLE |  |  |  |  |  |  |  |  |
| ■ Row 4 (thumb) | (outer)<br>`&none` | mo6 (outer)<br>`&none` | LEFT_WIN<br>`&none` | LEFT_ALT<br>`&none` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | (mo1 center)<br>`&none` | (mo2 center)<br>`&none` | lt1 ENTER<br>`&none` | (none)<br>`&none` | (none)<br>`&none` | mo6<br>`&none` | mo6 (outer)<br>`&none` | (outer)<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ダブルタップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Shift+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ctrl+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### VIM_VISUAL レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 0 (top wing) | (outer)<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | (outer)<br>`&none` |  |  |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ダブルタップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Shift+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ctrl+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ■ Row 1 (QWERTY 上段) | (outer)<br>`&none` | Q<br>`&macro_vim_visual_exit` | W<br>`&kp LS(LC(RIGHT))` | E<br>`&kp LS(LC(RIGHT))` | R<br>`&none` | T<br>`&none` | Y<br>`&none` | U<br>`&none` | I<br>`&none` | O<br>`&none` | P<br>`&macro_vim_visual_p` | (outer)<br>`&none` |  |  |
| 単発タップ |  | Left Shift → RSHIFT &kp RIGHT → レイヤー 0 へ | Shift+Ctrl+→ 入力 | Shift+Ctrl+→ 入力 |  |  |  |  |  |  | Left Shift → RSHIFT &kp LC(V) → レイヤー 0 へ |  |  |  |
| ダブルタップ |  | Left Shift → RSHIFT &kp RIGHT → レイヤー 0 へ（2 回実行） | Shift+Ctrl+→ 入力 × 2 | Shift+Ctrl+→ 入力 × 2 |  |  |  |  |  |  | Left Shift → RSHIFT &kp LC(V) → レイヤー 0 へ（2 回実行） |  |  |  |
| Shift+ |  | Left Shift → RSHIFT &kp RIGHT → レイヤー 0 へ（Shift 物理保持で実行） | Shift + Shift+Ctrl+→（OS で合成） | Shift + Shift+Ctrl+→（OS で合成） |  |  |  |  |  |  | Left Shift → RSHIFT &kp LC(V) → レイヤー 0 へ（Shift 物理保持で実行） |  |  |  |
| Ctrl+ |  | Left Shift → RSHIFT &kp RIGHT → レイヤー 0 へ（Ctrl 物理保持で実行） | Ctrl + Shift+Ctrl+→（OS で合成） | Ctrl + Shift+Ctrl+→（OS で合成） |  |  |  |  |  |  | Left Shift → RSHIFT &kp LC(V) → レイヤー 0 へ（Ctrl 物理保持で実行） |  |  |  |
| ■ Row 2 (home row) | (outer)<br>`&none` | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&macro_vim_visual_cut` | F<br>`&none` | G<br>`&mm_vim_visual_g` | (center L)<br>`&none` | (center R)<br>`&none` | H<br>`&kp LS(LEFT)` | J<br>`&kp LS(DOWN)` | K<br>`&kp LS(UP)` | L<br>`&kp LS(RIGHT)` | MINUS<br>`&kp RCTRL` | (outer)<br>`&none` |
| 単発タップ |  | Left Ctrl 入力 |  | Left Shift → RSHIFT &kp LC(X) → レイヤー 0 へ |  |  |  |  | Shift+← 入力 | Shift+↓ 入力 | Shift+UP 入力 | Shift+→ 入力 | Right Ctrl 入力 |  |
| ダブルタップ |  | Left Ctrl 入力 × 2 |  | Left Shift → RSHIFT &kp LC(X) → レイヤー 0 へ（2 回実行） |  | Shift+Ctrl+HOME 入力 |  |  | Shift+← 入力 × 2 | Shift+↓ 入力 × 2 | Shift+UP 入力 × 2 | Shift+→ 入力 × 2 | Right Ctrl 入力 × 2 |  |
| Shift+ |  | Shift + Left Ctrl（OS で合成） |  | Left Shift → RSHIFT &kp LC(X) → レイヤー 0 へ（Shift 物理保持で実行） |  | Shift+Ctrl+END 入力 |  |  | Shift + Shift+←（OS で合成） | Shift + Shift+↓（OS で合成） | Shift + Shift+UP（OS で合成） | Shift + Shift+→（OS で合成） | Shift + Right Ctrl（OS で合成） |  |
| Ctrl+ |  | Ctrl + Left Ctrl（OS で合成） |  | Left Shift → RSHIFT &kp LC(X) → レイヤー 0 へ（Ctrl 物理保持で実行） |  |  |  |  | Ctrl + Shift+←（OS で合成） | Ctrl + Shift+↓（OS で合成） | Ctrl + Shift+UP（OS で合成） | Ctrl + Shift+→（OS で合成） | Ctrl + Right Ctrl（OS で合成） |  |
| ■ Row 3 (Z row) | (outer)<br>`&none` | Z<br>`&kp LEFT_SHIFT` | X<br>`&macro_vim_visual_cut` | C<br>`&none` | V<br>`&macro_vim_visual_exit` | B<br>`&kp LS(LC(LEFT))` | (center L)<br>`&none` | (center R)<br>`&none` | N<br>`&kp F3` | M<br>`&none` | COMMA<br>`&none` | PERIOD<br>`&none` | SLASH<br>`&kp RIGHT_SHIFT` | (outer)<br>`&none` |
| 単発タップ |  | Left Shift 入力 | Left Shift → RSHIFT &kp LC(X) → レイヤー 0 へ |  | Left Shift → RSHIFT &kp RIGHT → レイヤー 0 へ | Shift+Ctrl+← 入力 |  |  | F3 入力 |  |  |  | Right Shift 入力 |  |
| ダブルタップ |  | Left Shift 入力 × 2 | Left Shift → RSHIFT &kp LC(X) → レイヤー 0 へ（2 回実行） |  | Left Shift → RSHIFT &kp RIGHT → レイヤー 0 へ（2 回実行） | Shift+Ctrl+← 入力 × 2 |  |  | F3 入力 × 2 |  |  |  | Right Shift 入力 × 2 |  |
| Shift+ |  | Shift + Left Shift（OS で合成） | Left Shift → RSHIFT &kp LC(X) → レイヤー 0 へ（Shift 物理保持で実行） |  | Left Shift → RSHIFT &kp RIGHT → レイヤー 0 へ（Shift 物理保持で実行） | Shift + Shift+Ctrl+←（OS で合成） |  |  | Shift + F3（OS で合成） |  |  |  | Shift + Right Shift（OS で合成） |  |
| Ctrl+ |  | Ctrl + Left Shift（OS で合成） | Left Shift → RSHIFT &kp LC(X) → レイヤー 0 へ（Ctrl 物理保持で実行） |  | Left Shift → RSHIFT &kp RIGHT → レイヤー 0 へ（Ctrl 物理保持で実行） | Ctrl + Shift+Ctrl+←（OS で合成） |  |  | Ctrl + F3（OS で合成） |  |  |  | Ctrl + Right Shift（OS で合成） |  |
| ■ Row 4 (thumb) | (outer)<br>`&none` | mo6 (outer)<br>`&none` | LEFT_WIN<br>`&none` | LEFT_ALT<br>`&none` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | (mo1 center)<br>`&none` | (mo2 center)<br>`&none` | lt1 ENTER<br>`&none` | (none)<br>`&none` | (none)<br>`&none` | mo6<br>`&none` | mo6 (outer)<br>`&none` | (outer)<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ダブルタップ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Shift+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ctrl+ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## 経路

### DEFAULT レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 0 (top wing) | (outer)<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | (outer)<br>`&none` |  |  |
| 単発タップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| ダブルタップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| Shift+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| Ctrl+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| ■ Row 1 (QWERTY 上段) | (outer)<br>`&none` | Q<br>`&kp Q` | W<br>`&kp W` | E<br>`&kp E` | R<br>`&kp R` | T<br>`&kp T` | Y<br>`&kp Y` | U<br>`&kp U` | I<br>`&kp I` | O<br>`&kp O` | P<br>`&kp P` | (outer)<br>`&none` |  |  |
| 単発タップ | &none | &kp Q | &kp W | &kp E | &kp R | &kp T | &kp Y | &kp U | &kp I | &kp O | &kp P | &none |  |  |
| ダブルタップ | &none | &kp Q（tap-dance 未定義、連打） | &kp W（tap-dance 未定義、連打） | &kp E（tap-dance 未定義、連打） | &kp R（tap-dance 未定義、連打） | &kp T（tap-dance 未定義、連打） | &kp Y（tap-dance 未定義、連打） | &kp U（tap-dance 未定義、連打） | &kp I（tap-dance 未定義、連打） | &kp O（tap-dance 未定義、連打） | &kp P（tap-dance 未定義、連打） | &none |  |  |
| Shift+ | &none | &kp Q（物理 Shift は HID にそのまま伝わる） | &kp W（物理 Shift は HID にそのまま伝わる） | &kp E（物理 Shift は HID にそのまま伝わる） | &kp R（物理 Shift は HID にそのまま伝わる） | &kp T（物理 Shift は HID にそのまま伝わる） | &kp Y（物理 Shift は HID にそのまま伝わる） | &kp U（物理 Shift は HID にそのまま伝わる） | &kp I（物理 Shift は HID にそのまま伝わる） | &kp O（物理 Shift は HID にそのまま伝わる） | &kp P（物理 Shift は HID にそのまま伝わる） | &none |  |  |
| Ctrl+ | &none | &kp Q（物理 Ctrl は HID にそのまま伝わる） | &kp W（物理 Ctrl は HID にそのまま伝わる） | &kp E（物理 Ctrl は HID にそのまま伝わる） | &kp R（物理 Ctrl は HID にそのまま伝わる） | &kp T（物理 Ctrl は HID にそのまま伝わる） | &kp Y（物理 Ctrl は HID にそのまま伝わる） | &kp U（物理 Ctrl は HID にそのまま伝わる） | &kp I（物理 Ctrl は HID にそのまま伝わる） | &kp O（物理 Ctrl は HID にそのまま伝わる） | &kp P（物理 Ctrl は HID にそのまま伝わる） | &none |  |  |
| ■ Row 2 (home row) | (outer)<br>`&none` | A<br>`&mt LEFT_CONTROL A` | S<br>`&kp S` | D<br>`&kp D` | F<br>`&kp F` | G<br>`&kp G` | (center L)<br>`&none` | (center R)<br>`&none` | H<br>`&kp H` | J<br>`&kp J` | K<br>`&kp K` | L<br>`&kp L` | MINUS<br>`&mt RCTRL MINUS` | (outer)<br>`&none` |
| 単発タップ | &none | &mt LEFT_CONTROL A | &kp S | &kp D | &kp F | &kp G | &none | &none | &kp H | &kp J | &kp K | &kp L | &mt RCTRL MINUS | &none |
| ダブルタップ | &none | &mt LEFT_CONTROL A（連打） | &kp S（tap-dance 未定義、連打） | &kp D（tap-dance 未定義、連打） | &kp F（tap-dance 未定義、連打） | &kp G（tap-dance 未定義、連打） | &none | &none | &kp H（tap-dance 未定義、連打） | &kp J（tap-dance 未定義、連打） | &kp K（tap-dance 未定義、連打） | &kp L（tap-dance 未定義、連打） | &mt RCTRL MINUS（連打） | &none |
| Shift+ | &none | &mt LEFT_CONTROL A | &kp S（物理 Shift は HID にそのまま伝わる） | &kp D（物理 Shift は HID にそのまま伝わる） | &kp F（物理 Shift は HID にそのまま伝わる） | &kp G（物理 Shift は HID にそのまま伝わる） | &none | &none | &kp H（物理 Shift は HID にそのまま伝わる） | &kp J（物理 Shift は HID にそのまま伝わる） | &kp K（物理 Shift は HID にそのまま伝わる） | &kp L（物理 Shift は HID にそのまま伝わる） | &mt RCTRL MINUS | &none |
| Ctrl+ | &none | &mt LEFT_CONTROL A | &kp S（物理 Ctrl は HID にそのまま伝わる） | &kp D（物理 Ctrl は HID にそのまま伝わる） | &kp F（物理 Ctrl は HID にそのまま伝わる） | &kp G（物理 Ctrl は HID にそのまま伝わる） | &none | &none | &kp H（物理 Ctrl は HID にそのまま伝わる） | &kp J（物理 Ctrl は HID にそのまま伝わる） | &kp K（物理 Ctrl は HID にそのまま伝わる） | &kp L（物理 Ctrl は HID にそのまま伝わる） | &mt RCTRL MINUS | &none |
| ■ Row 3 (Z row) | (outer)<br>`&none` | Z<br>`&mt LEFT_SHIFT Z` | X<br>`&kp X` | C<br>`&kp C` | V<br>`&kp V` | B<br>`&kp B` | (center L)<br>`&mo 7` | (center R)<br>`&mo 7` | N<br>`&kp N` | M<br>`&kp M` | COMMA<br>`&kp COMMA` | PERIOD<br>`&kp PERIOD` | SLASH<br>`&mt RIGHT_SHIFT SLASH` | (outer)<br>`&none` |
| 単発タップ | &none | &mt LEFT_SHIFT Z | &kp X | &kp C | &kp V | &kp B | &mo 7 | &mo 7 | &kp N | &kp M | &kp COMMA | &kp PERIOD | &mt RIGHT_SHIFT SLASH | &none |
| ダブルタップ | &none | &mt LEFT_SHIFT Z（連打） | &kp X（tap-dance 未定義、連打） | &kp C（tap-dance 未定義、連打） | &kp V（tap-dance 未定義、連打） | &kp B（tap-dance 未定義、連打） | &mo 7 | &mo 7 | &kp N（tap-dance 未定義、連打） | &kp M（tap-dance 未定義、連打） | &kp COMMA（tap-dance 未定義、連打） | &kp PERIOD（tap-dance 未定義、連打） | &mt RIGHT_SHIFT SLASH（連打） | &none |
| Shift+ | &none | &mt LEFT_SHIFT Z | &kp X（物理 Shift は HID にそのまま伝わる） | &kp C（物理 Shift は HID にそのまま伝わる） | &kp V（物理 Shift は HID にそのまま伝わる） | &kp B（物理 Shift は HID にそのまま伝わる） | &mo 7 | &mo 7 | &kp N（物理 Shift は HID にそのまま伝わる） | &kp M（物理 Shift は HID にそのまま伝わる） | &kp COMMA（物理 Shift は HID にそのまま伝わる） | &kp PERIOD（物理 Shift は HID にそのまま伝わる） | &mt RIGHT_SHIFT SLASH | &none |
| Ctrl+ | &none | &mt LEFT_SHIFT Z | &kp X（物理 Ctrl は HID にそのまま伝わる） | &kp C（物理 Ctrl は HID にそのまま伝わる） | &kp V（物理 Ctrl は HID にそのまま伝わる） | &kp B（物理 Ctrl は HID にそのまま伝わる） | &mo 7 | &mo 7 | &kp N（物理 Ctrl は HID にそのまま伝わる） | &kp M（物理 Ctrl は HID にそのまま伝わる） | &kp COMMA（物理 Ctrl は HID にそのまま伝わる） | &kp PERIOD（物理 Ctrl は HID にそのまま伝わる） | &mt RIGHT_SHIFT SLASH | &none |
| ■ Row 4 (thumb) | (outer)<br>`&none` | mo6 (outer)<br>`&mo 6` | LEFT_WIN<br>`&kp LEFT_WIN` | LEFT_ALT<br>`&kp LEFT_ALT` | lt2 SPACE<br>`&lt 2 SPACE` | lt2 SPACE<br>`&lt 2 SPACE` | (mo1 center)<br>`&mo 1` | (mo2 center)<br>`&mo 2` | lt1 ENTER<br>`&lt 1 ENTER` | (none)<br>`&none` | (none)<br>`&none` | mo6<br>`&mo 6` | mo6 (outer)<br>`&mo 6` | (outer)<br>`&none` |
| 単発タップ | &none | &mo 6 | &kp LEFT_WIN | &kp LEFT_ALT | &lt 2 SPACE | &lt 2 SPACE | &mo 1 | &mo 2 | &lt 1 ENTER | &none | &none | &mo 6 | &mo 6 | &none |
| ダブルタップ | &none | &mo 6 | &kp LEFT_WIN（tap-dance 未定義、連打） | &kp LEFT_ALT（tap-dance 未定義、連打） | &lt 2 SPACE（連打） | &lt 2 SPACE（連打） | &mo 1 | &mo 2 | &lt 1 ENTER（連打） | &none | &none | &mo 6 | &mo 6 | &none |
| Shift+ | &none | &mo 6 | &kp LEFT_WIN（物理 Shift は HID にそのまま伝わる） | &kp LEFT_ALT（物理 Shift は HID にそのまま伝わる） | &lt 2 SPACE | &lt 2 SPACE | &mo 1 | &mo 2 | &lt 1 ENTER | &none | &none | &mo 6 | &mo 6 | &none |
| Ctrl+ | &none | &mo 6 | &kp LEFT_WIN（物理 Ctrl は HID にそのまま伝わる） | &kp LEFT_ALT（物理 Ctrl は HID にそのまま伝わる） | &lt 2 SPACE | &lt 2 SPACE | &mo 1 | &mo 2 | &lt 1 ENTER | &none | &none | &mo 6 | &mo 6 | &none |

### SYMBOL レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 0 (top wing) | (outer)<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | (outer)<br>`&none` |  |  |
| 単発タップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| ダブルタップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| Shift+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| Ctrl+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| ■ Row 1 (QWERTY 上段) | (outer)<br>`&none` | Q<br>`&kp N1` | W<br>`&kp N2` | E<br>`&kp N3` | R<br>`&kp N4` | T<br>`&kp N5` | Y<br>`&kp N6` | U<br>`&kp N7` | I<br>`&kp N8` | O<br>`&kp N9` | P<br>`&kp N0` | (outer)<br>`&none` |  |  |
| 単発タップ | &none | &kp N1 | &kp N2 | &kp N3 | &kp N4 | &kp N5 | &kp N6 | &kp N7 | &kp N8 | &kp N9 | &kp N0 | &none |  |  |
| ダブルタップ | &none | &kp N1（tap-dance 未定義、連打） | &kp N2（tap-dance 未定義、連打） | &kp N3（tap-dance 未定義、連打） | &kp N4（tap-dance 未定義、連打） | &kp N5（tap-dance 未定義、連打） | &kp N6（tap-dance 未定義、連打） | &kp N7（tap-dance 未定義、連打） | &kp N8（tap-dance 未定義、連打） | &kp N9（tap-dance 未定義、連打） | &kp N0（tap-dance 未定義、連打） | &none |  |  |
| Shift+ | &none | &kp N1（物理 Shift は HID にそのまま伝わる） | &kp N2（物理 Shift は HID にそのまま伝わる） | &kp N3（物理 Shift は HID にそのまま伝わる） | &kp N4（物理 Shift は HID にそのまま伝わる） | &kp N5（物理 Shift は HID にそのまま伝わる） | &kp N6（物理 Shift は HID にそのまま伝わる） | &kp N7（物理 Shift は HID にそのまま伝わる） | &kp N8（物理 Shift は HID にそのまま伝わる） | &kp N9（物理 Shift は HID にそのまま伝わる） | &kp N0（物理 Shift は HID にそのまま伝わる） | &none |  |  |
| Ctrl+ | &none | &kp N1（物理 Ctrl は HID にそのまま伝わる） | &kp N2（物理 Ctrl は HID にそのまま伝わる） | &kp N3（物理 Ctrl は HID にそのまま伝わる） | &kp N4（物理 Ctrl は HID にそのまま伝わる） | &kp N5（物理 Ctrl は HID にそのまま伝わる） | &kp N6（物理 Ctrl は HID にそのまま伝わる） | &kp N7（物理 Ctrl は HID にそのまま伝わる） | &kp N8（物理 Ctrl は HID にそのまま伝わる） | &kp N9（物理 Ctrl は HID にそのまま伝わる） | &kp N0（物理 Ctrl は HID にそのまま伝わる） | &none |  |  |
| ■ Row 2 (home row) | (outer)<br>`&none` | A<br>`&mt LCTRL TAB` | S<br>`&kp GRAVE` | D<br>`&kp LEFT_BRACKET` | F<br>`&kp RIGHT_BRACKET` | G<br>`&kp DELETE` | (center L)<br>`&none` | (center R)<br>`&none` | H<br>`&kp BACKSPACE` | J<br>`&kp SEMICOLON` | K<br>`&kp SINGLE_QUOTE` | L<br>`&kp BACKSLASH` | MINUS<br>`&trans` | (outer)<br>`&none` |
| 単発タップ | &none | &mt LCTRL TAB | &kp GRAVE | &kp LEFT_BRACKET | &kp RIGHT_BRACKET | &kp DELETE | &none | &none | &kp BACKSPACE | &kp SEMICOLON | &kp SINGLE_QUOTE | &kp BACKSLASH | &trans | &none |
| ダブルタップ | &none | &mt LCTRL TAB（連打） | &kp GRAVE（tap-dance 未定義、連打） | &kp LEFT_BRACKET（tap-dance 未定義、連打） | &kp RIGHT_BRACKET（tap-dance 未定義、連打） | &kp DELETE（tap-dance 未定義、連打） | &none | &none | &kp BACKSPACE（tap-dance 未定義、連打） | &kp SEMICOLON（tap-dance 未定義、連打） | &kp SINGLE_QUOTE（tap-dance 未定義、連打） | &kp BACKSLASH（tap-dance 未定義、連打） | &trans | &none |
| Shift+ | &none | &mt LCTRL TAB | &kp GRAVE（物理 Shift は HID にそのまま伝わる） | &kp LEFT_BRACKET（物理 Shift は HID にそのまま伝わる） | &kp RIGHT_BRACKET（物理 Shift は HID にそのまま伝わる） | &kp DELETE（物理 Shift は HID にそのまま伝わる） | &none | &none | &kp BACKSPACE（物理 Shift は HID にそのまま伝わる） | &kp SEMICOLON（物理 Shift は HID にそのまま伝わる） | &kp SINGLE_QUOTE（物理 Shift は HID にそのまま伝わる） | &kp BACKSLASH（物理 Shift は HID にそのまま伝わる） | &trans | &none |
| Ctrl+ | &none | &mt LCTRL TAB | &kp GRAVE（物理 Ctrl は HID にそのまま伝わる） | &kp LEFT_BRACKET（物理 Ctrl は HID にそのまま伝わる） | &kp RIGHT_BRACKET（物理 Ctrl は HID にそのまま伝わる） | &kp DELETE（物理 Ctrl は HID にそのまま伝わる） | &none | &none | &kp BACKSPACE（物理 Ctrl は HID にそのまま伝わる） | &kp SEMICOLON（物理 Ctrl は HID にそのまま伝わる） | &kp SINGLE_QUOTE（物理 Ctrl は HID にそのまま伝わる） | &kp BACKSLASH（物理 Ctrl は HID にそのまま伝わる） | &trans | &none |
| ■ Row 3 (Z row) | (outer)<br>`&none` | Z<br>`&mt LEFT_SHIFT ESCAPE` | X<br>`&none` | C<br>`&none` | V<br>`&none` | B<br>`&none` | (center L)<br>`&none` | (center R)<br>`&none` | N<br>`&none` | M<br>`&kp EQUAL` | COMMA<br>`&trans` | PERIOD<br>`&trans` | SLASH<br>`&trans` | (outer)<br>`&none` |
| 単発タップ | &none | &mt LEFT_SHIFT ESCAPE | &none | &none | &none | &none | &none | &none | &none | &kp EQUAL | &trans | &trans | &trans | &none |
| ダブルタップ | &none | &mt LEFT_SHIFT ESCAPE（連打） | &none | &none | &none | &none | &none | &none | &none | &kp EQUAL（tap-dance 未定義、連打） | &trans | &trans | &trans | &none |
| Shift+ | &none | &mt LEFT_SHIFT ESCAPE | &none | &none | &none | &none | &none | &none | &none | &kp EQUAL（物理 Shift は HID にそのまま伝わる） | &trans | &trans | &trans | &none |
| Ctrl+ | &none | &mt LEFT_SHIFT ESCAPE | &none | &none | &none | &none | &none | &none | &none | &kp EQUAL（物理 Ctrl は HID にそのまま伝わる） | &trans | &trans | &trans | &none |
| ■ Row 4 (thumb) | (outer)<br>`&none` | mo6 (outer)<br>`&none` | LEFT_WIN<br>`&trans` | LEFT_ALT<br>`&trans` | lt2 SPACE<br>`&lt 3 SPACE` | lt2 SPACE<br>`&lt 3 SPACE` | (mo1 center)<br>`&none` | (mo2 center)<br>`&mo 3` | lt1 ENTER<br>`&none` | (none)<br>`&none` | (none)<br>`&none` | mo6<br>`&trans` | mo6 (outer)<br>`&none` | (outer)<br>`&none` |
| 単発タップ | &none | &none | &trans | &trans | &lt 3 SPACE | &lt 3 SPACE | &none | &mo 3 | &none | &none | &none | &trans | &none | &none |
| ダブルタップ | &none | &none | &trans | &trans | &lt 3 SPACE（連打） | &lt 3 SPACE（連打） | &none | &mo 3 | &none | &none | &none | &trans | &none | &none |
| Shift+ | &none | &none | &trans | &trans | &lt 3 SPACE | &lt 3 SPACE | &none | &mo 3 | &none | &none | &none | &trans | &none | &none |
| Ctrl+ | &none | &none | &trans | &trans | &lt 3 SPACE | &lt 3 SPACE | &none | &mo 3 | &none | &none | &none | &trans | &none | &none |

### VIM_NORMAL_1 レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 0 (top wing) | (outer)<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | (outer)<br>`&none` |  |  |
| 単発タップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| ダブルタップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| Shift+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| Ctrl+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| ■ Row 1 (QWERTY 上段) | (outer)<br>`&none` | Q<br>`&mm_vim_q` | W<br>`&mm_vim_w` | E<br>`&kp LC(RIGHT)` | R<br>`&mm_vim_ctrl_r` | T<br>`&none` | Y<br>`&mm_vim_shift_y` | U<br>`&mm_vim_ctrl_u` | I<br>`&none` | O<br>`&mm_vim_shift_o` | P<br>`&kp LC(V)` | (outer)<br>`&none` |  |  |
| 単発タップ | &none | mm_vim_q[0] → &kp ESCAPE | mm_vim_w[0] → &kp LC(RIGHT) | &kp LC(RIGHT) | mm_vim_ctrl_r[0] → &none | &none | mm_vim_shift_y[0] → td_vim_y[0] → &kp LC(C) | mm_vim_ctrl_u[0] → &kp LC(Z) | &none | mm_vim_shift_o[0] → macro_vim_o | &kp LC(V) | &none |  |  |
| ダブルタップ | &none | mm_vim_q[0] → &kp ESCAPE（tap-dance 未定義、連打） | mm_vim_w[0] → &kp LC(RIGHT)（tap-dance 未定義、連打） | &kp LC(RIGHT)（tap-dance 未定義、連打） | mm_vim_ctrl_r[0] → &none | &none | mm_vim_shift_y[0] → td_vim_y[1] → macro_vim_yy | mm_vim_ctrl_u[0] → &kp LC(Z)（tap-dance 未定義、連打） | &none | mm_vim_shift_o[0] → macro_vim_o（連打） | &kp LC(V)（tap-dance 未定義、連打） | &none |  |  |
| Shift+ | &none | mm_vim_q[1] (Shift 検知) → &kp LC(Q) | mm_vim_w[0] (Shift は本 mod-morph 検知外) → &kp LC(RIGHT)（物理 Shift は HID にそのまま伝わる） | &kp LC(RIGHT)（物理 Shift は HID にそのまま伝わる） | mm_vim_ctrl_r[0] (Shift は本 mod-morph 検知外) → &none | &none | mm_vim_shift_y[1] (Shift 検知) → macro_vim_shift_y | mm_vim_ctrl_u[0] (Shift は本 mod-morph 検知外) → &kp LC(Z)（物理 Shift は HID にそのまま伝わる） | &none | mm_vim_shift_o[1] (Shift 検知) → macro_vim_shift_o | &kp LC(V)（物理 Shift は HID にそのまま伝わる） | &none |  |  |
| Ctrl+ | &none | mm_vim_q[0] (Ctrl は本 mod-morph 検知外) → &kp ESCAPE（物理 Ctrl は HID にそのまま伝わる） | mm_vim_w[1] (Ctrl 検知) → &kp LC(BACKSPACE) | &kp LC(RIGHT)（物理 Ctrl は HID にそのまま伝わる） | mm_vim_ctrl_r[1] (Ctrl 検知) → &kp LC(Y) | &none | mm_vim_shift_y[0] (Ctrl は本 mod-morph 検知外) → td_vim_y[0] (tap-dance は mods 検知なし) → &kp LC(C)（物理 Ctrl は HID にそのまま伝わる） | mm_vim_ctrl_u[1] (Ctrl 検知) → &kp PAGE_UP | &none | mm_vim_shift_o[0] (Ctrl は本 mod-morph 検知外) → macro_vim_o | &kp LC(V)（物理 Ctrl は HID にそのまま伝わる） | &none |  |  |
| ■ Row 2 (home row) | (outer)<br>`&none` | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&mm_vim_ctrl_then_shift_d` | F<br>`&none` | G<br>`&mm_vim_g` | (center L)<br>`&none` | (center R)<br>`&none` | H<br>`&kp LEFT` | J<br>`&mm_vim_j` | K<br>`&kp UP_ARROW` | L<br>`&kp RIGHT` | MINUS<br>`&kp RCTRL` | (outer)<br>`&none` |
| 単発タップ | &none | &kp LCTRL | &none | mm_vim_ctrl_then_shift_d[0] → mm_vim_shift_d[0] → td_vim_d[0] → &none | &none | mm_vim_g[0] → td_vim_g[0] → &none | &none | &none | &kp LEFT | mm_vim_j[0] → &kp DOWN | &kp UP_ARROW | &kp RIGHT | &kp RCTRL | &none |
| ダブルタップ | &none | &kp LCTRL（tap-dance 未定義、連打） | &none | mm_vim_ctrl_then_shift_d[0] → mm_vim_shift_d[0] → td_vim_d[1] → macro_vim_dd | &none | mm_vim_g[0] → td_vim_g[1] → &kp LC(HOME) | &none | &none | &kp LEFT（tap-dance 未定義、連打） | mm_vim_j[0] → &kp DOWN（tap-dance 未定義、連打） | &kp UP_ARROW（tap-dance 未定義、連打） | &kp RIGHT（tap-dance 未定義、連打） | &kp RCTRL（tap-dance 未定義、連打） | &none |
| Shift+ | &none | &kp LCTRL（物理 Shift は HID にそのまま伝わる） | &none | mm_vim_ctrl_then_shift_d[0] (Shift は本 mod-morph 検知外) → mm_vim_shift_d[1] (Shift 検知) → macro_vim_shift_d | &none | mm_vim_g[1] (Shift 検知) → &kp LC(END) | &none | &none | &kp LEFT（物理 Shift は HID にそのまま伝わる） | mm_vim_j[1] (Shift 検知) → macro_vim_join | &kp UP_ARROW（物理 Shift は HID にそのまま伝わる） | &kp RIGHT（物理 Shift は HID にそのまま伝わる） | &kp RCTRL（物理 Shift は HID にそのまま伝わる） | &none |
| Ctrl+ | &none | &kp LCTRL（物理 Ctrl は HID にそのまま伝わる） | &none | mm_vim_ctrl_then_shift_d[1] (Ctrl 検知) → &kp PAGE_DOWN | &none | mm_vim_g[0] (Ctrl は本 mod-morph 検知外) → td_vim_g[0] (tap-dance は mods 検知なし) → &none | &none | &none | &kp LEFT（物理 Ctrl は HID にそのまま伝わる） | mm_vim_j[0] (Ctrl は本 mod-morph 検知外) → &kp DOWN（物理 Ctrl は HID にそのまま伝わる） | &kp UP_ARROW（物理 Ctrl は HID にそのまま伝わる） | &kp RIGHT（物理 Ctrl は HID にそのまま伝わる） | &kp RCTRL（物理 Ctrl は HID にそのまま伝わる） | &none |
| ■ Row 3 (Z row) | (outer)<br>`&none` | Z<br>`&kp LEFT_SHIFT` | X<br>`&kp DELETE` | C<br>`&none` | V<br>`&mm_vim_v` | B<br>`&kp LC(LEFT)` | (center L)<br>`&none` | (center R)<br>`&none` | N<br>`&mm_vim_n` | M<br>`&none` | COMMA<br>`&none` | PERIOD<br>`&none` | SLASH<br>`&kp RIGHT_SHIFT` | (outer)<br>`&none` |
| 単発タップ | &none | &kp LEFT_SHIFT | &kp DELETE | &none | mm_vim_v[0] → &to 8 | &kp LC(LEFT) | &none | &none | mm_vim_n[0] → &kp F3 | &none | &none | &none | &kp RIGHT_SHIFT | &none |
| ダブルタップ | &none | &kp LEFT_SHIFT（tap-dance 未定義、連打） | &kp DELETE（tap-dance 未定義、連打） | &none | mm_vim_v[0] → &to 8 | &kp LC(LEFT)（tap-dance 未定義、連打） | &none | &none | mm_vim_n[0] → &kp F3（tap-dance 未定義、連打） | &none | &none | &none | &kp RIGHT_SHIFT（tap-dance 未定義、連打） | &none |
| Shift+ | &none | &kp LEFT_SHIFT（物理 Shift は HID にそのまま伝わる） | &kp DELETE（物理 Shift は HID にそのまま伝わる） | &none | mm_vim_v[1] (Shift 検知) → macro_vim_v_line | &kp LC(LEFT)（物理 Shift は HID にそのまま伝わる） | &none | &none | mm_vim_n[1] (Shift 検知) → &kp LS(F3) | &none | &none | &none | &kp RIGHT_SHIFT（物理 Shift は HID にそのまま伝わる） | &none |
| Ctrl+ | &none | &kp LEFT_SHIFT（物理 Ctrl は HID にそのまま伝わる） | &kp DELETE（物理 Ctrl は HID にそのまま伝わる） | &none | mm_vim_v[0] (Ctrl は本 mod-morph 検知外) → &to 8 | &kp LC(LEFT)（物理 Ctrl は HID にそのまま伝わる） | &none | &none | mm_vim_n[0] (Ctrl は本 mod-morph 検知外) → &kp F3（物理 Ctrl は HID にそのまま伝わる） | &none | &none | &none | &kp RIGHT_SHIFT（物理 Ctrl は HID にそのまま伝わる） | &none |
| ■ Row 4 (thumb) | (outer)<br>`&none` | mo6 (outer)<br>`&none` | LEFT_WIN<br>`&trans` | LEFT_ALT<br>`&trans` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | (mo1 center)<br>`&mo 3` | (mo2 center)<br>`&none` | lt1 ENTER<br>`&lt 3 ENTER` | (none)<br>`&none` | (none)<br>`&none` | mo6<br>`&trans` | mo6 (outer)<br>`&none` | (outer)<br>`&none` |
| 単発タップ | &none | &none | &trans | &trans | &none | &none | &mo 3 | &none | &lt 3 ENTER | &none | &none | &trans | &none | &none |
| ダブルタップ | &none | &none | &trans | &trans | &none | &none | &mo 3 | &none | &lt 3 ENTER（連打） | &none | &none | &trans | &none | &none |
| Shift+ | &none | &none | &trans | &trans | &none | &none | &mo 3 | &none | &lt 3 ENTER | &none | &none | &trans | &none | &none |
| Ctrl+ | &none | &none | &trans | &trans | &none | &none | &mo 3 | &none | &lt 3 ENTER | &none | &none | &trans | &none | &none |

### VIM_NORMAL_2 レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 0 (top wing) | (outer)<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | (outer)<br>`&none` |  |  |
| 単発タップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| ダブルタップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| Shift+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| Ctrl+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| ■ Row 1 (QWERTY 上段) | (outer)<br>`&none` | Q<br>`&none` | W<br>`&none` | E<br>`&none` | R<br>`&mm_vim_shift_4` | T<br>`&none` | Y<br>`&mm_vim_shift_6` | U<br>`&none` | I<br>`&none` | O<br>`&none` | P<br>`&kp HOME` | (outer)<br>`&none` |  |  |
| 単発タップ | &none | &none | &none | &none | mm_vim_shift_4[0] → &none | &none | mm_vim_shift_6[0] → &none | &none | &none | &none | &kp HOME | &none |  |  |
| ダブルタップ | &none | &none | &none | &none | mm_vim_shift_4[0] → &none | &none | mm_vim_shift_6[0] → &none | &none | &none | &none | &kp HOME（tap-dance 未定義、連打） | &none |  |  |
| Shift+ | &none | &none | &none | &none | mm_vim_shift_4[1] (Shift 検知) → &kp END | &none | mm_vim_shift_6[1] (Shift 検知) → &kp HOME | &none | &none | &none | &kp HOME（物理 Shift は HID にそのまま伝わる） | &none |  |  |
| Ctrl+ | &none | &none | &none | &none | mm_vim_shift_4[0] (Ctrl は本 mod-morph 検知外) → &none | &none | mm_vim_shift_6[0] (Ctrl は本 mod-morph 検知外) → &none | &none | &none | &none | &kp HOME（物理 Ctrl は HID にそのまま伝わる） | &none |  |  |
| ■ Row 2 (home row) | (outer)<br>`&none` | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&none` | F<br>`&none` | G<br>`&none` | (center L)<br>`&none` | (center R)<br>`&none` | H<br>`&kp LEFT` | J<br>`&none` | K<br>`&none` | L<br>`&none` | MINUS<br>`&kp RCTRL` | (outer)<br>`&none` |
| 単発タップ | &none | &kp LCTRL | &none | &none | &none | &none | &none | &none | &kp LEFT | &none | &none | &none | &kp RCTRL | &none |
| ダブルタップ | &none | &kp LCTRL（tap-dance 未定義、連打） | &none | &none | &none | &none | &none | &none | &kp LEFT（tap-dance 未定義、連打） | &none | &none | &none | &kp RCTRL（tap-dance 未定義、連打） | &none |
| Shift+ | &none | &kp LCTRL（物理 Shift は HID にそのまま伝わる） | &none | &none | &none | &none | &none | &none | &kp LEFT（物理 Shift は HID にそのまま伝わる） | &none | &none | &none | &kp RCTRL（物理 Shift は HID にそのまま伝わる） | &none |
| Ctrl+ | &none | &kp LCTRL（物理 Ctrl は HID にそのまま伝わる） | &none | &none | &none | &none | &none | &none | &kp LEFT（物理 Ctrl は HID にそのまま伝わる） | &none | &none | &none | &kp RCTRL（物理 Ctrl は HID にそのまま伝わる） | &none |
| ■ Row 3 (Z row) | (outer)<br>`&none` | Z<br>`&kp LEFT_SHIFT` | X<br>`&none` | C<br>`&none` | V<br>`&none` | B<br>`&none` | (center L)<br>`&none` | (center R)<br>`&none` | N<br>`&none` | M<br>`&none` | COMMA<br>`&none` | PERIOD<br>`&none` | SLASH<br>`&kp RIGHT_SHIFT` | (outer)<br>`&none` |
| 単発タップ | &none | &kp LEFT_SHIFT | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &kp RIGHT_SHIFT | &none |
| ダブルタップ | &none | &kp LEFT_SHIFT（tap-dance 未定義、連打） | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &kp RIGHT_SHIFT（tap-dance 未定義、連打） | &none |
| Shift+ | &none | &kp LEFT_SHIFT（物理 Shift は HID にそのまま伝わる） | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &kp RIGHT_SHIFT（物理 Shift は HID にそのまま伝わる） | &none |
| Ctrl+ | &none | &kp LEFT_SHIFT（物理 Ctrl は HID にそのまま伝わる） | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &kp RIGHT_SHIFT（物理 Ctrl は HID にそのまま伝わる） | &none |
| ■ Row 4 (thumb) | (outer)<br>`&none` | mo6 (outer)<br>`&none` | LEFT_WIN<br>`&trans` | LEFT_ALT<br>`&trans` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | (mo1 center)<br>`&none` | (mo2 center)<br>`&none` | lt1 ENTER<br>`&none` | (none)<br>`&none` | (none)<br>`&none` | mo6<br>`&trans` | mo6 (outer)<br>`&none` | (outer)<br>`&none` |
| 単発タップ | &none | &none | &trans | &trans | &none | &none | &none | &none | &none | &none | &none | &trans | &none | &none |
| ダブルタップ | &none | &none | &trans | &trans | &none | &none | &none | &none | &none | &none | &none | &trans | &none | &none |
| Shift+ | &none | &none | &trans | &trans | &none | &none | &none | &none | &none | &none | &none | &trans | &none | &none |
| Ctrl+ | &none | &none | &trans | &trans | &none | &none | &none | &none | &none | &none | &none | &trans | &none | &none |

### MOUSE レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 0 (top wing) | (outer)<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | (outer)<br>`&none` |  |  |
| 単発タップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| ダブルタップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| Shift+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| Ctrl+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| ■ Row 1 (QWERTY 上段) | (outer)<br>`&none` | Q<br>`&none` | W<br>`&none` | E<br>`&none` | R<br>`&none` | T<br>`&none` | Y<br>`&none` | U<br>`&none` | I<br>`&none` | O<br>`&none` | P<br>`&none` | (outer)<br>`&none` |  |  |
| 単発タップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| ダブルタップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| Shift+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| Ctrl+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| ■ Row 2 (home row) | (outer)<br>`&none` | A<br>`&none` | S<br>`&none` | D<br>`&none` | F<br>`&none` | G<br>`&none` | (center L)<br>`&none` | (center R)<br>`&none` | H<br>`&none` | J<br>`&none` | K<br>`&mo 5` | L<br>`&none` | MINUS<br>`&none` | (outer)<br>`&none` |
| 単発タップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &mo 5 | &none | &none | &none |
| ダブルタップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &mo 5 | &none | &none | &none |
| Shift+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &mo 5 | &none | &none | &none |
| Ctrl+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &mo 5 | &none | &none | &none |
| ■ Row 3 (Z row) | (outer)<br>`&none` | Z<br>`&none` | X<br>`&none` | C<br>`&none` | V<br>`&none` | B<br>`&none` | (center L)<br>`&none` | (center R)<br>`&none` | N<br>`&none` | M<br>`&none` | COMMA<br>`&none` | PERIOD<br>`&none` | SLASH<br>`&none` | (outer)<br>`&none` |
| 単発タップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| ダブルタップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| Shift+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| Ctrl+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| ■ Row 4 (thumb) | (outer)<br>`&none` | mo6 (outer)<br>`&none` | LEFT_WIN<br>`&none` | LEFT_ALT<br>`&none` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | (mo1 center)<br>`&none` | (mo2 center)<br>`&none` | lt1 ENTER<br>`&none` | (none)<br>`&none` | (none)<br>`&none` | mo6<br>`&none` | mo6 (outer)<br>`&none` | (outer)<br>`&none` |
| 単発タップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| ダブルタップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| Shift+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| Ctrl+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |

### SCROLL レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 0 (top wing) | (outer)<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | (outer)<br>`&none` |  |  |
| 単発タップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| ダブルタップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| Shift+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| Ctrl+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| ■ Row 1 (QWERTY 上段) | (outer)<br>`&none` | Q<br>`&none` | W<br>`&none` | E<br>`&none` | R<br>`&none` | T<br>`&none` | Y<br>`&none` | U<br>`&none` | I<br>`&none` | O<br>`&none` | P<br>`&none` | (outer)<br>`&none` |  |  |
| 単発タップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| ダブルタップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| Shift+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| Ctrl+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| ■ Row 2 (home row) | (outer)<br>`&none` | A<br>`&none` | S<br>`&none` | D<br>`&none` | F<br>`&none` | G<br>`&none` | (center L)<br>`&none` | (center R)<br>`&none` | H<br>`&none` | J<br>`&mkp MB1` | K<br>`&none` | L<br>`&mkp MB2` | MINUS<br>`&none` | (outer)<br>`&none` |
| 単発タップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &mkp MB1 | &none | &mkp MB2 | &none | &none |
| ダブルタップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &mkp MB1 | &none | &mkp MB2 | &none | &none |
| Shift+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &mkp MB1 | &none | &mkp MB2 | &none | &none |
| Ctrl+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &mkp MB1 | &none | &mkp MB2 | &none | &none |
| ■ Row 3 (Z row) | (outer)<br>`&none` | Z<br>`&none` | X<br>`&none` | C<br>`&none` | V<br>`&none` | B<br>`&none` | (center L)<br>`&none` | (center R)<br>`&none` | N<br>`&none` | M<br>`&mkp MB4` | COMMA<br>`&none` | PERIOD<br>`&mkp MB5` | SLASH<br>`&none` | (outer)<br>`&none` |
| 単発タップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &mkp MB4 | &none | &mkp MB5 | &none | &none |
| ダブルタップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &mkp MB4 | &none | &mkp MB5 | &none | &none |
| Shift+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &mkp MB4 | &none | &mkp MB5 | &none | &none |
| Ctrl+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &mkp MB4 | &none | &mkp MB5 | &none | &none |
| ■ Row 4 (thumb) | (outer)<br>`&none` | mo6 (outer)<br>`&none` | LEFT_WIN<br>`&none` | LEFT_ALT<br>`&none` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | (mo1 center)<br>`&none` | (mo2 center)<br>`&none` | lt1 ENTER<br>`&none` | (none)<br>`&none` | (none)<br>`&none` | mo6<br>`&none` | mo6 (outer)<br>`&none` | (outer)<br>`&none` |
| 単発タップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| ダブルタップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| Shift+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| Ctrl+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |

### FUNCTION レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 0 (top wing) | (outer)<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | (outer)<br>`&none` |  |  |
| 単発タップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| ダブルタップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| Shift+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| Ctrl+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| ■ Row 1 (QWERTY 上段) | (outer)<br>`&none` | Q<br>`&kp F1` | W<br>`&kp F2` | E<br>`&kp F3` | R<br>`&kp F4` | T<br>`&kp F5` | Y<br>`&kp F6` | U<br>`&kp F7` | I<br>`&kp F8` | O<br>`&kp F9` | P<br>`&kp F10` | (outer)<br>`&none` |  |  |
| 単発タップ | &none | &kp F1 | &kp F2 | &kp F3 | &kp F4 | &kp F5 | &kp F6 | &kp F7 | &kp F8 | &kp F9 | &kp F10 | &none |  |  |
| ダブルタップ | &none | &kp F1（tap-dance 未定義、連打） | &kp F2（tap-dance 未定義、連打） | &kp F3（tap-dance 未定義、連打） | &kp F4（tap-dance 未定義、連打） | &kp F5（tap-dance 未定義、連打） | &kp F6（tap-dance 未定義、連打） | &kp F7（tap-dance 未定義、連打） | &kp F8（tap-dance 未定義、連打） | &kp F9（tap-dance 未定義、連打） | &kp F10（tap-dance 未定義、連打） | &none |  |  |
| Shift+ | &none | &kp F1（物理 Shift は HID にそのまま伝わる） | &kp F2（物理 Shift は HID にそのまま伝わる） | &kp F3（物理 Shift は HID にそのまま伝わる） | &kp F4（物理 Shift は HID にそのまま伝わる） | &kp F5（物理 Shift は HID にそのまま伝わる） | &kp F6（物理 Shift は HID にそのまま伝わる） | &kp F7（物理 Shift は HID にそのまま伝わる） | &kp F8（物理 Shift は HID にそのまま伝わる） | &kp F9（物理 Shift は HID にそのまま伝わる） | &kp F10（物理 Shift は HID にそのまま伝わる） | &none |  |  |
| Ctrl+ | &none | &kp F1（物理 Ctrl は HID にそのまま伝わる） | &kp F2（物理 Ctrl は HID にそのまま伝わる） | &kp F3（物理 Ctrl は HID にそのまま伝わる） | &kp F4（物理 Ctrl は HID にそのまま伝わる） | &kp F5（物理 Ctrl は HID にそのまま伝わる） | &kp F6（物理 Ctrl は HID にそのまま伝わる） | &kp F7（物理 Ctrl は HID にそのまま伝わる） | &kp F8（物理 Ctrl は HID にそのまま伝わる） | &kp F9（物理 Ctrl は HID にそのまま伝わる） | &kp F10（物理 Ctrl は HID にそのまま伝わる） | &none |  |  |
| ■ Row 2 (home row) | (outer)<br>`&none` | A<br>`&none` | S<br>`&sys_reset` | D<br>`&none` | F<br>`&none` | G<br>`&none` | (center L)<br>`&none` | (center R)<br>`&none` | H<br>`&none` | J<br>`&none` | K<br>`&none` | L<br>`&sys_reset` | MINUS<br>`&none` | (outer)<br>`&none` |
| 単発タップ | &none | &none | &sys_reset | &none | &none | &none | &none | &none | &none | &none | &none | &sys_reset | &none | &none |
| ダブルタップ | &none | &none | &sys_reset | &none | &none | &none | &none | &none | &none | &none | &none | &sys_reset | &none | &none |
| Shift+ | &none | &none | &sys_reset | &none | &none | &none | &none | &none | &none | &none | &none | &sys_reset | &none | &none |
| Ctrl+ | &none | &none | &sys_reset | &none | &none | &none | &none | &none | &none | &none | &none | &sys_reset | &none | &none |
| ■ Row 3 (Z row) | (outer)<br>`&none` | Z<br>`&none` | X<br>`&none` | C<br>`&none` | V<br>`&none` | B<br>`&bootloader` | (center L)<br>`&none` | (center R)<br>`&none` | N<br>`&bootloader` | M<br>`&none` | COMMA<br>`&none` | PERIOD<br>`&none` | SLASH<br>`&none` | (outer)<br>`&none` |
| 単発タップ | &none | &none | &none | &none | &none | &bootloader | &none | &none | &bootloader | &none | &none | &none | &none | &none |
| ダブルタップ | &none | &none | &none | &none | &none | &bootloader | &none | &none | &bootloader | &none | &none | &none | &none | &none |
| Shift+ | &none | &none | &none | &none | &none | &bootloader | &none | &none | &bootloader | &none | &none | &none | &none | &none |
| Ctrl+ | &none | &none | &none | &none | &none | &bootloader | &none | &none | &bootloader | &none | &none | &none | &none | &none |
| ■ Row 4 (thumb) | (outer)<br>`&none` | mo6 (outer)<br>`&none` | LEFT_WIN<br>`&none` | LEFT_ALT<br>`&none` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | (mo1 center)<br>`&none` | (mo2 center)<br>`&none` | lt1 ENTER<br>`&none` | (none)<br>`&none` | (none)<br>`&none` | mo6<br>`&none` | mo6 (outer)<br>`&none` | (outer)<br>`&none` |
| 単発タップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| ダブルタップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| Shift+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| Ctrl+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |

### BLUETOOTH レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 0 (top wing) | (outer)<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | (outer)<br>`&none` |  |  |
| 単発タップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| ダブルタップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| Shift+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| Ctrl+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| ■ Row 1 (QWERTY 上段) | (outer)<br>`&none` | Q<br>`&bt BT_SEL 0` | W<br>`&bt BT_SEL 1` | E<br>`&bt BT_SEL 2` | R<br>`&bt BT_SEL 3` | T<br>`&bt BT_SEL 4` | Y<br>`&none` | U<br>`&out OUT_USB` | I<br>`&none` | O<br>`&none` | P<br>`&none` | (outer)<br>`&none` |  |  |
| 単発タップ | &none | &bt BT_SEL 0 | &bt BT_SEL 1 | &bt BT_SEL 2 | &bt BT_SEL 3 | &bt BT_SEL 4 | &none | &out OUT_USB | &none | &none | &none | &none |  |  |
| ダブルタップ | &none | &bt BT_SEL 0 | &bt BT_SEL 1 | &bt BT_SEL 2 | &bt BT_SEL 3 | &bt BT_SEL 4 | &none | &out OUT_USB | &none | &none | &none | &none |  |  |
| Shift+ | &none | &bt BT_SEL 0 | &bt BT_SEL 1 | &bt BT_SEL 2 | &bt BT_SEL 3 | &bt BT_SEL 4 | &none | &out OUT_USB | &none | &none | &none | &none |  |  |
| Ctrl+ | &none | &bt BT_SEL 0 | &bt BT_SEL 1 | &bt BT_SEL 2 | &bt BT_SEL 3 | &bt BT_SEL 4 | &none | &out OUT_USB | &none | &none | &none | &none |  |  |
| ■ Row 2 (home row) | (outer)<br>`&none` | A<br>`&bt BT_CLR_ALL` | S<br>`&none` | D<br>`&none` | F<br>`&none` | G<br>`&none` | (center L)<br>`&none` | (center R)<br>`&none` | H<br>`&none` | J<br>`&none` | K<br>`&none` | L<br>`&none` | MINUS<br>`&none` | (outer)<br>`&none` |
| 単発タップ | &none | &bt BT_CLR_ALL | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| ダブルタップ | &none | &bt BT_CLR_ALL | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| Shift+ | &none | &bt BT_CLR_ALL | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| Ctrl+ | &none | &bt BT_CLR_ALL | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| ■ Row 3 (Z row) | (outer)<br>`&none` | Z<br>`&none` | X<br>`&none` | C<br>`&bt BT_CLR` | V<br>`&none` | B<br>`&out OUT_BLE` | (center L)<br>`&none` | (center R)<br>`&none` | N<br>`&none` | M<br>`&none` | COMMA<br>`&none` | PERIOD<br>`&none` | SLASH<br>`&none` | (outer)<br>`&none` |
| 単発タップ | &none | &none | &none | &bt BT_CLR | &none | &out OUT_BLE | &none | &none | &none | &none | &none | &none | &none | &none |
| ダブルタップ | &none | &none | &none | &bt BT_CLR | &none | &out OUT_BLE | &none | &none | &none | &none | &none | &none | &none | &none |
| Shift+ | &none | &none | &none | &bt BT_CLR | &none | &out OUT_BLE | &none | &none | &none | &none | &none | &none | &none | &none |
| Ctrl+ | &none | &none | &none | &bt BT_CLR | &none | &out OUT_BLE | &none | &none | &none | &none | &none | &none | &none | &none |
| ■ Row 4 (thumb) | (outer)<br>`&none` | mo6 (outer)<br>`&none` | LEFT_WIN<br>`&none` | LEFT_ALT<br>`&none` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | (mo1 center)<br>`&none` | (mo2 center)<br>`&none` | lt1 ENTER<br>`&none` | (none)<br>`&none` | (none)<br>`&none` | mo6<br>`&none` | mo6 (outer)<br>`&none` | (outer)<br>`&none` |
| 単発タップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| ダブルタップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| Shift+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| Ctrl+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |

### VIM_VISUAL レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 0 (top wing) | (outer)<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | top wing<br>`&none` | (outer)<br>`&none` |  |  |
| 単発タップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| ダブルタップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| Shift+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| Ctrl+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |  |  |
| ■ Row 1 (QWERTY 上段) | (outer)<br>`&none` | Q<br>`&macro_vim_visual_exit` | W<br>`&kp LS(LC(RIGHT))` | E<br>`&kp LS(LC(RIGHT))` | R<br>`&none` | T<br>`&none` | Y<br>`&none` | U<br>`&none` | I<br>`&none` | O<br>`&none` | P<br>`&macro_vim_visual_p` | (outer)<br>`&none` |  |  |
| 単発タップ | &none | macro_vim_visual_exit | &kp LS(LC(RIGHT)) | &kp LS(LC(RIGHT)) | &none | &none | &none | &none | &none | &none | macro_vim_visual_p | &none |  |  |
| ダブルタップ | &none | macro_vim_visual_exit（連打） | &kp LS(LC(RIGHT))（tap-dance 未定義、連打） | &kp LS(LC(RIGHT))（tap-dance 未定義、連打） | &none | &none | &none | &none | &none | &none | macro_vim_visual_p（連打） | &none |  |  |
| Shift+ | &none | macro_vim_visual_exit | &kp LS(LC(RIGHT))（物理 Shift は HID にそのまま伝わる） | &kp LS(LC(RIGHT))（物理 Shift は HID にそのまま伝わる） | &none | &none | &none | &none | &none | &none | macro_vim_visual_p | &none |  |  |
| Ctrl+ | &none | macro_vim_visual_exit | &kp LS(LC(RIGHT))（物理 Ctrl は HID にそのまま伝わる） | &kp LS(LC(RIGHT))（物理 Ctrl は HID にそのまま伝わる） | &none | &none | &none | &none | &none | &none | macro_vim_visual_p | &none |  |  |
| ■ Row 2 (home row) | (outer)<br>`&none` | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&macro_vim_visual_cut` | F<br>`&none` | G<br>`&mm_vim_visual_g` | (center L)<br>`&none` | (center R)<br>`&none` | H<br>`&kp LS(LEFT)` | J<br>`&kp LS(DOWN)` | K<br>`&kp LS(UP)` | L<br>`&kp LS(RIGHT)` | MINUS<br>`&kp RCTRL` | (outer)<br>`&none` |
| 単発タップ | &none | &kp LCTRL | &none | macro_vim_visual_cut | &none | mm_vim_visual_g[0] → td_vim_visual_g[0] → &none | &none | &none | &kp LS(LEFT) | &kp LS(DOWN) | &kp LS(UP) | &kp LS(RIGHT) | &kp RCTRL | &none |
| ダブルタップ | &none | &kp LCTRL（tap-dance 未定義、連打） | &none | macro_vim_visual_cut（連打） | &none | mm_vim_visual_g[0] → td_vim_visual_g[1] → &kp LS(LC(HOME)) | &none | &none | &kp LS(LEFT)（tap-dance 未定義、連打） | &kp LS(DOWN)（tap-dance 未定義、連打） | &kp LS(UP)（tap-dance 未定義、連打） | &kp LS(RIGHT)（tap-dance 未定義、連打） | &kp RCTRL（tap-dance 未定義、連打） | &none |
| Shift+ | &none | &kp LCTRL（物理 Shift は HID にそのまま伝わる） | &none | macro_vim_visual_cut | &none | mm_vim_visual_g[1] (Shift 検知) → &kp LS(LC(END)) | &none | &none | &kp LS(LEFT)（物理 Shift は HID にそのまま伝わる） | &kp LS(DOWN)（物理 Shift は HID にそのまま伝わる） | &kp LS(UP)（物理 Shift は HID にそのまま伝わる） | &kp LS(RIGHT)（物理 Shift は HID にそのまま伝わる） | &kp RCTRL（物理 Shift は HID にそのまま伝わる） | &none |
| Ctrl+ | &none | &kp LCTRL（物理 Ctrl は HID にそのまま伝わる） | &none | macro_vim_visual_cut | &none | mm_vim_visual_g[0] (Ctrl は本 mod-morph 検知外) → td_vim_visual_g[0] (tap-dance は mods 検知なし) → &none | &none | &none | &kp LS(LEFT)（物理 Ctrl は HID にそのまま伝わる） | &kp LS(DOWN)（物理 Ctrl は HID にそのまま伝わる） | &kp LS(UP)（物理 Ctrl は HID にそのまま伝わる） | &kp LS(RIGHT)（物理 Ctrl は HID にそのまま伝わる） | &kp RCTRL（物理 Ctrl は HID にそのまま伝わる） | &none |
| ■ Row 3 (Z row) | (outer)<br>`&none` | Z<br>`&kp LEFT_SHIFT` | X<br>`&macro_vim_visual_cut` | C<br>`&none` | V<br>`&macro_vim_visual_exit` | B<br>`&kp LS(LC(LEFT))` | (center L)<br>`&none` | (center R)<br>`&none` | N<br>`&kp F3` | M<br>`&none` | COMMA<br>`&none` | PERIOD<br>`&none` | SLASH<br>`&kp RIGHT_SHIFT` | (outer)<br>`&none` |
| 単発タップ | &none | &kp LEFT_SHIFT | macro_vim_visual_cut | &none | macro_vim_visual_exit | &kp LS(LC(LEFT)) | &none | &none | &kp F3 | &none | &none | &none | &kp RIGHT_SHIFT | &none |
| ダブルタップ | &none | &kp LEFT_SHIFT（tap-dance 未定義、連打） | macro_vim_visual_cut（連打） | &none | macro_vim_visual_exit（連打） | &kp LS(LC(LEFT))（tap-dance 未定義、連打） | &none | &none | &kp F3（tap-dance 未定義、連打） | &none | &none | &none | &kp RIGHT_SHIFT（tap-dance 未定義、連打） | &none |
| Shift+ | &none | &kp LEFT_SHIFT（物理 Shift は HID にそのまま伝わる） | macro_vim_visual_cut | &none | macro_vim_visual_exit | &kp LS(LC(LEFT))（物理 Shift は HID にそのまま伝わる） | &none | &none | &kp F3（物理 Shift は HID にそのまま伝わる） | &none | &none | &none | &kp RIGHT_SHIFT（物理 Shift は HID にそのまま伝わる） | &none |
| Ctrl+ | &none | &kp LEFT_SHIFT（物理 Ctrl は HID にそのまま伝わる） | macro_vim_visual_cut | &none | macro_vim_visual_exit | &kp LS(LC(LEFT))（物理 Ctrl は HID にそのまま伝わる） | &none | &none | &kp F3（物理 Ctrl は HID にそのまま伝わる） | &none | &none | &none | &kp RIGHT_SHIFT（物理 Ctrl は HID にそのまま伝わる） | &none |
| ■ Row 4 (thumb) | (outer)<br>`&none` | mo6 (outer)<br>`&none` | LEFT_WIN<br>`&none` | LEFT_ALT<br>`&none` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | (mo1 center)<br>`&none` | (mo2 center)<br>`&none` | lt1 ENTER<br>`&none` | (none)<br>`&none` | (none)<br>`&none` | mo6<br>`&none` | mo6 (outer)<br>`&none` | (outer)<br>`&none` |
| 単発タップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| ダブルタップ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| Shift+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |
| Ctrl+ | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none | &none |

