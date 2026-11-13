#!/usr/bin/env python3
"""
mdBook Preprocessor: 将 LaTeX 风格数学公式替换为 MathJax 标准定界符。
"""

import json
import sys
import re

def replace_mathjax(text: str) -> str:
    """
    对单个章节的 Markdown 文本进行 MathJax 定界符替换。
    """
    # 1. 首先处理块级公式 $$ ... $$
    # 将 \\ 替换为 \\\\
    text = re.sub(r'\\\\', r'\\' * 4, text)
    # 使用 DOTALL 使 . 能匹配换行，非贪婪匹配
    text = re.sub(r'\$\$(.+?)\$\$', r'\\\\[\1\\\\]', text, flags=re.DOTALL)

    # 2. 处理行内公式 $ ... $
    # 使用负向断言 (?<!\$) 和 (?!\$) 确保不会匹配到 $$ 的一部分
    text = re.sub(r'(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)', r'\\\\(\1\\\\)', text)

    return text


def process_book(book: dict) -> dict:
    def process_item(item):
        # 如果是 Chapter 类型，处理其 content
        if isinstance(item, dict) and item.get("Chapter"):
            chapter = item["Chapter"]
            if "content" in chapter and isinstance(chapter["content"], str):
                chapter["content"] = replace_mathjax(chapter["content"])
            # 递归处理子章节
            if "sub_items" in chapter:
                for sub_item in chapter["sub_items"]:
                    process_item(sub_item)
        # 也可以处理 Separator 或 PartTitle，此处忽略
        return item

    for item in book['items']:
        process_item(item)

    return book


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "supports":
        sys.exit(0)

    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.stderr.write("Error: 无法解析 stdin 中的 JSON 数据。\n")
        sys.exit(1)

    context, book = data[0], data[1]
    modified_book = process_book(book)

    json.dump(modified_book, sys.stdout)


if __name__ == "__main__":
    main()
