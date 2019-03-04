
import socket
import threading
import json  # json.dumps(some)打包   json.loads(some)解包
import tkinter as tk
import tkinter.messagebox
from tkinter.scrolledtext import ScrolledText  # 导入多行文本框用到的包

from tkinter import StringVar

def send():
    m=555555
    #消息接受
    def recv_msg():
        pass
    msg = tk.Tk()
    msg.title('Chat')
    msg.geometry('500x500')                 #窗口大小*
    msg.resizable(width=False, height=False)

    #响应函数
    def send_msg():
        print(dir(msg.protocol()))
        #开启两个线程，一个用来不断地接收服务器的消息，另一个用来给服务器

        pass
    def donothing(*e):
        nonlocal m
        print(m)
        msg.destroy()
        pass
    msg.protocol("WM_DELETE_WINDOW", donothing)

    text_send = StringVar()

    text_chat = tk.Text(msg, width=65, height=20).place(x=20,y=60)
    entry_send = tk.Entry(msg,textvariable=text_send, bg="white").place(x=20,y=350,width=460, height=80)
    button_send=tk.Button(msg,text='send',command= send_msg ).place(x=190,y=450,width=110)

    msg.mainloop()

send()
