#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_sys.py
#Created Time:2019-07-17 03:39:42

'a test module'

__author__ = 'yudf'


import sys


def main():
    # sys 模块有一个 argv 变量，用 list 存储了命令行的所有参数
    argv = sys.argv
    if len(argv) == 1:
        print('%s'%argv[0])
    elif len(argv) == 2:
        print('%s %s'%(argv[0],argv[1]))
    else:
        print('too mant args')

if __name__ == '__main__':
    main()

