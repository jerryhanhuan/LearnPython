#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_yield.py
#Created Time:2019-07-15 05:56:03



# generator
# 通过列表生成式，我们可以直接创建一个 list，但是受到 内存限制，list 的容量肯定有限
# list 很占用内存，如果列表元素可以按照某种算法推算出来，我们可以在循环中不断推算后续元素，而不必创建完整的 list，从而节省空间

# 在 python 中，这种一边循环一边计算的机制，称为 生成器: generator


# 创建一个生成器，最简单的方法，把列表生成式的[] 改为 ()

L = [x for x in range(1,10)]

print(type(L)) #<class 'list'>''

g = (x for x in range(1,10)) 

print(type(g)) #<class 'generator'>



# generator 是可迭代对象 支持  next() 方法

print(next(g))
print(next(g))

# 使用 next() ，没有更多元素时，抛出错误 StopIteration
# 所以，正确的迭代方法是 for 循环,for 循环不会抛出错误 StopIteration

print('====  for ====')
for n in g:
    print(n)



#yield 如果一个函数定义中包含 yield ,那么这个函数就不是一个普通函数，而是一个 generator

def Fibonacci(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n += 1
    return 'donw'

f = Fibonacci(10)

print(' ==== Fibonacci iter using for ====')
# 使用 for
for n in f:
    print(n)

# for 无法获取 Fibonacci 返回的值 'done' 使用 next,需要处理 StopIteration

print(' ==== Fibonacci iter using for ====')

f = Fibonacci(10)

while True:
    try:
        x = next(f)
        print(x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break






# generator 和函数执行流程不一样，函数是顺序执行，遇到 return 或者最后一行语句就返回
# generator 则是在每次调用 next 时执行，遇到 yield 返回，再次执行时从上次 yield 语句的下一语句处执行

print('============== yield ==============')

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3


o = odd()
n = next(o)
print('n is:',n)
n = next(o)
print('n is:',n)
n = next(o)
print('n is:',n)




# 杨辉三角

# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]


def triangles():
    yield [1]
    line = [1,1]
    yield line
    # 从第三行开始计算
    while True:
        i = 0
        r = []
        # 按规律生成该行除首尾外的数字
        for i in range(0,len(line)-1):
            r.append(line[i] + line[i+1])
        # 把两端的数字连上
        line = [1] + r + [1]
        yield line


# test triangles

n = 0
results = []

for l in triangles():
     print(l)
     n += 1
     if n == 10:
         break










