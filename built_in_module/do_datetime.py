#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_datetime.py
#Created Time:2019-07-20 10:01:45



from datetime import datetime
import time

def main():
    now =  datetime.now()
    print(now) #2019-07-20 10:15:09.476397
    
    #构造一个 date
    date = datetime(2014,7,1,12,3,34)
    print(date) #2014-07-01 12:03:34


    # datetime -> timestamp
    # python 的 timestamp 是一个浮点数，如果由小数位，小数位表示毫秒数
    print(now.timestamp())
    print(date.timestamp())

    # timestamp -> datetime
    t = 1429417200.0
    # 本地时间
    print(datetime.fromtimestamp(t)) #
    # UTC 时间
    print(datetime.utcfromtimestamp(t)) #

    # datetime -> str 注意 月份是 小写 m
    print(now.strftime('datetime->str %Y-%m-%d %H:%M:%S'))
    
    # str -> datetime
    str_time = '2019-07-20 12:15:37'
    dt = datetime.strptime(str_time,'%Y-%m-%d %H:%M:%S')
    print('str->datetime',dt)



    #get timestamp
    print('timestamp::',time.time())

    # datetime -> timestamp
    now = datetime.now()
    print('datetime -> timestamp using timestamp()::',now.timestamp()) #1563630236.570223
    print('datetime -> timestamp using mktime()::',time.mktime(now.timetuple())) #1563630236.0


    #timestamp - > datetime
    t = time.time()
    #utc timestamp
    print('timestamp->datetime::',datetime.utcfromtimestamp(t))


    # str -> timestamp
    # str ->datetime -> timestamp
    str_time = '2019-7-20 21:55:12'
    dt = datetime.strptime(str_time,'%Y-%m-%d %H:%M:%S')
    print('str -> timestamp::',time.mktime(dt.timetuple()))





if __name__ == '__main__':
    main()






