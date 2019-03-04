'''
    没有改动
'''
from select import select 
import socket
import threading
import queue
import json  # json.dumps(some)打包   json.loads(some)解包

IP = '0.0.0.0'
PORT = 9001

que = queue.Queue()  # 用于存放客户端发送的信息的队列
users = []  # 用于存放在线用户的信息  [conn, user, addr]
lock = threading.Lock()  # 创建锁, 防止多个线程写入数据的顺序打乱

# 用于接收所有客户端发送信息的函数
def tcp_connect(conn, addr):
    # 连接后将用户信息添加到users列表
    user = conn.recv(1024)  # 接收用户名
    user = user.decode()
    if user == 'no':
        user = addr[0] + ':' + str(addr[1])
    users.append((conn, user, addr))
    print('新连接:', addr, ':', user, end='')  # 打印用户名
    d = onlines()  # 有新连接则刷新客户端的在线用户显示
    recv(addr, d)  #save msg to que
    try:
        while True:
            data = conn.recv(1024)
            data = data.decode()
            print(data)
            if data == 'quit':
                #print(666)
                conn.close()
            else:
                recv(addr, data)  # 保存信息到队列

            
        conn.close()
    except:
        print(user + ' 断开连接')
        delUsers(conn, addr)  # 将断开用户移出users
        conn.close()

# 判断断开用户在users中是第几位并移出列表, 刷新客户端的在线用户显示
def delUsers(conn, addr):
    a = 0
    for i in users:
        if i[0] == conn:
            users.pop(a)
            print('剩余在线用户: ', end='')  # 打印剩余在线用户(conn)
            d = onlines()
            recv(addr, d)
            #print(d)
            break
        a += 1

# 将接收到的信息(ip,端口以及发送的信息)存入que队列
def recv(addr, data):
    lock.acquire()
    try:
        que.put((addr, data))
    finally:
        lock.release()

# 将队列que中的消息发送给所有连接到的用户
def sendData():
    while True:
        if not que.empty():
            data = ''
            message = que.get()  # 取出队列第一个元素
            print(message)
            print("把发送出去的消息存在芒果DB中")#bb**:;liyuan:;zhangsan
            if isinstance(message[1], str):  # 如果data是str则返回Ture
                for i in range(len(users)):
                    #user[i][1]是用户名, users[i][2]是addr, 将message[0]改为用户名
                    for j in range(len(users)):
                        if message[0] == users[j][2]:                            
                            data = ' ' + users[j][1] + '：' + message[1]
                            break      
                    users[i][0].send(data.encode())
            data = data.split(':;')[0]
            #print(data)
            if isinstance(message[1], list):  # 同上
                # 如果是list则打包后直接发送  
                data = json.dumps(message[1])
                for i in range(len(users)):
                    users[i][0].send(data.encode())
            

# 将在线用户存入online列表并返回
def onlines():
    online = []
    for i in range(len(users)):
        online.append(users[i][1])
    return online





               
s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
s.bind( (IP, PORT) )
s.listen(5)
print('tcp server is running...')
#添加关注列表
rlist = [s]
wlist = []
xlist = [s]

q = threading.Thread(target=sendData)
q.start()
while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    #遍历三个列表确定哪个IO发生
    for r in rs:
        #如果遍历到s说明s就绪则有客户端发起连接
        if r is s:
            conn,addr = r.accept()
            print("Connect from",addr)
            rlist.append(conn)
        #客户端连接套接子就绪,则接收消息
        else:
            tcp_connect(conn,addr)
conn.close()


