#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def printme( str ):
   "打印传入的字符串到标准显示设备上"
   print(str)
   return

printme('yudf')



def ShowClassmates(classmates):
    num = len(classmates)
    print('class has',num,'students')
    for index in range(num):
        print('serail:',index,'name:',classmates[index])
    return

ShowClassmates([1,2,3,4])
