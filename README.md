# PopClip Extension: Open in Finder (在 Finder 中打開)

[![PopClip Extension](https://img.shields.io/badge/PopClip-Extension-blue.svg)](https://www.popclip.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Release](https://img.shields.io/github/v/release/houtacheng/popclip-open-in-finder?color=green)](https://github.com/houtacheng/popclip-open-in-finder/releases)

A macOS [PopClip](https://www.popclip.app/) extension to open highlighted folder paths directly in Finder, or reveal files, with a single click.

專為 macOS **PopClip** 設計的高效外掛。選取任何資料夾或檔案路徑文字後，一鍵直接在 Finder 中開啟該資料夾並置頂顯示。完全採用原生 JavaScript 開發，零外部依賴。

---

## ✨ Features / 功能特色

- **Direct Folder Access (直接進入資料夾)**:
  - Select folder paths like `/Users/sunda/Documents/POPCLIP/`, click the icon, and Finder instantly opens and focuses the target directory.
  - 選取資料夾路徑，點擊按鈕直接在 Finder 中開啟該目錄並置頂。
- **File Reveal (檔案高亮定位)**:
  - If a file path is selected (e.g. `/path/to/file.txt`), it reveals and selects the item in its enclosing folder.
  - 若選取的是檔案，則在 Finder 中顯示並自動高亮選取該檔案。
- **Robust Path Cleaning (強大路徑相容性)**:
  - **Tilde expansion**: Supports `~`, `~/Documents`, etc.
  - **Quote handling**: Cleans double quotes `"/path"`, single quotes `'~/path'`, backticks `` `path` ``, angle brackets `<path>`, or smart quotes `“/path”`.
  - **`file://` URIs**: Automatically strips schema and URL-decodes percent encoding (spaces `%20`, unicode).
  - **Shell-escaped spaces**: Handles `/My\ Folder/` correctly.
  - **Trailing punctuation**: Strips trailing punctuation marks (e.g. `.` or `,`) if included by mistake in prose.
- **Copy Path Shortcut via ⌥ Option Key (快捷鍵複製路徑)**:
  - Hold `⌥ Option` when clicking to copy the clean, normalized path to your clipboard.
  - 按住 `⌥ Option` 鍵點選，直接複製清理並正規化後的純淨路徑至剪貼簿。
- **Pure JavaScript & Zero Dependencies (純 JavaScript 無任何外部依賴)**:
  - Built natively with PopClip's sandboxed JavaScript API. Fast, lightweight, and requires no external tools or runtime.

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

## 🧪 Testing / 單元測試

Run the unit tests:

```bash
node tests/test_open_finder.js
```

---

## 📄 License / 授權條款

This project is licensed under the [MIT License](LICENSE).

---

## Changelog

- 2026-10-19: Re-implemented as pure JavaScript action for official PopClip Extensions Directory compliance and instant execution.
- 2026-10-12: Initial release.
