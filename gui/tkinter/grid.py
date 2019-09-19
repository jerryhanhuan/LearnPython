#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     ：2019/7/21 23:23
# @Author   ：joey
# @File     ：grid.py
# @Software ：PyCharm

'''
Grid 把组件空间分解成了 一个网格进行维护，即按照 行，列的方式排列组合，组件位置由其所在的行号和列号决定。
使用 Grid 布局的过程就是为各个组件指定 行号和列号 的过程，不需要为 每个网格都指定大小， Grid 布局 会自动为它们设置合适的大小

程序调用组件的 grid() 方法进行 Grid 布局，在调用 grid() 方法时可传入多个选项
grid() 方法支持的 ipadx、ipady、padx、pady  和  pack() 方法的这些选项相同，而 grid() 额外增加了如下选项


'''

from tkinter import *

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        # 创建一个输入组件
        e = Entry(relief=SUNKEN,font=('Courier New', 24), width=25)
        # 对输入组件进行 pack 布局，放在容器顶部,在垂直方向和其它组件间距为 10
        e.pack(side=TOP, pady=10)

        p = Frame(self.master)
        p.pack(side=TOP)

        # 定义显示字符串元祖
        names = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '.', '=')
        for i in range(len(names)):
            b = Button(p, text=names[i], font=('Verdana', 20), width=6)
            b.grid(row=i//4, column=i % 4)


if __name__ == '__main__':
    root = Tk()
    root.title('Grid 布局')
    # 设置窗口的大小和位置
    # width x height + x_offset + y_offset
    root.geometry("250x250+30+30")
    App(root)
    root.mainloop()
