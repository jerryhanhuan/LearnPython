#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 元祖(tuple) 是一中有序列表,和list 很类似，但是 list 可被改变,tuple 不能被修改

# define a tuple witk ()
# empty tuple
t = ()
print('empty tuple len is:',len(t))

#define a tuple only with one element
# note not t1 = (1) ,must with ,

t1 = (1,)
print('t1 len is:',len(t1))

# tuple's element can not be changed and assigned 

t2 = (1,2,'hello')

# range 1
for item in t2:
    print('item:',item)

# range 2
for index in range(len(t2)):
    print('t2[%d]:'%(index),t2[index])



# tuple can not be assigned
# tuple' object does not support item assignment
#t2[0]=10


#but if tuple has an item is a list,list can not be changed

L = [1,10,100,1000]

t3 = ('I','Money',L)

for index in range(len(t3)):
    print('t3[%d]:'%(index),t3[index])

L.insert(0,0)
L.append(10000)

for index in range(len(t3)):
    print("t3[%d]:"%(index),t3[index])

