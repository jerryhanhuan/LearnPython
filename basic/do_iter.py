#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_iter.py
#Created Time:2019-07-16 05:48:33


#可直接作用于 for 循环的数据类型有以下几种:
#
#一类是 集合数据类型,如 list、tuple、dict、set、str 等
#一类是 generator，包括 生成器 和 带 yield 的 generator funciton
#这样可直接用于 for 循环的对象统称为 可迭代对象 Iterable
#可使用 isinstance() 判断一个对象是否是 Iterable 对象


from collections import Iterable
from collections import Iterator

L = [1,2,3]
t = (1,2,3)
d = {'x':1,'b':2,'c':3}
s = {1,2,3,4}
s1 = 'hello'

g = (x for x in range(1,10))


def Fibonacci(count):
    n,a,b = 0,0,1
    while n < count:
        yield b
        a,b = b,a+b
        n += 1
  
f = Fibonacci(10)


print('============ Iterable =============')

print(isinstance(L,Iterable))# False 
print(isinstance(t,Iterable))# False
print(isinstance(d,Iterable))# False
print(isinstance(s,Iterable))# False
print(isinstance(s1,Iterable))# False
print(isinstance(g,Iterable))# True
print(isinstance(f,Iterable))# True




# generator 不但可以作用于 for 循环，还可以被 next 调用，直到最后抛出 StopIteration 错误表示 无法继续返回下一个值了
# !!! 可以被 next() 调用并不断返回下一个值得对象称为 迭代器 : Iterator
# generator 是 Iterator ，但是 list tuple set str dict 虽然是 Iterable,但不是 Iterator
# Iterator 的计算是惰性的，只有在需要返回下一个数据时它才会计算，Iterator 甚至可以表示一个无限大的数据流，例如全体自然数，list 是不可能存储全体自然数的

print('=========== Iterator ============')

print(isinstance(L,Iterator))# True 
print(isinstance(t,Iterator))# True
print(isinstance(d,Iterator))# True
print(isinstance(s,Iterator))# True
print(isinstance(s1,Iterator))# True
print(isinstance(g,Iterator))# True
print(isinstance(f,Iterator))# True




# 将 Iterable 变为 Iterator，使用 iter() 函数
print('========== iter ===============')

print(isinstance(iter(L),Iterator))# True 
print(isinstance(iter(t),Iterator))# True
print(isinstance(iter(d),Iterator))# True
print(isinstance(iter(s),Iterator))# True
print(isinstance(iter(s1),Iterator))# True
print(isinstance(g,Iterator))# True
print(isinstance(f,Iterator))# True




