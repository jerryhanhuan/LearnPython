#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_subprocess.py
#Created Time:2019-07-19 07:27:08


# 当子进程是外部进程时
# 使用 subprocess module
# subprocess 可以让我们非常方便的启动一个子进程，然后控制其输入输出


# eg1. 使用 python 运行 ls 命令

import subprocess


def test_ls():
    print('ls -la')
    r = subprocess.call(['ls','-la'])
    print('Exit code:',r)

def main():
    test_ls()


if __name__ == '__main__':
    test_ls()
