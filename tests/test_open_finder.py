#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import unittest

# 將 extension 目錄加入模組搜尋路徑
ext_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "OpenInFinder.popclipext"))
sys.path.insert(0, ext_dir)

from open_finder import sanitize_path

class TestOpenFinder(unittest.TestCase):
    def test_simple_absolute_path(self):
        path = "/Users/sunda/Documents/POPCLIP/"
        self.assertEqual(sanitize_path(path), "/Users/sunda/Documents/POPCLIP")

    def test_path_with_quotes(self):
        cases = [
            ('"/Users/sunda/Documents/POPCLIP/"', "/Users/sunda/Documents/POPCLIP"),
            ("'/Users/sunda/Documents/POPCLIP'", "/Users/sunda/Documents/POPCLIP"),
            ("`~/Documents/POPCLIP`", os.path.expanduser("~/Documents/POPCLIP")),
            ("“/Users/sunda/Documents/POPCLIP”", "/Users/sunda/Documents/POPCLIP"),
            ("<~/Documents/POPCLIP>", os.path.expanduser("~/Documents/POPCLIP")),
        ]
        for raw, expected in cases:
            self.assertEqual(sanitize_path(raw), expected)

    def test_file_url(self):
        cases = [
            ("file:///Users/sunda/Documents/POPCLIP/", "/Users/sunda/Documents/POPCLIP"),
            ("file:///Users/sunda/Documents%20Folder", "/Users/sunda/Documents Folder"),
        ]
        for raw, expected in cases:
            self.assertEqual(sanitize_path(raw), expected)

    def test_tilde_expansion(self):
        self.assertEqual(sanitize_path("~"), os.path.expanduser("~"))
        self.assertEqual(sanitize_path("~/Documents"), os.path.expanduser("~/Documents"))

    def test_escaped_spaces(self):
        self.assertEqual(
            sanitize_path(r"/Library/Application\ Support"),
            "/Library/Application Support"
        )

    def test_trailing_punctuation_strip(self):
        # 如果路徑後面接內文標點符號，但該路徑原本存在，自動剔除標點
        self.assertEqual(
            sanitize_path("/Users/sunda/Documents/POPCLIP."),
            "/Users/sunda/Documents/POPCLIP"
        )
        self.assertEqual(
            sanitize_path("/Users/sunda/Documents/POPCLIP,"),
            "/Users/sunda/Documents/POPCLIP"
        )

    def test_relative_path_resolution(self):
        # Documents/POPCLIP 在使用者家目錄下存在
        self.assertEqual(
            sanitize_path("Documents/POPCLIP"),
            os.path.join(os.path.expanduser("~"), "Documents/POPCLIP")
        )

if __name__ == "__main__":
    unittest.main()
