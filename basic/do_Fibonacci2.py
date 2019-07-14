#!/usr/bin/env python3
# -*- coding: utf-8 -*-




def fab(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n += 1


def main():
    max = int(input('请输入斐波拉契数列的最大数目:'))
    for item in fab(max):
        print(item)


if __name__ == '__main__':
    main()
