# -*- coding: UTF-8 -*-
from socket import * 
import os,sys 
import pymysql


#客户端处理函数
def client_handler(c,db):
    print("客户端:",c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        if data.decode().split(' ')[4] !='R':
            c.send(b"no")
        else:
            #save data############################################################
            print("you have to save data",data.decode())
            cursor = db.cursor()
            sql='''insert into user(name,passwd)values ("%s","%s")'''%(data.decode().split(' ')[0] ,data.decode().split(' ')[1] )
            cursor.execute(sql)
            db.commit()
            c.send(b"ok")
    c.close()

#创建套接子
HOST = '0.0.0.0'
PORT = 8889
ADDR = (HOST,PORT)
db = pymysql.connect('localhost','root','123456','chat')
s = socket() #TCP套接字
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

#循环等待接收客户端连接请求
print("Listen to the port 8889....")
while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        sys.exit("退出服务器")
    except Exception as e:
        print("Error:",e)
        continue 
    
    #创建新的进程处理客户端请求
    pid = os.fork()

    if pid == 0:
        p = os.fork()
        if p == 0: #二级子进程
            s.close()
            client_handler(c,db) #处理具体请求
            sys.exit(0) #子进程处理完请求即退出
        else:
            os._exit(0)
    #父进程或者创建进程失败都继续等待下一个客户端连接
    else:
        c.close()
        os.wait()

