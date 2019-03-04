# -*- coding:utf-8 -*-
# file: TkinterCanvas.py
#
import tkinter         # 导入Tkinter模块
from PIL import Image, ImageTk
from tkinter.scrolledtext import ScrolledText  # 导入多行文本框用到的包 
root = tkinter.Tk()
root['height'] = 390
root['width'] = 580
root.resizable(0, 0)  # 限制窗口大小
canvas = tkinter.Canvas(root,
    width = 580,      # 指定Canvas组件的宽度
    height = 390,      # 指定Canvas组件的高度
    bg = 'white')      # 指定Canvas组件的背景色
#im = Tkinter.PhotoImage(file='img.gif')     # 使用PhotoImage打开图片
image = Image.open('img.png')
im = ImageTk.PhotoImage(image)
 
canvas.create_image(300,50,image = im)      # 使用create_image将图片添加到Canvas组件中
canvas.create_text(302,77,       # 使用create_text方法在坐标（302，77）处绘制文字
   text = 'Use Canvas'      # 所绘制文字的内容
   ,fill = 'gray')       # 所绘制文字的颜色为灰色
canvas.create_text(300,75,
   text = 'Use Canvas',
   fill = 'blue')
canvas.pack()         # 将Canvas添加到主窗口
a = tkinter.StringVar()
a.set('')
listbox = ScrolledText(root)
#listbox.create_image(0,0,image = im)
listbox.place(x=5, y=0, width=570, height=320)
entry = tkinter.Entry(root, width=120, textvariable=a)
entry.place(x=5, y=348, width=570, height=40)


root.mainloop()
