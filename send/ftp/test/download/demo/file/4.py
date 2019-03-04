from tkinter import *

from socket import *
'''
Listbox组件根据selectmode选项提供了四种不同的选择模式：SINGLE(单选）
BROWSE（也是单选，但推动鼠标或通过方向键可以直接改变选项）
MULTIPLE（多选）和EXTENDED（也是多选，但需要同时按住Shift和Ctrl或拖动鼠标实现
），默认是BROWSE
'''
root = Tk()
theLB = Listbox(root,height=11)#height=11设置listbox组件的高度，默认是10行。
theLB.pack()


#创建套接字
sockfd = socket()

#发起连接请求
server_addr = ('127.0.0.1',8888)
sockfd.connect(server_addr)

#发送请求服务器文件列表
filelist='get'
sockfd.send(filelist.encode())



#接收到文件列表后生成listbox
for item in['公鸡','母鸡','小鸡','火鸡','战斗机',]:
    theLB.insert(END,item)  #END表示每插入一个都是在最后一个位置

#定义下载按钮，向服务器发送下载请求

theButton = Button(root,text='下载',command=lambda x=theLB:x.delete(ACTIVE))
theButton.pack()
mainloop()
