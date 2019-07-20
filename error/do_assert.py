#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_assert.py
#Created Time:2019-07-18 03:30:01


def foo(s):
    n = int(s)
    # python -O  大写字母 O 可以关闭断言，加 -O 执行时，下面这句无效
    assert n!=0 ,'s:%d is zero'%n
    return 10-n

n =foo('0')
print(n)

