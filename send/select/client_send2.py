'''
    完善聊天室窗口布局, 增加表情 图片 截屏 文件按钮
'''

import socket
import threading
import json  # json.dumps(some)打包   json.loads(some)解包
import tkinter
import tkinter.messagebox
from tkinter.scrolledtext import ScrolledText  # 导入多行文本框用到的包
from PIL import Image, ImageTk


def send(name):
    
    IP = '127.0.0.1'
    PORT = 9001
    user = name
    listbox1 = ''  # 用于显示在线用户的列表框
    ii = 0  # 用于判断是开还是关闭列表框
    users = []  # 在线用户列表
    chat = '----------群聊----------'  # 聊天对象, 默认为群聊



    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    if user:
        s.send(user.encode())  # 发送用户名
    else:
        s.send('no'.encode())  # 没有输入用户名则标记no

    # 如果没有用户名则将ip和端口号设置为用户名
    addr = s.getsockname()  # 获取客户端ip和端口号
    addr = addr[0] + ':' + str(addr[1])
    if user == '':
        user = addr

    ## 聊天窗口
    # 创建图形界面
    root = tkinter.Tk()
    root.title(user)  # 窗口命名为用户名
    root['height'] = 390
    root['width'] = 580
    root.resizable(0, 0)  # 限制窗口大小

    # 创建多行文本框
    listbox = ScrolledText(root)
    listbox.place(x=5, y=0, width=570, height=320)
    # 文本框使用的字体颜色
    listbox.tag_config('red', foreground='red')
    listbox.tag_config('blue', foreground='blue')
    listbox.tag_config('green', foreground='green')
    listbox.insert(tkinter.END, '欢迎进入聊天室!', 'blue')

    #emoticon
    # 四个按钮, 使用全局变量, 方便创建和销毁
    b1 = ''
    b2 = ''
    b3 = ''
    b4 = ''

    p1 = ImageTk.PhotoImage(file = '捂脸.png')
    p2 = ImageTk.PhotoImage(file = '奸笑.png')
    p3 = ImageTk.PhotoImage(file = '皱眉.png')
    p4 = ImageTk.PhotoImage(file = '机智.png')

    # 用字典将标记与表情图片一一对应, 用于后面接收标记判断表情贴图
    dic = {'aa**':p1, 'bb**':p2, 'cc**':p3, 'dd**':p4}
    ee = 0  # 判断表情面板开关的标志
    # 发送表情图标记的函数, 在按钮点击事件中调用
    def mark(exp):  # 参数是发的表情图标记, 发送后将按钮销毁
        global ee
        mes = exp + ':;' + user + ':;' + chat
        s.send(mes.encode())
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b4.destroy()
        ee = 0
    
    # 四个对应的函数
    def bb1():
        mark('aa**')
    def bb2():
        mark('bb**')
    def bb3():
        mark('cc**')
    def bb4():
        mark('dd**')
    def express():
        nonlocal b1, b2, b3, b4, ee
        if ee == 0:
            ee = 1
            b1 = tkinter.Button(root, command=bb1, image=p1,
                                relief=tkinter.FLAT ,bd=0)
            b2 = tkinter.Button(root, command=bb2, image=p2,
                                relief=tkinter.FLAT ,bd=0)
            b3 = tkinter.Button(root, command=bb3, image=p3,
                                relief=tkinter.FLAT ,bd=0)
            b4 = tkinter.Button(root, command=bb4, image=p4,
                                relief=tkinter.FLAT ,bd=0)

            b1.place(x=5, y=248)
            b2.place(x=75, y=248)
            b3.place(x=145, y=248)
            b4.place(x=215, y=248)
        else:
            ee = 0
            b1.destroy()
            b2.destroy()
            b3.destroy()
            b4.destroy()

    
    # 创建表情按钮
    eBut = tkinter.Button(root, text='表情', command=express)
    eBut.place(x=5, y=320, width=60, height=30)

    def picture():
        pass
    # 创建发送图片按钮
    pBut = tkinter.Button(root, text='图片', command=picture)
    pBut.place(x=65, y=320, width=60, height=30)

    def shot():
        pass
    # 创建截屏按钮
    sBut = tkinter.Button(root, text='截屏', command=shot)
    sBut.place(x=125, y=320, width=60, height=30)

    def file():
        pass
    # 创建文件按钮
    fBut = tkinter.Button(root, text='文件', command=file)
    fBut.place(x=185, y=320, width=60, height=30)

    # 创建多行文本框, 显示在线用户
    listbox1 = tkinter.Listbox(root)  
    listbox1.place(x=445, y=0, width=130, height=320)

    def users_online():
        nonlocal listbox1, ii
        if ii == 1:
            listbox1.place(x=445, y=0, width=130, height=320)
            ii = 0
        else:
            listbox1.place_forget()  # 隐藏控件
            ii = 1
    
    # 查看在线用户按钮
    button1 = tkinter.Button(root, text='在线用户', command=users_online)
    button1.place(x=505, y=320, width=70, height=30)

    # 创建输入文本框和关联变量
    a = tkinter.StringVar()
    a.set('')
    entry = tkinter.Entry(root, width=120, textvariable=a)
    entry.place(x=5, y=348, width=570, height=40)

    def send(*args):
        # 没有添加的话发送信息时会提示没有聊天对象
        users.append('----------群聊----------')  
        if chat not in users:
            tkinter.messagebox.showerror('发送失败', message = '没有聊天对象!')
            return
        if chat == user:
            tkinter.messagebox.showerror('发送失败', message = '不能私聊自己!')
            return
        mes = entry.get() + ':;' + user + ':;' + chat  # 添加聊天对象标记
        s.send(mes.encode())
        a.set('')  # 发送后清空文本框
    
    # 创建发送按钮
    button = tkinter.Button(root, text='发送', command=send)
    button.place(x=515, y=353, width=60, height=30)
    root.bind('<Return>', send)  # 绑定回车发送信息



    def private(*args):
        nonlocal chat
        # 获取点击的索引然后得到内容(用户名)
        indexs = listbox1.curselection()
        index = indexs[0]
        chat = listbox1.get(index)
        # 修改客户端名称
        if chat == '----------群聊----------':
            root.title(user)
            return       
        ti = user + '  -->  ' + chat
        root.title(ti)

    # 在显示用户列表框上设置绑定事件
    listbox1.bind('<ButtonRelease-1>', private)

    # 用于时刻接收服务端发送的信息并打印,
    def recv():
        nonlocal users
        while True:
            data = s.recv(1024)
            data = data.decode()
            # 没有捕获到异常则表示接收到的是在线用户列表
            try:
                data = json.loads(data)
                users = data
                listbox1.delete(0, tkinter.END)  # 清空列表框
                number = ('     在线人数: ' + str(len(data)) + ' 人')
                listbox1.insert(tkinter.END, number)
                listbox1.itemconfig(tkinter.END,fg='green', bg="#f0f0ff")
                listbox1.insert(tkinter.END, '----------群聊----------')
                listbox1.itemconfig(tkinter.END,fg='green')
                for i in range(len(data)):
                    listbox1.insert(tkinter.END, (data[i]))
                    listbox1.itemconfig(tkinter.END,fg='green') 
            except:
                data = data.split(':;')
                data1 = data[0].strip()  # 消息
                data2 = data[1]  # 发送信息的用户名
                data3 = data[2]  # 聊天对象
                #data [' liyuan：bb**', 'liyuan', '----------群聊----------']
                #        发消息的人 和消息   发送者     接收者
                markk = data1.split('：')[1]
                print(data)
                print(markk)
                # 判断是不是表情
                # 如果字典里有则贴图
                if markk in dic:
                    print("do something")
                    data4 = '\n' + data2 + '：'  # 例:名字-> \n名字：
                    if data3 == '----------群聊----------':
                        if data2 == '\n' + user:  # 如果是自己则将则字体变为蓝色
                            listbox.insert(tkinter.END, data4, 'blue')
                            listbox.image_create(tkinter.END, image=dic[markk])
                        else:
                            listbox.insert(tkinter.END, data4, 'green')  # END将信息加在最后一行
                            listbox.image_create(tkinter.END, image=dic[markk])
                    elif data2 == user or data3 == user:  # 显示私聊
                        listbox.insert(tkinter.END, data4, 'red')  # END将信息加在最后一行 
                        listbox.image_create(tkinter.END, image=dic[markk])
                else:
                    data1 = '\n' + data1
                    if data3 == '----------群聊----------':
                        if data2 == '\n' + user:  # 如果是自己则将则字体变为蓝色
                            listbox.insert(tkinter.END, data1, 'blue')
                        else:
                            listbox.insert(tkinter.END, data1, 'green')  # END将信息加在最后一行
                    elif data2 == user or data3 == user:  # 显示私聊
                        listbox.insert(tkinter.END, data1, 'red')  # END将信息加在最后一行 
                listbox.see(tkinter.END)  # 显示在最后
            
        
    r = threading.Thread(target=recv)
    r.start()  # 开始线程接收信息

    root.mainloop()
    s.send(b'quit')
    s.close()  # 关闭图形界面后关闭TCP连接
send('wangwu')
