#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:insert_sort.py
#Created Time:2019-09-20 02:19:02



def insert_sort(L):
    length = len(L)
    for x in range(1,length):
        for i in range(0,x):
            if L[x] < L[i]:
                L[x],L[i] = L[i],L[x]



if __name__ == '__main__':
    L = [25,21,25,4,16,12,8,49,3]
    insert_sort(L)
    print(L)

