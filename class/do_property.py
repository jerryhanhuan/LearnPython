#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_property.py
#Created Time:2019-07-18 02:28:55



# python 内置 的 @property 装饰器(decorator) 装饰器就是负责把一个方法变成属性调用的
# 将一个 getter方法变为属性，只需要加上 @property，此时，@property 又创建了另外一个装饰器 @score.setter，负责把一个 setter 方法变成属性赋值
# 只定义 getter 不定义setter 就是定义只读方法


class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueErrror('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueErrror('score must between 0~100!')
        self._score = value

    @property
    def birth(self):
        return self._birth 
    
    @birth.setter
    def birth(self,value):
        self._birth = value

    #age 制度，因为 age 可以根据 birth 推算出来

    @property
    def age(self):
        return 2019 - self._birth



s = Student()

s.score = 85
print(s.score) # 85

s.birth = 1992
print('birth is:',s.birth)

print('age is:',s.age) # 27



