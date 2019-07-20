#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_access.py
#Created Time:2019-07-17 09:29:34


# 如果需要内部属性不被外部访问，可以把属性的名称前加上两个下划线 __
# 在 python 中，实例的变量名如果以 __ 开头，就变成了一个 private ，只有内部可以访问，外部不能访问

# !!! 需要注意的是，变量名类似 __xxx__ 这样的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量
# 特殊变量是可以直接访问的，不是 private 变量，所以不能用 __name__,或者 __score__ 这样的变量名


class Student(object):
    
    def __init__(self,name,score):
        self.__name = name
        self.__score= score

    def name(self):
        return self.__name

    def score(self):
        return self.__score

    def print_info(self):
        print('%s got score:%.2f'%(self.__name,self.__score))


s = Student('yudf',99.5)
print(s.name())
print(s.score())
s.print_info()


# can not access __name and __score
# AttributeError: 'Student' object has no attribute '__name'

#print(s.__name)
#print(s.__score)








