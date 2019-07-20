#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_open.py
#Created Time:2019-07-18 04:18:44



#文件使用完之后必须关闭
#保证一定会关闭文件，使用 try ... finally 来实现
def test_file(path):
    try:
        f = open(path,'rb')
        print(f.read())
    finally:
        if f:
            f.close()

#使用 with 语句来自动帮我们调用 close() 方法

def test_file2(path):
    with open(path,'r') as f:
        print(f.read())

# 如果文件很小，read() 一次性读取最方便
# 如果不能确定文件大小，反复调用  read(size) 比较保险
# readline() 每次读取一行
# readlines() 一次读取所有文件，并按照行返回 list

def main():
    path = input('请输入文件路径:')
    test_file2(path)



if __name__ == '__main__':
    main()



