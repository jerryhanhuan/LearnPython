#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 切片：L[start,end],包括 L[start],不包括 L[end]
# 可用于 list,tuple,str


L = [1,2,3,4,5]
s1 = L[0:3]
print(s1,'type is:',type(s1)) #[1, 2, 3] type is: <class 'list'>


t = (1,2,3,4,5)
s2 = t[0:3]
print(s2,'type is:',type(s2)) #(1, 2, 3) type is: <class 'tuple'>

s = '12345'
s3 = s[0:3]
print(s3,'type is:',type(s3)) #123 type is: <class 'str'>






