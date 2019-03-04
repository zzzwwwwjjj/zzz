from socket import * 
from threading import Thread 
import time
import sys 
import os
import json
import os.path
filePath = 'file'
flna=os.listdir(filePath)

#发送数据给客户端
def send_file(filepath):
    filepath=filepath
    print("this is a send func")
    with open(filepath, 'rb') as f:
        while True:
            a = f.read(1024)
            if not a:
                break
            c.send(a)
    time.sleep(0.1)


#客户端处理函数
def handler(c):
    print("Connect from",c.getpeername())

    while True:

        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        if data.decode()=='get':
            filename=json.dumps(flna)
            c.send(filename.encode())
            print("filename send ok")
            #请求文件列表
            needfile=c.recv(1024)
            nf=needfile.decode()
            print(nf)
            print("this is a recv file begin to send file")
            print(needfile.decode())
            folder = 'file/'
            filepath=folder + nf
            print("begin to send file")
            print(needfile)
            send_file(filepath)
            c.close()
            break
    c.close()

#创建套接子
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)

#接收客户端请求
while True:
    try:
        print('server is on,waiting for a connection')
        c,addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit("服务器退出")
    except Exception as e:
        print("服务端异常:",e)
        continue 
    
    #创建线程
    t = Thread(target=handler,args=(c,))
    #t.setDaemon(True)
    t.start()