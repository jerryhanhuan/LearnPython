#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     ：2019/7/21 21:47
# @Author   ：joey
# @File     ：pack.py
# @Software ：PyCharm


from tkinter import *

'''
# 创建窗口
root = Tk()
# 创建窗口标题
root.title('测试 Pack')

# 添加3个label

for i in range(3):
    lab = Label(root, text='第%d个label'%(i+1), background='yellow')
    # 调用 pack 进行布局
    lab.pack()

#启动主窗口的消息循环

root.mainloop()
'''

'''
help(tkinter.Label.pack)
pack() 布局方法通常可以支持如下选项

anchor :当可用空间大于组件所需求的大小时，该选项决定组件被放置在容器的何处。
该选项支持 N（北，代表上），E（东，代表右），S（南，代表下），W（西，代表左）、NW（左上）、NE（右上）、SW（左下），SE（右下）
CENTER（中，默认值）

expand：bool 值，指定当 父容器增大时才是否？拉伸组件

fill：设置组件是否沿水平或垂直方向填充，支持 NONE、X、Y、BOTH 四个值，其中 NONE 表示不填充，BOTH 表示沿着两个方向填充

side：设置组件的添加位置，可以设置为 TOP、BOTTOM、LEFT 或 RIGHT 这四个值其中之一

padx：指定组件在 X 水平方向上与其它组件的间距
pady：指定组件在 Y 垂直方向上与其它组件的间距

ipadx： 指定组件在水平方向 X 上的内部留白 (padding)
ipady： 指定组件在垂直方向 Y 上的内部留白 (padding)

'''

# 当程序界面比较复杂时，就需要使用多个容器(Frame) 分开布局，然后再将 Frame 添加到窗口中

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        # 创建第一个容器
        fm1 = Frame(self.master)
        # 该容器放在左边排列
        fm1.pack(side=LEFT, fill=BOTH, expand=YES)
        # 向 fm1 中添加三个按钮
        # 设置按钮从 顶部开始排列，而且按钮在 水平方向(X) 上填充
        Button(fm1, text='第一个').pack(side=TOP, fill=X, expand=True)
        Button(fm1, text='第二个').pack(side=TOP, fill=X,  expand=True)
        Button(fm1, text='第三个').pack(side=TOP, fill=X, expand=True)

        # 创建第二个容器
        fm2 = Frame(self.master)
        # 将该容器放在左边排列，就会紧挨着 fm1,水平间距设置为10
        fm2.pack(side=LEFT, padx=10, fill=BOTH, expand=True)
        #向 fm2 中添加三个按钮，从右到左开始排列,在垂直方向 Y上填充
        Button(fm2, text='第一个').pack(side=RIGHT, fill=Y, expand=True)
        Button(fm2, text='第二个').pack(side=RIGHT, fill=Y, expand=True)
        Button(fm2, text='第三个').pack(side=RIGHT, fill=Y, expand=True)

        #创建第三个容器
        fm3 = Frame(self.master)
        # 将该容器放在右边排列
        fm3.pack(side=RIGHT, padx=10, fill=BOTH, expand=True)
        # 向 fm3 中添加三个按钮，从下到上排列，在 垂直方向（Y） 上排列
        Button(fm3, text='第一个').pack(side=BOTTOM, fill=Y, expand=True)
        Button(fm3, text='第二个').pack(side=BOTTOM, fill=Y, expand=True)
        Button(fm3, text='第三个').pack(side=BOTTOM, fill=Y, expand=True)

def main():
    root = Tk()
    root.title('pack 布局')
    display = App(root)
    root.mainloop()


if __name__ == '__main__':
    main()

