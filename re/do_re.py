#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_re.py
#Created Time:2019-07-20 08:49:03


import re


# 使用 r 前缀，不用考虑转义的问题
match_re = r'^\d{3}\-\d{3,8}$'


def main():
    str = input('Phone Num:')
    if re.match(match_re,str):
        print('match')
    else:
        print('Not match')

    # 分组，用 () 表示的就是要提取的分组 (group)
    pattern = r'^(\d{3})-(\d{3,8})$'
    m = re.match(pattern,str)
    # 原始字符串
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))

if __name__ == '__main__':
    main()


