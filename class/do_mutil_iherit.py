#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_mutil_iherit.py
#Created Time:2019-07-18 02:54:35



# 多重继承

# 通过多重继承，一个子类就可以同时获得多个父类的功能

class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Runnable(object):
    def run(self):
        print('Running')


class Flyable(object):
    def fly(self):
        print('Flying')


# 多重继承

class Dog(Mammal,Runnable):
    pass

class Bat(Mammal,Flyable):
    pass



# MixIn
# 组合多个单一功能的类，完成对应功能，这种设计通常称为 Mixin
# 由于 python 允许使用多重继承，因此， mixin 就是一种常见的设计
# 只允许单一继承的语言(如 java) 不能使用 mixin 的设计














