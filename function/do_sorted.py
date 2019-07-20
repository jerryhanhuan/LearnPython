#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_sorted.py
#Created Time:2019-07-16 09:06:04


#sorted(iterable, /, *, key=None, reverse=False))



# 默认从小到达排序

L = [9,4,5,1,23,0,7]

print(sorted(L))



# 使用 key 实现自定义排序

# 按绝对值 排序


L = [-5,-7,-1,-9,4,8,10]

print(sorted(L))
print(sorted(L,key=abs))


# 字符串排序，忽略大小写


L = ['Bob','John','Jack','amy','cook']

print(sorted(L,key=str.lower))

# 反向排序

print(sorted(L,key=str.lower,reverse=True))




# 自定义排序

L = [('Bob',80),('Adam',90),('Jack',77),('Alice',56)]

# 按照名字排序

def by_name(t):
    return t[0].lower()

def by_score(t):
    return t[1]


print(sorted(L,key=by_name))

print(sorted(L,key=by_score))







