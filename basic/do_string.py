#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# str -> bytes  bytes = str.encode
# str -> bytes  bytes = str(str,'encoding')
# bytes -> str  str = bytes.diecode()
# bytes -> str  str = str(bytes,'encoding')


s = 'Python - 中文'
#print(s)

b = s.encode('utf-8')
print('str=>bytes str.encode(\'utf-8\'):',b)

s1 = b.decode('utf-8')
print('bytes=>str  bytes.decode(\'utf-8\'):',s1)

s1 = b.decode()
print('bytes=>str  bytes.decode():',s1)



b = bytes(s,'utf-8')
print("str=>bytes alternative way:",b)

s1 = str(b,'utf-8')
print("bytes=>str alternative way:",s1)



