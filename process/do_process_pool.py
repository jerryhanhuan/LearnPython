#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_process_pool.py
#Created Time:2019-07-19 05:56:56

# 如果需要启动大量子进程，就需要以进程池的方式 批量创建子进程

from multiprocessing import Pool
from multiprocessing import cpu_count

import os,time,random






def child_run(arg):
    print('Run task %d pid:%d ...'%(arg,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %d spent %.2f seconds.'%(arg,(end-start)))


def main():
    num_of_cpu = cpu_count()
    print('cpu count is:',num_of_cpu)
    num_of_child = int(input('请输入进程数:'))
    p = Pool(num_of_child)
    for i in range(num_of_child):
        p.apply_async(child_run,args=(i,))
    print('waiting for all child done...')
    p.close()

    # join() 类似 wait() 等待所有子进程执行完
    # join() 之前必须先 close(),close() 后就不许添加新的 process了
    p.join()
    print('all child done...')



if __name__ == '__main__':
    main()







