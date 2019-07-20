#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_return_func.py
#Created Time:2019-07-16 11:45:10



#函数不仅可以作为参数， 函数还可以作为返回值

# 一般定义一个求和函数

def calc_sum(*args):
    sum = 0
    for n in args:
        sum += n
    return sum



sum = calc_sum(1,4,6,7,8,0)

print(sum)


# 如果不需要立刻求和，而是在后面的代码中，根据需要再计算
# 可以不返回求和的结果，而是返回求和的函数


def lazy_sum(*args):
    def sum():
        s = 0
        for n in args:
            s += n
        return s
    return sum

# 调用 lazy_sum ，返回的不是求和结果，而是求和函数
f = lazy_sum(1,3,5,7,9)

# 调用函数 f 的时候才真正计算求和的结果
s = f()

print('sum is:',s)



# !!! 闭包，在这个例子中，在函数 lazy_sum 中定义了函数 sum，内部函数 sum 可以引用外部函数 lazy_sum 的参数 和局部变量
#当 lazy_sum 返回函数 sum 时，相关参数都保存在返回的函数中，这种程序结构被称为 闭包

#lazy_sum 每次都返回一个新的函数

f1 = lazy_sum(1,3,5,7,9)
f2 = lazy_sum(1,3,5,7,9)

if f1 == f2:
    print('f1 == f2')
else:
    print('f1 != f2') # 会执行这一句





# 闭包

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1,f2,f3  = count()

print(f1())
print(f2())
print(f3())

# 上面的输出 是 9 9 9 而不是 1 4 9
# 这是因为 返回的函数引用了变量 i,但是函数并非立刻执行，等到三个函数都返回的时候，i=3，所以结果都是 9 


# !!! 返回闭包时 牢记一点，返回函数不要引用任何循环变量，或后续会发生改变的变量


# 如果一定要 引用循环变量，方式再创建一个函数，用该函数的参数绑定循环变量当前的值
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变

def count2():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i)) # f(i) 立即执行，因此 i 的值被立即传入f
    return fs

f1,f2,f3 = count2()
print(f1())
print(f2())
print(f3())





# 利用闭包返回一个计算器函数，每次调用它返回递增整数

s = 0
def createCounter():
    def count():
        global s
        s += 1
        return s
    return count


counterA = createCounter()
print(counterA(),counterA(),counterA()) # 1 2 3


counterB = createCounter()
print(counterB(),counterB(),counterB()) # 4 5 6




#另外一种做法

def Counter():
    s = [0]
    def count():
        s[0] = s[0] + 1
        return s[0]
    return count

countA = Counter()
print(countA(),countA(),countA()) # 1 2 3


countB = Counter()
print(countB(),countB(),countB()) # 1 2 3

















