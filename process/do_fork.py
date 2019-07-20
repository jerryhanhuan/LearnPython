#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_fork.py
#Created Time:2019-07-18 15:55:51


import os

print('process %s runing'%(os.getpid()))


# fork only work success on the linux/unix/mac

pid = os.fork()

if pid == 0:
    print('this is in the child process pid %d parent pid %d' % (os.getpid(),os.getppid()))
elif pid > 0:
    print('this is int the parent process pid %d'%os.getpid())
else:
    print('fork failed')


