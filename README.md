# PopClip Extension: 在 Finder 中打開 (Open in Finder)

在 macOS 上選取任何資料夾或檔案路徑文字後，透過 PopClip 一鍵直接在 Finder 中開啟該目錄或定位檔案。

---

## ✨ 功能特色

1. **直接進入資料夾**：
   - 選取資料夾路徑（例如 `/Users/sunda/Documents/POPCLIP/`），點擊按鈕立即在 Finder 中打開該資料夾並置頂顯示。
2. **檔案自動定位**：
   - 若選取的是檔案路徑（如 `/Users/sunda/Documents/POPCLIP/README.md`），則會在 Finder 中開啟其所在資料夾並高亮選取該檔案（Reveal in Finder）。
3. **強大路徑相容性**：
   - **波浪號家目錄**：支援 `~/Documents`、`~` 等格式，自動展開為使用者家目錄。
   - **引號包覆**：無論是雙引號 `"/path"`、單引號 `'~/path'`、反引號 `` `path` ``、書名號或中文引號 `“/path”`，均能智慧去除。
   - **`file://` 協議**：支援瀏覽器或郵件複製的 `file:///Users/...`，並自動處理 URL 百分比編碼（例如 `%20` 空格與中文字元）。
   - **終端機跳脫空格**：支援 `/Applications/App\ Store.app` 等跳脫空格路徑。
   - **常見內文標點隔離**：選取路徑時若不小心連帶選取句尾的逗號、句號（如 `見 /Users/sunda/Downloads/.`），會自動剔除並正確辨識。
4. **快捷鍵輔助功能（Option + 點選）**：
   - 按住鍵盤 `⌥ Option` 鍵點擊按鈕，可直接在終端機應用中開啟該目錄！
   - 支援在 PopClip 外掛設定中選擇：`Terminal`（內建終端機）、`iTerm`、`Warp` 或 `Ghostty`。
5. **友善錯誤回饋**：
   - 若選取的路徑在硬碟中不存在，會透過 macOS 系統通知提示「找不到指定的路徑」，PopClip 則會顯示輕微晃動動畫。

---

## 📦 安裝方式

1. 進入此專案目錄：`popclip-open-in-finder`。
2. 雙擊 **`OpenInFinder.popclipextz`**（或直接雙擊 `OpenInFinder.popclipext` 資料夾）。
3. PopClip 會彈出安裝確認視窗，點擊「安裝」即可使用！

> 💡 **提示**：若未出現圖示，請確認 PopClip 設定中的「動作（Actions）」分頁，確認「在 Finder 中打開」已勾選啟用。

---

## ⚙️ 外掛設定選項

在外掛設定面板中，可調整：
- **Option 鍵輔助終端機**：
  - `Terminal`（macOS 內建，預設值）
  - `iTerm`
  - `Warp`
  - `Ghostty`

---

## 📁 專案檔案結構

```
popclip-open-in-finder/
├── LICENSE
├── README.md
├── popclip-directory.yaml
├── OpenInFinder.popclipext/
│   ├── Config.yaml          # PopClip 外掛設定與正規表達式
│   ├── open_finder.sh       # 啟動腳本
│   └── open_finder.py       # 核心路徑清理與執行邏輯
├── OpenInFinder.popclipextz  # 已打包完成的外掛安裝包
└── tests/
    └── test_open_finder.py  # 單元測試
```

---

## 🧪 執行測試

在終端機中執行：

```bash
python3 tests/test_open_finder.py
```

---

## 📄 授權條款

MIT License
