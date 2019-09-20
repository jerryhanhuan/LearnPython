#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:bubble_sort.py
#Created Time:2019-09-20 01:02:11


def bubble_sort(L):
    length = len(L)
    for i in range(1,length):
        for x in range(0,length-i):
            if L[x] > L[x+1]:
                L[x],L[x+1] = L[x+1],L[x]


if __name__ == '__main__':
    L = [25, 21, 25, 4, 16, 12, 8, 49, 3]
    bubble_sort(L)
    print(L)
