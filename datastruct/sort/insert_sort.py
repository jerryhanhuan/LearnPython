#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:insert_sort.py
#Created Time:2019-09-20 02:19:02

'''
插入排序的核心思想是： 将数组中的所有元素依次跟前面已经排好的元素相比较
如果选择的元素比已排序的元素小，则交换，直到全部元素比较过

1. 第一层循环，遍历待比较的所有数组元素
2. 第二层循环，将本轮选择的元素 selected 与已经排好序的元素 ordered 相比较，如果 selected < ordered ，那么将两者交换

'''




def insert_sort(L):
    length = len(L)
    # 遍历数组中的所有元素，0 号 索引元素默认已排序，因此从1开始
    for x in range(1,length):
    # 将L[x] 与已经排好序的前序数组元素依次比较，如果L[x] 小，则交换
        # L[0,x-1]
        for i in range(0,x):
            if L[x] < L[i]:
                L[x],L[i] = L[i],L[x]



if __name__ == '__main__':
    L = [25,21,25,4,16,12,8,49,3]
    insert_sort(L)
    print(L)

