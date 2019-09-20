#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:select_sort.py
#Created Time:2019-09-20 01:21:17


def select_sort(L):
    length = len(L)
    for x in range(0,length):
        min = L[x]
        for i in range(x+1,length):
            if L[i] < min:
                L[i],min = min,L[i]
        L[x] = min



if __name__ == '__main__':
    L = [25,21,25,4,16,12,8,49,3]
    select_sort(L)
    print(L)


