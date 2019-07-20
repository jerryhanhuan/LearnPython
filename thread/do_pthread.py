#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_pthread.py
#Created Time:2019-07-19 11:58:52


import os,threading
import time,random



#新线程执行代码


def thread_routine(args):
    print('threading %s is running...'%(threading.current_thread().name))
    print('threading %s args:%s'%(threading.current_thread().name,args))
    t1 = time.time()
    time.sleep(random.random())
    t2 = time.time()
    print('threading %s end spent %.2f seconds'%(threading.current_thread().name,(t2-t1)))



def main():
    print('Main threading %s is running...'%(threading.current_thread().name))
    #创建一个线程
    t = threading.Thread(target = thread_routine,name='thread_routine',args=('12345678',))
    t.start()
    t.join()
    print('Main threading %s end ...'%(threading.current_thread().name))



if __name__ == '__main__':
    main()
