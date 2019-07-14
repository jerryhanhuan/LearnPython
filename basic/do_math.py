#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math

def quadratic(a,b,c):
    "ax^2 + bx + c = 0 求解 x 的值"
    n = math.sqrt(b**2-4*a*c)
    x1 = ((-b) + n)/(2*a)
    x2 = ((-b) - n)/(2*a)
    return (x1,x2)




def power(x,n = 2):
    s = 1
    while n > 0:
        n = n-1
        s = s * x
    return s


if __name__ == '__main__':
    a,b,c = 2,3,1
    x1,x2 = quadratic(a,b,c)
    print('x1 is %f x2 is %f'%(x1,x2))

    n = power(100)
    print('100^2 is:',n)
    n = power(100,3)
    print('100^3 is:',n)

