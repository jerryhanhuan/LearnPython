#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
列表生成式练习
'''

# 列表生成的方法

L = list(range(1,10))
print(L) #[1, 2, 3, 4, 5, 6, 7, 8, 9]


L = []
for x in range(1,10):
    L.append(x * x)

print(L) #[1, 4, 9, 16, 25, 36, 49, 64, 81]

#以上两种使用列表生成式更加简单

L = [x for x in range(1,10)]
print('L is:',L) #L is: [1, 2, 3, 4, 5, 6, 7, 8, 9]

L = [x*x for x in range(1,10)]
print('L is:',L) #L is: [1, 4, 9, 16, 25, 36, 49, 64, 81]


# 列表生成式 还可以使用条件判断

L = [x * x for x in range(1,10) if x % 2 == 0]
print(L) #[4, 16, 36, 64]

# 还可以使用两层循环，生成全排列


L = [x + y for x in 'ABC' for y in 'XYZ']
print(L) # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']



# 实例
# 使用列表生成式,列出当前目录所有的目录和文件

import os

L = [d for d in os.listdir('.')]
print(L) #


# for 循环可以同时使用两个甚至多个变量
# 例如,dict 的 items 可以同时迭代 key 和 value

d = {'yudf':'12','yexb':'13','mohz':'14'}
for k,v in d.items():
    print('%s:%s'%(k,v))

# 列表生成式也可以使用两个变量来生成 list

L = [x + '=' + y for x,y in d.items()]
print(L)  #


# 把一个 list 中的所有字符串变为小写

L = ['HELLO','NICE','TO','MEET','YOU']

L = [ s.lower() for s in L]

print(L) #

# 如果 list 中 还包含 数字，数字类型没有 lower() 方法
# 可以使用内置的 isinstance 函数来判断 列表内元素是否是 字符串类型

L = ['HELLO','NICE','TO','MEET',14,15.6,{'goob':1234}]

L = [s.lower() for s in L if isinstance(s,str)]
print(L)#












