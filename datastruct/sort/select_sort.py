#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:select_sort.py
#Created Time:2019-09-20 01:21:17

'''
选择排序：
1. 从待排序序列中，找到关键字最小的元素
2. 将最小的元素放到待排序序列最左边

'''


def select_sort(L):
    length = len(L)
    #依次遍历 序列中的每一个元素
    for x in range(0,length):
        #将当前位置的元素定义为 此轮循环中的最小值
        min = L[x]
        #将该元素与剩下的元素依次比较寻找到最小元素
        for i in range(x+1,length):
            if L[i] < min:
                L[i],min = min,L[i]
        #将此轮循环中得到的最小值赋值给当前位置
        L[x] = min



if __name__ == '__main__':
    L = [25,21,25,4,16,12,8,49,3]
    select_sort(L)
    print(L)


