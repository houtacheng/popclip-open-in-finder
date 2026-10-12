# PopClip Extension: Open in Finder (在 Finder 中打開)

[![PopClip Extension](https://img.shields.io/badge/PopClip-Extension-blue.svg)](https://www.popclip.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Release](https://img.shields.io/github/v/release/houtacheng/popclip-open-in-finder?color=green)](https://github.com/houtacheng/popclip-open-in-finder/releases)

A macOS [PopClip](https://www.popclip.app/) extension to open highlighted folder paths directly in Finder, or reveal files, with a single click.

專為 macOS **PopClip** 設計的高效外掛。選取任何資料夾或檔案路徑文字後，一鍵直接在 Finder 中打開該資料夾並置頂顯示。

---

## ✨ Features / 功能特色

- **Direct Folder Access (直接進入資料夾)**:
  - Select folder paths like `/Users/sunda/Documents/POPCLIP/`, click the icon, and Finder instantly opens and focuses the target directory.
  - 選取資料夾路徑，點擊按鈕直接在 Finder 中開啟該目錄並置頂。
- **File Reveal (檔案高亮定位)**:
  - If a file path is selected (e.g. `/path/to/file.txt`), it reveals and selects the item in its enclosing folder (`open -R`).
  - 若選取的是檔案，則在 Finder 中顯示並自動高亮選取該檔案。
- **Robust Path Cleaning (強大路徑相容性)**:
  - **Tilde expansion**: Supports `~`, `~/Documents`, etc.
  - **Quote handling**: Cleans double quotes `"/path"`, single quotes `'~/path'`, backticks `` `path` ``, angle brackets `<path>`, or smart quotes `“/path”`.
  - **`file://` URIs**: Automatically strips schema and URL-decodes percent encoding (spaces `%20`, unicode).
  - **Shell-escaped spaces**: Handles `/My\ Folder/` correctly.
  - **Trailing punctuation**: Strips trailing punctuation marks (e.g. `.` or `,`) if included by mistake in prose.
- **Terminal Shortcut via ⌥ Option Key (快捷鍵終端機)**:
  - Hold `⌥ Option` when clicking to open the folder in your preferred terminal emulator (`Terminal`, `iTerm`, `Warp`, or `Ghostty`).
  - 按住 `⌥ Option` 鍵點選，直接在自訂終端機應用中開啟該資料夾。
- **Helpful Notification (友善提示)**:
  - If the path does not exist on disk, a native macOS notification is displayed.

---

## 🚀 Installation / 安裝方式

### Method 1: Download Release Package / 下載套件安裝 (Recommended)

1. Go to the [Releases](https://github.com/houtacheng/popclip-open-in-finder/releases) page.
2. Download **`OpenInFinder.popclipextz`**.
3. Double-click the file to install it directly into PopClip!

### Method 2: Manual Installation / 手動安裝

1. Clone or download this repository.
2. Double-click the `OpenInFinder.popclipext` folder or run:
   ```bash
   open OpenInFinder.popclipextz
   ```

---

## ⚙️ Options / 設定選項

In PopClip's extension settings for **Open in Finder**, you can configure:

- **Option Key Terminal (Option 鍵輔助終端機)**:
  - `Terminal` (macOS default, 預設)
  - `iTerm`
  - `Warp`
  - `Ghostty`

---

## 🧪 Testing / 單元測試

Run the unit tests:

```bash
python3 tests/test_open_finder.py
```

---

## 📄 License / 授權條款

This project is licensed under the [MIT License](LICENSE).
