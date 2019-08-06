#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_list_str.py
#Created Time:2019-08-05 01:50:44


def listAllSubStr(s):
    sub = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
    print(sub)

if __name__ == '__main__':
    s = input('请输入一个字符串::')
    listAllSubStr(s)


