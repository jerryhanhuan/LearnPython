#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:bubble_sort.py
#Created Time:2019-09-20 01:02:11


'''
冒泡排序的思路比较简单

1. 将序列中的相邻元素，依次比较，保证右边的元素大于左边的元素，第一轮结束后，序列最后一个元素一定是当前序列的最大值
2. 对序列中剩下的 n-1 个元素再次执行步骤1
3. 对于长度为 n 的序列，以供需要执行 n-1 轮比较


'''


def bubble_sort(L):
    length = len(L)
    # 需要执行 n-1 轮交换，从1 开始，避免二层for 循环中的 x+1 溢出
    for i in range(1,length):
        #每轮交换中，需要最右侧的一定是顺序的，最大的都在右侧，所以只用循环到未排序的位置
        #每轮过后，未排序的位置到 length-i
        for x in range(0,length-i):
            if L[x] > L[x+1]:
                L[x],L[x+1] = L[x+1],L[x]


if __name__ == '__main__':
    L = [25, 21, 25, 4, 16, 12, 8, 49, 3]
    bubble_sort(L)
    print(L)
