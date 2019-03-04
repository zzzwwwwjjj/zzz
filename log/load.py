# -*- coding: UTF8 -*-
import tkinter as tk
from tkinter import StringVar
import tkinter.messagebox
#import sleep
from socket import *


import regist as r
#import client as c



load = tk.Tk()             #初始化Tk()
load.title("My First QQ load Program")#
load.geometry('300x240')                 #窗口大小*
load.resizable(width=False, height=False) #宽不可变, 高可变,默认为True
load['bg'] = 'gray'
#定义触发函数
def log():
    msg=[]
    msg.append(text_ip.get())
    msg.append(text_name.get())
    #创建套接字
    sockfd = socket()
    server_addr = ('127.0.0.1',8888)
    sockfd.connect(server_addr)
    mstr=str(msg[0])+' '+str(msg[1])
    if not msg[0] and msg[1]:
        tkinter.messagebox.showinfo('Warrning', 'Print something!')
    else:
        sockfd.send(mstr.encode())
        data = sockfd.recv(1024)
        print("From server:",data.decode())
        if data.decode()=='ok':
            print("ok")
            #c.client()  #  load send msg
            load.withdraw()
        else:
            tkinter.messagebox.showinfo('Warrning', 'Try again!')
    sockfd.close()

def reg():
    t = r.regist()







text_ip = StringVar()
text_name = StringVar()

lid =tk.Label(load, text="name:", bg="gray",anchor='w', font=("Arial", 12),justify='right', width=5, height=2).place(x=10,y=35,width=45,height=30)
lpasd =tk.Label(load, text="pswd:", bg="gray", anchor='w',font=("Arial", 12), width=5, height=2).place(x=10,y=85,width=45,height=30)



entry_ip=tk.Entry(load,textvariable=text_ip, bg = "white").place(x=60,y=35,width=180,height=30)
entry_name=tk.Entry(load,textvariable=text_name, bg="white").place(x=60,y=85,width=180,height=30)



button_log_in=tk.Button(load,text='Log in',command= log ).place(x=60,y=135,width=180)


button_send=tk.Button(load,text='Regist',command= reg ).place(x=20,y=210,width=80,height=20)

load.mainloop()  
