#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     ：2019/7/22 17:23
# @Author   ：joey
# @File     ：place.py
# @Software ：PyCharm


from tkinter import *
import random

class App:
    def __init__(self, master):
        self.master = master
        self.init_widgets()

    def init_widgets(self):
        books = ('疯狂Python讲义', '疯狂Java讲义', '疯狂Ruby讲义', '疯狂Lua讲义','疯狂Go讲义')
        for i in range(len(books)):
            # 生成三个随机数配色
            ct = [random.randrange(256) for x in range(3)]
            grayness = int(round(0.299 * ct[0] + 0.587 * ct[1] + 0.114 * ct[2]))
            # 将元组中3个随机数格式化成16进制数,转成颜色格式
            bg_color = "#%02x%02x%02x" % tuple(ct)

            # 创建 label，设置 background, frontground
            lb = Label(self.master, text=books[i], fg='White' if grayness < 120 else 'Black', bg=bg_color)
            # 使用 place 来设置该 Label 的大小和位置
            lb.place(x=20, y=36 + i*36, width=180, height=30)
def main():
    root = Tk()
    root.title('Place 布局')
    App(root)
    root.mainloop()

if __name__ == '__main__':
    main()

