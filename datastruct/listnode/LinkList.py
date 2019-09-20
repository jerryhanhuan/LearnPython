#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     ：2019/9/3 9:20
# @Author   ：joey
# @File     ：LinkList.py
# @Software ：PyCharm

'''
在 C/C++ 中，通常采用 指针+结构体 来实现链表
在 Python 中，则可以采用 引用+类 来实现链表

'''

# 链表节点类
class Node:
    def __init__(self, element, next_=None):
        self.element = element
        self.next = next_


#构建一个链表

n1 = Node(1)
p = n1
for i in range(2,10):
    n = Node(i)
    p.next = n
    p = p.next

#遍历链表
p = n1
while p is not None:
    print("%d "%(p.element))
    p = p.next









