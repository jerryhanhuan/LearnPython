#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:shell_sort.py
#Created Time:2019-09-20 02:42:45

def shell_sort(L):
    length = len(L)
    gap = length//2
    while gap >= 1:
        for x in range(gap,length):
            for i in range(x-gap,-1,-gap):
                if L[i] > L[i+gap]:
                    L[i],L[i+gap] = L[i+gap],L[i]
        gap = gap//2

if __name__ == '__main__':
    L = [25,21,25,4,16,12,8,49,3]
    shell_sort(L)
    print(L)
