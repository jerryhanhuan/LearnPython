#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_re_split.py
#Created Time:2019-07-20 08:56:15


import re


def str_split():
    # split 无法识别连续的空格
    str = 'a b  c'.split(' ')
    print(str) #['a', 'b', '', 'c']

def re_str_split():
    str = 'a b  c'
    L = re.split(r'\s+',str)
    print(L) # ['a','b','c']

    str = 'a,b,c  d'
    L = re.split(r'[\s\,]+',str)
    print(L)

    str = 'a,b;; c  d'
    L = re.split(r'[\s\,\;]+',str)
    print(L)



def main():
    str_split()
    re_str_split()


if __name__ == '__main__':
    main()








