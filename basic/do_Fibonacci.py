#!/usr/bin/env python3
# -*- coding: utf-8 -*-



def fab(max):
    "斐波那契數列:除了第一个，第二个数，其它的数都等于之前两个数相加"
    n,a,b = 0,0,1
    L = []
    while n < max:
        L.append(b)
        a,b = b,a+b
        n = n + 1
    return L


def main():
    max = int(input('请输入斐波那契数列最大个数:'))
    L = fab(max)
    for item in L:
        print(item)


if __name__ == '__main__':
    main()
