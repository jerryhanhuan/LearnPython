#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_serial.py
#Created Time:2019-07-18 13:46:10


# 把变量从内存中变成可存储或者可传输的过程称之为序列化
# 序列化之后，可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上
# python 中提供了 pickle 模块来实现序列化


import pickle
import os

d = {'name':'Bob','age':20,'score':88}

for k,v in d.items():
    print(k,v)

# pickle.dumps() 方法把任意对象序列化为 一个 bytes，然后，就可以把这个 bytes 写入文件
b = pickle.dumps(d)
print(b)

# pickle.dump() 方法直接把序列化对象写入一个 file-like objcet


file = 'b.txt'
with open(file,'wb') as f:
    pickle.dump(d,f)

with open(file,'rb') as f:
#    data = f.read()
#    print(data)
#     d = pickle.loads(data)
#     print(d)
      d1 = pickle.load(f)
      print(d1)

os.remove(file)












