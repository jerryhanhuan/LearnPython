#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_high_func.py
#Created Time:2019-07-16 07:01:42


# 函数可以是变量

def f1():
    print('Hello world!')

f = f1

f() #Hello world!


# 函数可以是参数

def power(n):
    return pow(n,2)


def f2(x,y,f):
    return f(x) + f(y)


n = f2(1,2,power) 
print(n) #5

