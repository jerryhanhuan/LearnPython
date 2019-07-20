#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_decorator.py
#Created Time:2019-07-17 01:16:27


# 装饰器

def now():
    return '2019-07-17'

f=  now
print(f)
print(f.__name__)
print(f())



#假设我们要增强 now() 函数的功能，比如在函数调用前后自动打印日志，但又不希望修改 now() 函数的定义
#这种在代码运行期间动态增加功能的方式，称之为 ‘装饰器’ Decorator

# 本质上，decorator 就是一个返回函数的高阶函数

def log(func):
    def warper(*args,**kv):
        print('call %s():'%func.__name__)
        return func(*args,**kv)
    return warper




# @log 放到 hi 函数的定义处，相当于执行了 语句 hi = log(hi)
# log 是一个 decorator ，返回一个函数，所以，原来的 hi()函数仍然存在，只是现在的同名变量指向了 log 返回的函数，于是调用 hi 将执行新函数，也就是 log 返回 的 warper
@log
def hi(name):
    print('hello',name)

hi('yudf') # call hi()
           # hello yudf

print(hi.__name__)#warper


# 如果 decorator 本身需要传入参数，那么就需要返回一个 decorator 的高阶函数

def log2(text):
    def decorator(func):
        def warper(*args,**kv):
            print('%s %s()'%(text,func.__name__))
            return func(*args,**kv)
        return warper
    return decorator



# hi2 = log2('excute')(hi2)
@log2('excute')
def hi2(name):
    print('hello',name)

hi2('yudf') # excute hi2()
            # hello yudf


# !!! 注意 hi2 是 decorator 返回的 warper，这个时候 hi2 的 __name__ 已经变了
print(hi2.__name__) # warper

# 因为 __name__ 已经变了，有些依赖函数签名的代码执行会出错
# 一种方法是 把原始函数的 __name__ 等属性复制到 wraper() 函数中， 即 wraper.__name__ = func.__name__
# 但 python 已经内置了 这样的方法 functools.wraps 




import functools


def log3(func):
    @functools.wraps(func)
    def wraper(*args,**kv):
        print('call %s()'%func.__name__)
        return func(*args,**kv)
    return wraper 

@log3 
def hi3(name):
    print('hello',name)

hi3('yudf')

print(hi3.__name__) #hi3



#带参数的装饰器
def log4(text):
    def docorator(func):
        @functools.wraps(func)
        def wraper(*args,**kv):
            print('%s %s()'%(text,func.__name__))
            return func(*args,**kv)
        return wraper
    return docorator

@log4('excute''')
def hi4(name):
    print('hello',name)

hi4('yudf')

print(hi4.__name__)





# practice,设计 一个 decorator，可以作用于任何函数上，打印函数的执行时间

import time
import functools

def metric(func):
    @functools.wraps(func)
    def wraper(*args,**kv):
        t1 = time.time()
        r = func(*args,**kv)
        print('call %s spend %s ms'%(func.__name__,(time.time()-t1)*1000))
        return r
    return wraper


@metric
def do_sm(x,y):
    return x * y

n = do_sm(4,5)
print(n)
print(do_sm.__name__)


#pratice ,设计一个 decorator log，即支持 @log，也支持 @log('debug')


def logr(*text):
    def decorator(func):
        @functools.wraps(func)
        def wraper(*args,**kv):
            print(func.__name__,'begin',*text)
            func(*args,**kv)
            print(func.__name__,'end',*text)
        return wraper
    return decorator


@logr() # or @logr('debug')
def func_run():
    print('%s is running'%(func_run.__name__))

func_run()




























