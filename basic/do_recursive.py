#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
===> fact(5)
===> 5 * fact(4)
===> 5 * (4 * fact(3))
===> 5 * (4 * (3 * fact(2)))
===> 5 * (4 * (3 * (2 * fact(1))))
===> 5 * (4 * (3 * (2 * 1)))
===> 5 * (4 * (3 * 2))
===> 5 * (4 * 6)
===> 5 * 24
===> 120
'''


def fact(n):
    "递归计算n的阶乘"
    if n == 1:
        return 1
    else:
        return n * fact(n-1)


def fact_iter(n,product):
    "递归存在栈溢出的风险，可用尾递归方式优，但是 python 解释器没有对尾递归做优化，尾递归方式也会造成栈溢出"
    if n == 1:
        return product
    else:
        return fact_iter(n-1,n*product)



def fact2(n):
    "尾递归计算n的阶乘"
    return fact_iter(n,1)

    


def main():
    n = int(input('请输入一个数字:'))
    sum = fact2(n)
    print('sum is:',sum)



if __name__ == '__main__':
    main()
    
	
