#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     ：2019/7/21 19:33
# @Author   ：joey
# @File     ：Hello_world.py
# @Software ：PyCharm

# python 2.x 使用这行
#from Tkinter import *
#python 3.x 使用这行

from tkinter import *

'''
# 创建 Tk 对象,Tk代表窗口
root = Tk()

# 设置窗口标题
root.title('第一个 tikle 程序')

# 创建 label 对象,第一个参数指定 label 放入 root 窗口
w = Label(root, text='Hello,tkinter')

# 调用 pack 进行布局
w.pack()

# 启动主窗口的消息循环
root.mainloop()
'''

# 另外一种方法是 不直接使用 Tk，只要创建 Frame 的子类，它的子类就会自动创建 Tk 对象作为窗口

# 定义继承于 Frame 的类，Application 类

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        #pack() 进行布局
        self.pack()
        # 调用 initWidgets 初始化界面
        self.initWidgets()

    def initWidgets(self):
        # 创建 label 对象，第一个参数指定该 Label 放入 root
        w = Label(self)
        # 创建一个位图
        bm = PhotoImage(file='../img/python.png')
        # 必须用一个不会被释放的变量引用该图片，否则该图片会被回收
        w.x = bm
        # 设置显示的图片的 bm
        w['image'] = bm
        # 布局
        w.pack()
        # 创建 button 对象，第一个参数指定该button 放入 root
        okButton = Button(self, text='确定')
        okButton['background'] = 'yellow'
        #okButton.configure(background='yellow')
        okButton.pack()


if __name__ == '__main__':
    # 创建Application对象
    app = Application()
    # Frame有个默认的master属性，该属性值是Tk对象（窗口）
    print(type(app.master))
    # 通过master属性来设置窗口标题
    app.master.title('Hello Python')
    # 启动主窗口的消息循环
    app.mainloop()