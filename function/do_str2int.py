#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_str2int.py
#Created Time:2019-07-23 06:04:04


from functools import reduce


DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

def char2int(c):
    return DIGITS[c]

def str2int(s):
    return reduce(lambda x, y:x*10+y, map(char2int,s)) 


if __name__ == '__main__':
    s = input('请输入一串数字:')
    num = str2int(s)
    print(num)




