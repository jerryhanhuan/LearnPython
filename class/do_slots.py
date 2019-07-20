#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_slots.py
#Created Time:2019-07-18 01:49:41


# python 是动态语言，创建了一个类的实例后，可以给该实例绑定任何属性和方法

class Student(object):
    pass

s = Student()

# 绑定一个 name 属性
s.name = 'Amy'
print(s.name) # Amy

# 绑定一个方法

# 首先定义一个方法
def showname(self):
    print('name:',self.name)

from types import MethodType

s.showname = MethodType(showname,s)

s.showname() #name: Amy




# 给一个实例绑定的属性和方法，对另外一个实例是不起作用的
s2 = Student()
#print(s2.name) #AttributeError: 'Student' object has no attribute 'name'
#s2.showname() #AttributeError: 'Student' object has no attribute 'showname'



# 为了给所有实例绑定属性和方法，可以给类绑定属性和方法，这样所有属性都可以调用

Student.name = 'Student'
Student.showname = showname

print(s2.name)
print(s2.showname())




# !!!! 可以使用 __slots__ 来限制实例的属性，比如，只允许对 Student 实例添加 name 和 age 属性
# 特殊变量 __slots__
# !!! __slots__ 仅对当前类的实例起作用，对继承的子类不起作用 
# 在子类中 定义 __slots__,允许设定的属性就是父类 的 __slots__ + 子类的 __slots__


class Student2(object):
    __slots__ = ('name','age') #用 tuple 定义允许绑定的属性名称


s3 = Student2()
s3.name = 'Bob'
s3.age = 17

print(s3.name) # Bob
print(s3.age)  # 17

#s3.score = 100 #AttributeError: 'Student2' object has no attribute 'score'
















