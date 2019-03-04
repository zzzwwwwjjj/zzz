# _*_ coding:utf-8 _*_
'''
    this a two threading server
    one is to send msg to client
    another is to recv msg to client
'''

import socket
import threading
import queue
import json  # json.dumps(some)打包   json.loads(some)解包

IP = '0.0.0.0'
PORT = 9000
users = []## save user socket  [conn, user, addr]

def tcp_connect(conn, addr):
    pass

def sendData():
    pass


s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
s.bind( (IP, PORT) )
s.listen(5)
print('tcp server is running...')
q = threading.Thread(target=sendData)
q.start()
while True:
    conn, addr = s.accept()
    t = threading.Thread(target=tcp_connect, args=(conn, addr))
    t.start()
s.close()
