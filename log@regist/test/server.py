from select import select 
from socket import *
import os,sys 
import pymysql

#传建数据库对象
db = pymysql.connect('localhost','root','123456','chat')

#准备要关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)

#load 查数据
def client_load(db,data,r):

    cursor = db.cursor()
    msrecv=data.decode()
    sql='''select * from user where name='%s' and passwd='%s';'''%(msrecv.split(' ')[0],msrecv.split(' ')[1])
    cursor.execute(sql)
    msg = cursor.fetchone()
    if msg == None:
        r.send(b'no')
    else:
        r.send(b'ok')

def client_regist(db):
    print("you have to save data",data.decode())
    cursor = db.cursor()
    sql='''insert into user(name,passwd)values ("%s","%s")'''%(data.decode().split(' ')[0] ,data.decode().split(' ')[1] )
    cursor.execute(sql)
    db.commit()

#添加关注列表
rlist = [s]
wlist = []
xlist = [s]

while True:
    #监控IO的发生
    rs,ws,xs = select(rlist,wlist,xlist)

    #遍历三个列表确定哪个IO发生
    for r in rs:
        #如果遍历到s说明s就绪则有客户端发起连接
        if r is s:
            c,addr = r.accept()
            print("Connect from",addr)
            rlist.append(c)
        #客户端连接套接子就绪,则接收消息
        else:
            #接收到客户端请求后的消息
            #mstr=str(msg[0])+' '+str(msg[1])+' '+'A2'+' '+'A3'+' '+'L'
            #
            #data_reg = str(user[0])+' '+str(user[1])+' '+str(user[2])+' '+str(user[3])+' '+'R'
            data = r.recv(1024)
            #判断data是l还是r
            if data.decode().split(' ')[4] =='R':
                client_regist(db)
                r.send(b"ok")
                rlist.remove(r)
                r.close()
            elif data.decode().split(' ')[4] =='L':
                client_load(db,data,r)
                rlist.remove(r)
                r.close()


