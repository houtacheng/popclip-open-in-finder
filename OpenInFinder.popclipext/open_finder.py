#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PopClip Extension: Open in Finder (在 Finder 中打開)
開啟選取的檔案或資料夾路徑。支援家目錄、引號、跳脫空格、file:// 與各類終端機快捷操作。
"""

import os
import sys
import urllib.parse
import subprocess

def show_notification(message: str, title: str = "在 Finder 中打開") -> None:
    """使用 AppleScript 顯示 macOS 系統通知（防止參數注入）"""
    script = (
        'on run argv\n'
        '    display notification (item 1 of argv) with title (item 2 of argv)\n'
        'end run'
    )
    try:
        subprocess.run(["osascript", "-e", script, message, title], check=False)
    except Exception:
        pass

def sanitize_path(raw: str) -> str:
    """清理與解析路徑字串"""
    if not raw:
        return ""

    p = raw.strip()

    # 去除前後可能包裹的引號與括號
    strip_chars = "\"'`<>[]()«»“”‘’"
    changed = True
    while changed and p:
        before = p
        p = p.strip(strip_chars).strip()
        changed = (before != p)

    if not p:
        return ""

    # 處理 file:// 協議格式
    if p.startswith("file://"):
        p = p[7:]
        # file:///Users/... 截取後為 /Users/...
        p = urllib.parse.unquote(p)
    elif "%" in p:
        try:
            p = urllib.parse.unquote(p)
        except Exception:
            pass

    # 處理終端機跳脫空格（例如 /My\ Documents/ -> /My Documents/）
    p = p.replace(r"\ ", " ")

    # 展開環境變數（如 $HOME、${HOME}）
    p = os.path.expandvars(p)

    # 展開家目錄波浪號（~ 或 ~/path）
    if p == "~" or p.startswith("~/"):
        p = os.path.expanduser(p)

    # 去除路徑結尾因內文標點符號誤入的點號或逗號（若原始不存在）
    if not os.path.exists(p) and len(p) > 1:
        for punct in (".", ",", ";", ":", "!", "?"):
            if p.endswith(punct):
                candidate = p[:-1]
                if os.path.exists(candidate) or candidate.endswith("/"):
                    p = candidate
                    break

    # 若為相對路徑且目前目錄找不到，嘗試檢查 ~/ 目錄下是否存在
    if not os.path.isabs(p) and not os.path.exists(p):
        home_candidate = os.path.join(os.path.expanduser("~"), p)
        if os.path.exists(home_candidate):
            p = home_candidate

    # 正規化路徑（處理 /./ 與 /../）
    if os.path.isabs(p):
        p = os.path.normpath(p)

    return p

def open_in_terminal(target_dir: str, terminal_choice: str) -> None:
    """在指定的終端機中開啟目標資料夾"""
    app_map = {
        "iTerm": "iTerm",
        "Warp": "Warp",
        "Ghostty": "Ghostty",
        "Terminal": "Terminal"
    }
    app_name = app_map.get(terminal_choice, "Terminal")
    subprocess.run(["open", "-a", app_name, target_dir], check=False)

def main() -> None:
    raw_text = os.environ.get("POPCLIP_TEXT", "").strip()
    if not raw_text:
        sys.exit(0)

    target_path = sanitize_path(raw_text)
    if not target_path:
        sys.exit(0)

    # 檢查 Option 按鍵狀態（PopClip 修飾鍵 Option 的 bitmask 為 524288）
    modifier_flags = int(os.environ.get("POPCLIP_MODIFIER_FLAGS", "0") or "0")
    option_pressed = bool(modifier_flags & 524288)

    terminal_app = os.environ.get("POPCLIP_OPTION_TERMINALAPP", "Terminal")

    # 判斷目標路徑是否存在
    if not os.path.exists(target_path):
        show_notification(f"找不到指定的路徑：{target_path}", "在 Finder 中打開")
        sys.exit(1)

    if option_pressed:
        # 按住 Option 鍵：在終端機中開啟該資料夾
        target_dir = target_path if os.path.isdir(target_path) else os.path.dirname(target_path)
        open_in_terminal(target_dir, terminal_app)
    else:
        # 一般點選：
        # 若是資料夾，直接進入該資料夾
        if os.path.isdir(target_path):
            subprocess.run(["open", "-a", "Finder", target_path], check=False)
        else:
            # 若是檔案，在 Finder 中選取並顯示該檔案（Reveal in Finder）
            subprocess.run(["open", "-R", target_path], check=False)

    sys.exit(0)

if __name__ == "__main__":
    main()
