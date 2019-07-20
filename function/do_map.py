#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_map.py
#Created Time:2019-07-16 07:06:30


# map 接收两个参数，一个是函数，一个是 Iterable，map 将 函数作用到 序列的每一个元素，返回一个 Iterator


# eg1 f(x) = x^2 L=[1,2,3,4,5,6,7,8,9]


def f(x):
    return x * x

L = [1,2,3,4,5,6,7,8,9]

r = map(f,L)

#for n in r:
#    print(n)
#

L = list(r)
print(L) #[1, 4, 9, 16, 25, 36, 49, 64, 81]]




L = list(map(str,[1,2,3,4,5]))
print(L)#['1', '2', '3', '4', '5']

# pratice
# 把不规范的英文名字，开头大写，其余小写
# 例如，输入 jAck 变为 Jack

def normalize(name):
    return name.title()

L = ['aMy','jACk','bOB']

L = list(map(normalize,L))

print(L) #['Amy', 'Jack', 'Bob']
