#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_lock.py
#Created Time:2019-07-19 13:01:38

import time,threading,random

# 余额
balance = 0
lock =  threading.Lock()



def bank(n):
    global balance
    # 先存后取
    balance += n
    balance -= n

def run_bank():
    print('threading %s is running'%threading.current_thread().name)
    for i in range(100):
        # 获取锁
        lock.acquire()
        try:
            bank(i)
        finally:
            #释放锁
            lock.release()
    print('thread %s is done'%threading.currentThread().name)

def main():
#    t = []
#    num_of_thread = 4
#    for i in range(4):
#        td = threading.Thread(target = run_bank)
#        t.append(td)
#
#    for td in t:
#        td.start()
#
#    for td in t:
#        td.join()
#
#    print('balance:',balance)

    t1 = threading.Thread(target = run_bank)
    t2 = threading.Thread(target = run_bank)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print('balance:',balance)


if __name__ == '__main__':
    main()





