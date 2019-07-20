#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_inherit.py
#Created Time:2019-07-17 12:46:52


class Animal(object):
    def run(self):
        print('animal runing')


#class Cat(Animal):
#    pass
#
#class Dog(Animal):
#    pass
#
#
#cat = Cat()
#dog = Dog()
#
#
#cat.run() #animal runing
#dog.run() #animal runing
#

class Dog(Animal):
    def run(self):
        print('dog runing')

class Cat(Animal):
    def run(self):
        print('cat runing')
    

cat = Cat()
cat.run()# cat runing
dog = Dog()
dog.run()#dog runing


a = list()
b = Dog()
c = Cat()

print(type(a))
print(type(b))
print(type(c))


# 判断变量是否属于某个类型，可以使用 isinstance() 判断

print(isinstance(a,list))#True
print(isinstance(b,Dog))#True
print(isinstance(c,Cat))#True
print(isinstance(b,Animal))#True


# 多态的好处
# 编写一个函数，函数接收一个 animal 类型的变量

def run_twice(animal):
    animal.run()
    animal.run()


a = Animal()
b = Dog()
c = Cat()

run_twice(a)
run_twice(b)
run_twice(c)




# 静态语言 vs 动态语言
# 对于静态语言(例如 java)，如果需要传入 Animal 类型，则传入的对象必须是 Animal 类型或者它的子类，否则无法调用 run()
# 对于 Python这样的动态语言，则不一定需要传入 Animal 类型，我们只需要保证传入的对象有一个 run() 方法即可
# 这就是动态语言的 ‘鸭子类型’，它不要求严格的继承体系，一个对象只要看起来像鸭子，走起路来像鸭子，那么它就可以被看做是鸭子

class Timer(object):
    def run(self):
        print('Time Start')

t = Timer()
run_twice(t) # Time Start

































