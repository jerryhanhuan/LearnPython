#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_scope.py
#Created Time:2019-07-17 04:29:32

# 正常函数和变量名是 public 的，可以直接被引用，比如：abc,x123,PI 等
# 以双下划线开头结尾的，类似 __xxx__ 这样的变量是特殊变量，可以直接被引用，但是有特殊用途
# __author__ , __name__ 就是特殊变量
# 我们自己的变量一般不要用这种变量名

# 类似 _xxx 和 __xxx 这样的函数和变量就是 private，不应该被直接引用，比如， _abc, __abc 等
# private 函数和变量 不应该被直接引用，而不是不能被直接引用，是因为 python 并没有一种方法可以完全限制访问 private 函数 或者 变量
# 但是，从编程习惯上不应该直接引用 private 函数或变量



def _private_1(name):
    return 'hello,%s'%name

def _private_2(name):
    return 'hi,%s'%name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)



