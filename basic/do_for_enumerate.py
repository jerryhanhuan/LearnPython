#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_for_enumerate.py
#Created Time:2019-07-22 02:46:28


L = ['Alice','Bob','Tom']

# 普通 for 方法,同时输出 索引和值

i = 0
for element in L:
    print('L[%d]:%s'%(i,element))
    i += 1

# enumerate 方法

for i, element in enumerate(L):
    print('L[%d]:%s'%(i,element))




