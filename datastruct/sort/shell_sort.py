#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:shell_sort.py
#Created Time:2019-09-20 02:42:45


'''
将待排序数组按照步长 gap 进行分组，然后将每组的元素利用直接插入排序的方法进行排序,
每次将 gap 折半减小，循环上述操作，当 gap = 1时，利用直接插入方法，完成排序。

总体实现应该 由 三个循环完成
1. 第一层循环：将 gap 依次折半，对序列进行分组，直到 gap = 1
2. 第二，三层循环，则是直接插入排序的两层循环

'''


def shell_sort(L):
    length = len(L)
    # gap 初值一半设置为序列长度的一半
    gap = length//2
    while gap >= 1:
        # 从 L[gap] 开始
        for x in range(gap,length):
            # 从 x-gap 开始与选定元素开始倒序比较，每个比较元素之间间隔 gap
            for i in range(x-gap,-1,-gap):
                if L[i] > L[i+gap]:
                    L[i],L[i+gap] = L[i+gap],L[i]
        gap = gap//2

if __name__ == '__main__':
    L = [25,21,25,4,16,12,8,49,3]
    shell_sort(L)
    print(L)
