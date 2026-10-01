# zmk-keyboard-torabo-tsuki-lp

[torabo-tsuki LP](https://github.com/sekigon-gonnoc/torabo-tsuki-lp) 用の ZMK ファームウェアです。[zmk-config-LisM](https://github.com/ryo-aoki-pc/zmk-config-LisM) を基準に、キーマップ・conf・CI を他のキーボードと揃えています。

- マイコン: BLE Micro Pro Boost (`bmp_boost`)。乾電池 1 本で動き、電源スイッチがあります
- 構成: 右手側にトラックボール (PAW3222) を付け、右手側をセントラルにします。左手側にトラックボールを付ける構成と両手にトラックボールを付ける構成は、`build.yaml` のコメントを外すとビルドできます
- キーマップ: `config/keymap.keymap` (66 ポジション・L レイアウト)。LisM との配列差の吸収ルールはファイル冒頭のコメントにあります。物理配列は `config/info.json` (keymap-editor も使用)
- スクロール: 他のキーボード (1/16) と違い、`zip_scroll_scaler 1 1` と `CONFIG_ZMK_POINTING_SMOOTH_SCROLLING=y` (スムーズスクロール) で実機に合わせて調整しています
- キーマップは keymap-editor と ZMK Studio (`_studio` 版を書き込んだとき) でも編集できます

## キー割り当て一覧

各レイヤーのキー割り当ては [KEYMAP.html](KEYMAP.html) にまとめています。ブラウザでレンダリング表示する場合は以下のリンクから閲覧できます。

https://htmlpreview.github.io/?https://github.com/ryo-aoki-pc/zmk-keyboard-torabo-tsuki-lp/blob/custom/KEYMAP.html

## 命名規則（カスタムビヘイビア）

`config/keymap.keymap` の Macro / Tap Dance / Mod Morph は以下の規則で命名します。

- **構造**：`<prefix>_vim_<id>` 形式。`<prefix>` は `macro_`（マクロ）/ `td_`（タップダンス）/ `mm_`（モッドモーフ）。ノードラベル・ノード名・`label` を一致させ、`label` はラベルの大文字にする（例：`mm_vim_g` → `label = "MM_VIM_G"`）。
- **Mod Morph の `<id>`**：キーに直接割り当てるモーフは無修飾時の vim キーで命名（`mm_vim_d` `mm_vim_g` など）。ベースが `&none`（修飾時のみ動作）またはネスト用ヘルパーは、修飾＋キーストロークで命名する（`mm_vim_shift_4` `mm_vim_ctrl_r` `mm_vim_shift_d`）。

## 生成されるファームウェア一覧

| ファームウェア名 | 説明 |
| --- | --- |
| `torabo_tsuki_lp_left_peripheral.uf2` | 左側 ペリフェラル |
| `torabo_tsuki_lp_right_central.uf2` | 右側 セントラル (トラックボールあり) |
| `torabo_tsuki_lp_right_central_studio.uf2` | 右側 セントラル (トラックボールあり、ZMK Studio 対応) |
| `settings_reset-bmp_boost-zmk.uf2` | 設定リセット用 |

全エントリに `studio-rpc-usb-uart` スニペットを付けています。ブートローダへの切り替え (`CONFIG_ZMK_CDC_ACM_BOOTLOADER_TRIGGER`) に必要な USB シリアル (CDC-ACM) をこのスニペットが定義しているためで、ZMK Studio が有効になるのは `_studio` 版だけです。

## ファームウェアの書き込み

[zmk-config-keyboards](https://github.com/ryo-aoki-pc/zmk-config-keyboards) の `tools/flash-zmk.cmd` を使うと、最新のファームウェアのダウンロードから左右への書き込みまでを案内に沿って行えます。手動で書き込む場合は次のとおりです。

1. 電源スイッチを OFF にした状態で、USB ケーブルで PC につなぐ
2. `BLEMICROPRO` という名前のドライブが現れ、中に `INFO_UF2.TXT` があることを確認する
3. `.uf2` をドライブにコピーする。トラックボールがある右手側に `_central`、左手側に `_peripheral` を書き込む
4. USB ケーブルを抜き、電源スイッチを ON にしてから USB ケーブルを差し直すと、キーボードとして動作する

`settings_reset-bmp_boost-zmk.uf2` は、書き込んだあとに一度起動させる必要があります (スイッチ OFF → USB 接続 → 書き込み → USB を抜く → スイッチ ON → USB 再接続)。設定がリセットされたら、同じ手順で通常のファームウェアを書き込みます。

## ローカルビルド手順

GitHub Actions でのビルドは毎回 2〜3 分かかりますが、ローカル環境では 40 秒〜1 分で完了します (PC スペックによって前後します)。
キーマップを少し試したいだけでもローカルビルドなら素早く試行錯誤ができます。

### 必要なもの

- [Visual Studio Code](https://code.visualstudio.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- VS Code 拡張機能: [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### 手順

1. **準備**
   1. このリポジトリを PC に clone します。
   2. Docker Desktop を起動します。
   3. VS Code でこのフォルダを開きます。
   4. 右下に表示される「Reopen in Container (コンテナーで再度開く)」をクリックします (初回は環境構築に時間がかかります)。

2. **ビルド**

   VS Code のターミナルで以下のいずれかを実行します。

   > [!TIP]
   > ビルドは CPU コアを使って並列実行できます。並列数は自動で CPU コア数になりますが、
   > 環境変数 `PARALLEL` で指定することもできます (例: `PARALLEL=4 make all_p`)。

   | コマンド | 内容 |
   | --- | --- |
   | `make` | 全ファームウェアを並列ビルド (ZMK Studio 版を除く) |
   | `make all` | 全ファームウェアを逐次ビルド (ZMK Studio 版を除く) |
   | `make all_studio_p` | ZMK Studio 版も含めて並列ビルド |
   | `make all_studio` | ZMK Studio 版も含めて逐次ビルド |
   | `make single` | 一覧から番号を選んで 1 つだけビルド |
   | `make clean` | `firmware_builds/` を削除 |

   キーマップ変更だけを試すなら `torabo_tsuki_lp_right_central` のみで十分です。

3. **完成**

   `firmware_builds/` に `.uf2` が生成されます。これをキーボードに書き込みます。
