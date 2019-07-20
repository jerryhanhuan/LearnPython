#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_filter.py
#Created Time:2019-07-16 08:28:59


# filter 类似 map，接收一个 函数f,和一个序列 作为参数
# filter 和 map 不同的是， filter() 把传入的函数一次作用于每个元素，然后根据返回值是True 还是 False 决定保留还是丢弃该元素
# True 保留，False 丢弃
# filter 返回的是一个 Iterator ,也就是一个惰性序列，强迫 filter() 完成计算结果，需要使用 list() 获取所有结果并返回 list

# 筛选奇数

def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd,[1,2,3,4,5,6,7,8,9]))
print(L)



# 用 filter 求素数
# 使用埃式筛法


# 构造从3开始奇数序列
# 这是一个生成器，无限序列
def _odd_iter():
    n = 3
    yield n
    while True:
        n += 2
        yield n


def _divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_divisible(n),it)

# prime 是一个无限序列，调用时需要设置一个退出循环的条件

for n in primes():
    if n < 1000:
        print(n)
    else:
        break










