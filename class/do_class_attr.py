#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_class_attr.py
#Created Time:2019-07-18 01:12:02


# 自定义类的 len() 方法

class Animal(object):
    def __len__(self):
        return 100


a = Animal()
print(len(a)) #100



class Myobject(object):
    def __init__(self):
        self.x = 9

    def pow(self):
        return self.x * self.x


# hasattr  setattr getattr

obj = Myobject()

if hasattr(obj,'x'):
    print('Myobject has attribute x:',obj.x)
else:
    setattr(obj,'x',9)

print(getattr(obj,'x'))#9




# 实例属性和类属性
# Python 是动态语言，根据类创建的实例可以任意绑定属性



# 实例属性
class Student(object):
    def __init__(self,name):
        self.name = name

Bob = Student('Bob')

if hasattr(Bob,'score'):
    print('%s got score:%.2f'%(Bob.name,Bob.score))
else:
    print('Bob has not attribute score,please set score')
    #setattr(Bob,'score')

Bob.score = 96.5

print('%s got score:%.2f'%(Bob.name,Bob.score))



# 类属性

# !!! 实例属性和类属性不能使用相同的名字，因为相同名字的实例属性将屏蔽类属性

class Student2(object):
    # 直接在 class 中定义属性，这种属性是类属性
    name = 'Student'
   

print(Student2.name) # Student

Amy = Student2()
Amy.name = 'Amy'
print(Amy.name) # Amy

Tom = Student2()
print(Tom.name) # Student






























