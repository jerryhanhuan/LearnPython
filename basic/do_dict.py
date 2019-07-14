#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# dict is map key => value { k1:v1,k2:v2}
# define a dict with {} 

# define an empty dict
d1 = {}


# key 不会重复,key 唯一性
# 无序
# 查找和插入的速度极快，不会随着key的增加而变慢
# 需要占用较多内存，dict 是用空间来换取时间的一种方法
# key 必须是不可变对象，string,int 是不可变的,list 是可变的



d2 = {'jack':100,'lilei':100,'hanmm':100,'bob':99}

print(d2)



# 使用 in 判断 key 是否在dict 中
sname = 'polly'

if sname in d2:
    print('%s'%(sname),'in class')
else:
    print('%s'%(sname),'not in class')


# dict.get() 方法判断 key 是否在 dict 中
# D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None

if d2.get(sname):
    print('%s'%(sname),'in class')
else:
    print('%s'%(sname),'not in class')



