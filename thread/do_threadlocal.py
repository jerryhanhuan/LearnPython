#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_threadlocal.py
#Created Time:2019-07-20 02:30:56



# ThreadLocal 变量虽然是全局变量，但是每个线程都只能读写自己线程的独立副本，互补干扰
# ThreadLocal 解决了参数在一个线程中各个函数之间互相传递的问题
# 如下例子所示，可以将 local_school 看成全局变量，但是每个属性如 local_school.student 都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal 内部会处理
# local_school 可以看成是一个 dict，不但可以用 local_school.student，还可以绑定其它变量，如 local_school.teacher

import threading


#创建全局的 threadlocal 对象

local_school = threading.local()



def do_process_student():
    print('Thread %s runing ,student is:%s'%(threading.current_thread().name,local_school.student)) 
    


def do_process_thread(name):
    local_school.student = name
    do_process_student()



def main():
    t1 = threading.Thread(target = do_process_thread,name = 'Thread-t1', args = ('Bob',))
    t2 = threading.Thread(target = do_process_thread,name = 'Thread-t2', args = ('Jack',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()





if __name__ == '__main__':
    main()







