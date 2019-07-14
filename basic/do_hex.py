#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import codecs




def str2hex(s):
    b = codecs.decode(s,'hex_codec')
    return b

def hex2str(b):
    s = codecs.encode(b,'hex_codec')
    return s


def main():
    s = input("请输入一串十六进制字符串::")
    print('s is:',s)
    b = str2hex(s)
    print('b is:',b,'len is:',len(b))
    s2 = hex2str(b)
    print('s is:',s,'len is:',len(s))


if __name__ == '__main__':
    main()
	
