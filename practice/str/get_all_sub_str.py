#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:get_all_sub_str.py
#Created Time:2019-07-24 01:15:44

# 方法1
def GetAllSubStr(s):
    result = []
    # x+1 表示字串长度
    for x in range(len(s)):
        # i 表示偏移量
        for i in range(len(s) - x):
            result.append(s[i:i+x+1])
    return result


# 方法2 列表生成式

def GetAllSubStr2(s):
    return [ s[i: i+x+1] for x in range(len(s)) for i in range(len(s) - x) ]


# 去重
def GetAllSubstr3(s):
    return list(set( s[i: i+x+1] for x in range(len(s)) for i  in range(len(s) - x)))



if __name__ == '__main__':
    s = input('输入一个字符串:')
    sub_str = GetAllSubStr(s)
    print(sub_str)
    
    sub_str2 = GetAllSubStr2(s)
    print(sub_str2)

    #去重字符串
    sub_str3 = GetAllSubstr3(s)
    print(sub_str3)
