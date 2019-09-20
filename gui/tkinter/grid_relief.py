#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     ：2019/7/22 14:54
# @Author   ：joey
# @File     ：grid_relief.py
# @Software ：PyCharm

from tkinter import *

RELIEF = ["flat", "raised", "sunken", "solid", "ridge", "groove"]

class   App:
    def __init__(self, master):
        self.master = master
        self.init_widgets()

    def init_widgets(self):
        # label frame
        fm1 = Frame(self.master)
        # 将 fm1 放在 TOP，垂直距离 10
        fm1.pack(side=TOP, pady=10)

        rows = 0
        for i in range(len(RELIEF)):
            label = Label(fm1, relief=RELIEF[i], text=RELIEF[i], borderwidth=5, width=5, height=5, padx=10)
            label.grid(row=rows, column=i % len(RELIEF))

        # button frame
        fm2 = Frame(self.master)
        fm2.pack(side=TOP, pady=10)
        for i in range(len(RELIEF)):
            label = Button(fm2, relief=RELIEF[i], text=RELIEF[i], borderwidth=5, width=5, height=5, padx=10)
            label.grid(row=rows, column=i % len(RELIEF))


def main():
    root = Tk()
    root.title('Grid RELIEF')
    App(root)
    root.mainloop()

if __name__ == '__main__':
    main()
