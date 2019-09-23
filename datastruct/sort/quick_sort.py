#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:quick_sort.py
#Created Time:2019-09-23 02:59:27

def quick_sort(L,start,end):
    if start>=end:
        return
    print("start:",start," end:",end)
    i,j,pivot = start,end,L[start]
    while i<j:
        #从右到左找比 pivot 小的
        while i<j and L[j]>=pivot:
            #--j python 没有 -- 和 ++ 操作符
            j = j-1
        if(i<j):
            L[i] = L[j]
        #从右往左找比 pivot 大的
        while i<j and L[i]<=pivot:
            #++i
            i = i+1
        if(i<j):
            L[j] = L[i]
    L[i] = pivot
    quick_sort(L,start,i-1)
    quick_sort(L,i+1,end)
    

if __name__ == '__main__':
    L = [25,21,25,4,16,12,8,49,3]
    quick_sort(L,0,len(L)-1)
    print(L)

