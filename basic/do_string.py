#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = 'Python - 中文'
print(s)

b = s.encode('utf-8')
print(b)

s1 = b.decode('utf-8')
print(s1)


