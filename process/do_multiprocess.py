#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_multiprocess.py
#Created Time:2019-07-19 01:01:24


# os.fork 只可用于 Unix/Linux/Mac，无法用于 Windows
# python 是跨平台的，自然也应该提供一个跨平台的多进程支持， multiprocessing 模块就是跨平台版本的多进程模块
# multiprocessing 模块提供了一个 Process 类来代表一个进程对象

from multiprocessing import Process
import os


# 子进程要执行的代码

def child_run(name):
    print('Run child process %s pid:%s'%(name,os.getpid()))

def main():
    print('Parent process pid:%s Running'%(os.getpid()))
    p = Process(target=child_run,args=('test',))
    print('child process will start')
    # 用 start() 方法启动
    p.start()
    # 等待子进程结束后再继续往下运行，通常用于进程间同步
    p.join()
    print('child process end')
if __name__ == '__main__':
    main()







