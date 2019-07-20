#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_reduce.py
#Created Time:2019-07-16 07:06:43


# reduce 把一个函数作用在一个序列上，这个函数必须接收 2 个 参数，reduce 把结果继续和序列的下一个元素做累计计算

# reduce(f,[x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)


# eg 对一个序列求和，就可以使用 reduce 实现

from functools import reduce


def add(x,y):
        return x + y


L = [1,2,3,4,5,6,7,8,9,10]

print(sum(L))


n = reduce(add,L)
print(n)


# 将[1,3,5,7,9] 变为 13579

L = [1,3,5,7,9]

def f1(x,y):
    return x * 10 + y

n = reduce(f1,L)
print(n) # 13579



# 将 字符串 '13579' 变为数字 13579

DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

def char2int(c):
        return DIGITS[c]



def str2int(s):
    return reduce(f1,map(char2int,s))


s = '12345'
n = str2int(s)
print(n) # 12345



#求序列每个元素的积

def multi(x,y):
        return x * y

def pord(L):
    return reduce(multi,L)

print('3 * 5 * 7 * 9 =',pord([3,5,7,9]))




#pratice 
#使用 map 和 reduce 将 字符串 '123.456' 变为 浮点数 123.456


def str2float(s):
    n = reduce(f1,map(char2int,s.replace('.','')))
    m = pow(10,len(s)-1-s.find('.'))
    return n/m

f = '1234.567'
f2 = str2float(f)
print(f2)













