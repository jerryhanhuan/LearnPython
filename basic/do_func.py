#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# 数据类型转换

print('=== str -> int ===')
str1 = input('输入一个数字字符串:')
num = int(str1)
print('str -> int %s -> %d success'%(str1,num))

str2 = str(num)
print('int -> str %d -> %s success'%(num,str2))

print('=== str -> float ===')
str3 = input('输入一个浮点数:')
fnum = float(str3)
print('str -> float %s -> %f success'%(str3,fnum))

str4 = str(fnum)
print('float -> str %f -> %s success'%(fnum,str4))


# 内置函数

# abs
num = int(input('请输入一个数字:'))

print('num is:',num)

if num > 0:
    print('num is positive num')
elif num == 0:
    print('num is zero')
else:
    print('num is negetive num')
    num = abs(num)

print('num is:',num)




# max 可以接收任意多个参数，返回值最大的参数

max_num = max(0,-1,100,-1000)
print('max num is:',max_num)



# num covert to hex

hex_num = int(input('输入一个整数:'))
hex_str = hex(hex_num)
print('int -> hex: %d - > %s'%(hex_num,hex_str))



def printme( str ):
   "打印传入的字符串到标准显示设备上"
   print(str)
   return

printme('yudf')



def ShowClassmates(classmates):
    num = len(classmates)
    print('class has',num,'students')
    for index in range(num):
        print('serail:',index,'name:',classmates[index])
    return

ShowClassmates([1,2,3,4])
