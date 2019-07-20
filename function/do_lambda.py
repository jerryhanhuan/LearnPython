#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_lambda.py
#Created Time:2019-07-16 14:12:37


# 匿名函数

# python 对匿名函数提供了有限支持

# 以 map 为例

def f(x):
    return x * x

L = list(map(f,[1,2,3,4,5]))
print(L)

# 用匿名函数
# 用关键字 lambda 表示匿名函数,冒号前面的 x 表示 参数
# 匿名函数只能有一个表达式，不用写 return，表达式的结果就是返回值

L = list(map(lambda x:x*x,[1,2,3,4,5]))
print(L)


# 可以把匿名函数赋值给一个变量

f1 = lambda x:x*x
print(f1(10))



# 也可以将匿名函数作为返回值返回


def build(x,y):
    return lambda:x*x + y*y

f2 = build(1,2)

print(f2()) #5



def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd,range(1,20)))
print(L) #[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# 使用匿名函数

L = list(filter(lambda x:x%2 == 1,range(1,20)))
print(L)#[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]



