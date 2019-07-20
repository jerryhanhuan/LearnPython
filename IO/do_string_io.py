#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_string_io.py
#Created Time:2019-07-18 12:39:48


# 很多时候，数据读写不一定是文件，也可以在内存中读写
# StringIO 顾名思义就是在内存中读写 str

from io import StringIO

f = StringIO()

f.write('hello\nworld\n')

print(f.getvalue())




f= StringIO('Hello\nworld')

while True:
    data = f.readline()
    if data == '':
        break
    else:
        print(data.strip())














