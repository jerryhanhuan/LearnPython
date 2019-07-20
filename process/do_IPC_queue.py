#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_IPC_queue.py
#Created Time:2019-07-19 07:44:13


#process 之间肯定是需要通信的，python 的 multiprocessing 模块包装了底层的机制
#提供了 Queue，Pipes 等多种方式来交换数据

# 以 Queue 为例，在父进程中创建两个子进程，一个 往 Queue里写数据，一个往Queue里读数据


from multiprocessing import Process,Queue
import os,time,random

# write

def write(q):
    print('Process to write,pid:%d'%os.getpid())
    for value in ['A','B','C','x','y','z']:
        print('puts %s to queue'%value)
        q.put(value)
        time.sleep(random.random())


# read
def read(q):
    print('Process to read pid:%d'%os.getpid())
    while True:
        value = q.get(True)
        print('get %s from queue'%value)


def main():
    # 父进程创建 Queue，并传递给子进程
    q = Queue()
    
    #写进程
    pw = Process(target = write,args=(q,))
    #读进程
    pr = Process(target = read,args=(q,))
    
    pw.start()
    pr.start()

    pw.join()
    pr.terminate()



if __name__ == '__main__':
    main()












