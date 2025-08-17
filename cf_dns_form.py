#!/usr/bin/env python3
"""
将 CSV 文件按行处理并生成带序号的管道分隔文本（跳过首行）：
- 先跳过输入文件的第一行（通常是表头）
- 跳过空行（只含空白的行也会被删除）
- 将行内所有 ',' 替换为 '|'
- 在每行最前面添加行号（从1开始），格式为 |<行号>|内容|
- 每行首尾添加 '|'
- 将结果写入输出 TXT 文件

用法:
    python convert_csv_to_pipe_numbered_skipheader.py input.csv output.txt
"""

import sys
import io
import os

def convert_file(in_path, out_path, encoding='utf-8'):
    if not os.path.isfile(in_path):
        raise FileNotFoundError(f"输入文件不存在: {in_path}")

    written_count = 0
    with io.open(in_path, 'r', encoding=encoding, newline='') as fin, \
         io.open(out_path, 'w', encoding=encoding, newline='') as fout:
        # 跳过第一行（表头）
        try:
            next(fin)
        except StopIteration:
            # 文件为空，直接返回
            return 0

        line_no = 0
        for raw_line in fin:
            # 去掉末尾换行符
            line = raw_line.rstrip('\r\n')
            # 跳过空行（只含空白也视为空行）
            if line.strip() == '':
                continue
            line_no += 1
            # 将逗号替换为竖线
            line = line.replace(',', '|')
            # 构造输出行：|<序号>|<内容>|
            out_line = '|' + str(line_no) + '|' + line + '|'
            fout.write(out_line + '\n')
            written_count += 1

    return written_count

def main():
    if len(sys.argv) != 3:
        print("用法: python convert_csv_to_pipe_numbered_skipheader.py input.csv output.txt")
        sys.exit(1)

    in_path = sys.argv[1]
    out_path = sys.argv[2]

    try:
        count = convert_file(in_path, out_path)
        print(f"已生成: {out_path} ，共写入 {count} 行（首行已跳过，空行已跳过）。")
    except Exception as e:
        print("处理文件时出错:", e)
        sys.exit(2)

if __name__ == '__main__':
    main()