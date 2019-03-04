from tkinter import *

from socket import *
import json
import time 
import os
import sys
'''
Listbox组件根据selectmode选项提供了四种不同的选择模式：SINGLE(单选）
BROWSE（也是单选，但推动鼠标或通过方向键可以直接改变选项）
MULTIPLE（多选）和EXTENDED（也是多选，但需要同时按住Shift和Ctrl或拖动鼠标实现
），默认是BROWSE
'''
#创建套接字
sockfd = socket()

#发起连接请求
server_addr = ('127.0.0.1',8888)
sockfd.connect(server_addr)

#发送请求服务器文件列表
request='get'
sockfd.send(request.encode())
fl = sockfd.recv(1024)
filelist=json.loads(fl.decode())
print(filelist)



root = Tk()
theLB = Listbox(root,height=11)#height=11设置listbox组件的高度，默认是10行。
theLB.pack()






#接收到文件列表后生成listbox
for item in filelist:
    theLB.insert(END,item)  #END表示每插入一个都是在最后一个位置

#定义下载按钮，向服务器发送下载请求
def select_file(event):
    print("entry the downlaod file func")
    a=theLB.get(theLB.curselection())  #a是选中的文件名称
    print(a)
    sockfd.send(a.encode())
    filepath = 'needfile/'
    with open(filepath+a, 'wb') as f:
        while True:
            data = sockfd.recv(1024)
            if not data:
                print("save finshed")
                break
            f.write(data)
    sockfd.close()
    sys.exit(0)


theLB.bind('<ButtonRelease-1>',select_file)


#theButton = Button(root,text='下载',command=lambda x=theLB:x.delete(ACTIVE))
#theButton.pack()
mainloop()
