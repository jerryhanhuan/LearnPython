#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_bytes_io.py
#Created Time:2019-07-18 13:02:42


# StringIO 只能操作 str
# 如果要操作二进制数据，就需要使用 BytesIO
# BytesIO 实现了在内存中读写 bytes

from io import BytesIO


b = BytesIO()

# 不能是 str,只能是 bytes
#b.write('Hello,中国')

b.write('Hello,中国'.encode('utf-8'))

print(b.getvalue())



f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
data = f.read()
print(data.decode('utf-8'))





