#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:test_read.py
#Created Time:2019-07-18 05:26:07

# read()
# read(size=-1,/),返回值为 str
# f.read()  读取全部
# f.read(size) 读取size 个字符
#
# readline() 读取一行数据
# readline(size=-1,/) 返回值为 str
# f.readline() # 读取一行
#  
# readlines() 一次性读取完，并以列表形式返回
#
# seek(offset,whence=0,/) offset 代表移动的字节偏移量， whence 代表移动的起始位置： 0-文件开头 1-当前位置，3-文件末尾
# tell() 返回文件的当前位置
#
#

import functools

# decorator

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wraper(*argv,**kv):
            print('===== begin %s ====='%text)
            func(*argv,**kv)
            print('===== end %s ====='%text)
        return wraper
    return decorator

@log('read()')
def test_read(path):
    with open(path,'rb') as f:
        data = f.read()
        print(data.decode('utf-8'))


@log('read_size')
def test_read_size(path):
    with open(path,'rb') as f:
        count = 10
        while True:
            data = f.read(count)
            if len(data) == 0:
                print('read done')
                break;
            else:
                print(data.decode('utf-8'))




@log('readline()')
def test_readline(path):
    with open(path,'rb') as f:
        count = 0
        while True:
            data = f.readline()
            if len(data):
                count += 1
                print(data.decode('utf-8'))
            else:
                print('read done count:',count)
                break

@log('readlines()')
def test_readlines(path):
    with open(path,'rb') as f:
        lines = f.readlines()
        for line in lines:
            print(line.decode('utf-8').strip())





def main():
    path = input('input file path:')
    mode = int(input('1-read() 2-read(size) 3-readline() 4-readlines():'))
    if mode == 1:
        test_read(path)
    elif mode == 2:
        test_read_size(path)
    elif mode == 3:
        test_readline(path)
    else:
        test_readlines(path)

if __name__ == '__main__':
    main()




