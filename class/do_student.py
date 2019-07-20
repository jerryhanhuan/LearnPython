#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_student.py
#Created Time:2019-07-17 08:51:00



# 通过 class 关键字定义 类
# class 后面紧跟着类名，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的
# 通常，没有合适的继承类，就使用 object 类object 类是所有类都会继承的类

class Student(object):

    # __init__  前后分别两个下划线
    # __init__ 第一个参数永远是 self，表示创建的实例本身
    # 有了 __init__ 方法，在创建实例的时候，就不能传入空的参数了，必须传入和 __init__ 方法匹配的参数，self 不用传，Python 解释器自己会把实例
    # 变量传进去
    def __init__(self,name,score):
        self._name = name
        self._score = score

    # 要定义一个普通方法，第一参数是 self，其它则是和普通方法一样
    def score(self):
        print('%s got score:%.2f'%(self._name,self._score))



s1 = Student('yudf',93.6)
s1.score()



