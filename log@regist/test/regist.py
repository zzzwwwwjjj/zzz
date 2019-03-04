# -*- coding: UTF-8 -*-
import tkinter as tk  #引用Tk模块
from tkinter import StringVar
import tkinter.messagebox
import sys
from socket import *
from multiprocessing import Process


def regist():
    reg = tk.Toplevel()             #初始化Tk()Toplevel
    reg.title("register")#
    reg.geometry('550x550')                 #窗口大小*
    reg.resizable(width=False, height=False) #宽不可变, 高可变,默认为True
    reg['bg'] = 'white'

    def send():
        user=[]
        user.append(v1n_ip.get())
        user.append(v1n_pswd.get())
        user.append(v1n_name.get())
        user.append(v1n_age.get())
        #regist comput if can send to server
        if not(user[1] and user[2] and user[3] and user[0]):
            tkinter.messagebox.showinfo('Warrning', 'some isue null')
        elif user[1] != user[2]:
            tkinter.messagebox.showinfo('Warrning', 'pswd not same!')
        else:
            #send msg to server
            data_reg = str(user[0])+' '+str(user[1])+' '+str(user[2])+' '+str(user[3])+' '+'R'
            print(data_reg)
            sockfd = socket()
            server_addr = ('127.0.0.1',8888)
            sockfd.connect(server_addr)
            sockfd.send(data_reg.encode())
            data_recv = sockfd.recv(1024)
            print("From server:",data_recv.decode())
            if data_recv.decode()=='ok':
                tkinter.messagebox.showinfo('Tips', 'Successfully regist in!')
            sockfd.close()
 
    def close():
        reg.destroy()

    lid =tk.Label(reg, text="Please input your name", bg="white",anchor='w', font=("Arial", 12),justify='right', width=5, height=2).place(x=100,y=40,width=200,height=30)
    lpasd =tk.Label(reg, text="Please input your paswd", bg="white", anchor='w',font=("Arial", 12), width=5, height=2).place(x=100,y=120,width=200,height=30)
    lname =tk.Label(reg, text="Please input paswd again", bg="white", anchor='w',font=("Arial", 12),justify='right', width=5, height=2).place(x=100,y=200,width=200,height=40)
    lage =tk.Label(reg, text="Please save your xxx", bg="white", anchor='w',font=("Arial", 12), width=5, height=2).place(x=100,y=280,width=200,height=40)




    v1n_ip = StringVar()
    v1n_pswd = StringVar()
    v1n_name = StringVar()
    v1n_age = StringVar()

    enid=tk.Entry(reg,text='input your id', textvariable=v1n_ip,bg="white").place(x=100,y=70,width=200,height=30)
    enpasd=tk.Entry(reg,text='input your address',textvariable=v1n_pswd, bg="white").place(x=100,y=150,width=200,height=30)
    enname=tk.Entry(reg,text='input your name', textvariable=v1n_name,bg="white").place(x=100,y=230,width=200,height=30)
    enage=tk.Entry(reg,text='save your age',textvariable=v1n_age, bg="white").place(x=100,y=310,width=200,height=30)
    bconf=tk.Button(reg,text='Confirm',command=send).place(x=330,y=400,width=200,height=40)
    bback=tk.Button(reg,text='Back',command=close).place(x=330,y=460,width=200,height=40)
    #reg.mainloop()         #进入消息循环





#regist()
#测试启动是否成功
#if __name__ == "__main__":
#
#    t = MyRegist(target=regist)
#    t.start()
#    t.join()





