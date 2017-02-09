# http://pythonstudy.xyz/python/article/111-Tkinter-%EC%9D%B4%EB%B2%A4%ED%8A%B8
#
#

import tkinter
from tkinter import *


def key_pressed(event):
    return True


def click_c(event):
    return True


def main():
    window = tkinter.Tk()
    window.title("post-it")

    text = tkinter.Text(window)
    text.insert("1.0", "Write a code to save text...")

    if text.bind("<Button-1>", click_c):
        print("hello")
        print(str(text.get("1.0", END)))

    # text.bind("<Key>", key_pressed)
    text.pack()
    window.mainloop()


if __name__ == '__main__':
    main()
