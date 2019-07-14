#!/usr/bin/env python3
# -*- coding: utf-8 -*-




# for var in sequence

# list

L = [1,2,3,4,5]

for item in L:
    print(item)

print(' --------- list end ---------')

# tuple
t = (10,20,30,40,50)

for item in t:
    print(item)

print(' --------- tuple end ---------')


# str

s = 'hello,world'

for item in s:
    print(item)


print(' --------- str end ---------')
    

# dict,没有下标，默认情况下迭代 key
# for key in dict
# 要迭代 value 使用: for v in d.values()
# 同时迭代 key 和 value for k,v in d.items()

d = {'a':1,'b':2,'c':3}

# key
for key in d:
    print(key)

#value 
for v in d.values():
    print(v)

#key,value
for k,v in d.items():
    print('%s:%d'%(k,v))




# 可以使用 collections 模块的 Iterable

from collections import Iterable

L = [1,2,3]
t = (1,2,3)
n = 123

if isinstance(L,Iterable):
    print('L is  iterable')
if isinstance(t,Iterable):
    print('t is iterable')
if isinstance(n,Iterable):
    print('n is iterable')
else:
    print('n is not iterable')



#enumerate 可以将 list 变为 索引-元素对

for i,v in enumerate(L):
    print('L[%d]:%d'%(i,v))



# for 循环时同时引用两个变量

for x,y in [(1,2),(3,4),(5,6)]:
    print(x,y)




def findMinAndMax(L):
    if L != []:
        (min,max) = (L[0],L[0])
        for x in L:
            if x > max:
                max = x
            if x < min:
                min = x
        return (min,max)
    else:
        return(None,None)



L = [3,4,1,5,7,9,12,56,789]
min,max = findMinAndMax(L)

print('min:%d max:%d'%(min,max))















