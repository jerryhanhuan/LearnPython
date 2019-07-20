#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_os.py
#Created Time:2019-07-18 13:29:05


import os


print('os:',os.name)
print('uname:',os.uname())


# 当前目录的绝对路径

print('path:',os.path.abspath('.'))


#mkdir
dir = 'test'
os.mkdir(dir)

#rmdir
os.rmdir(dir)




