#coding=utf-8

import socket

HOST = '192.168.20.29'
PORT = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print 'Server start at: %s:%s' %(HOST, PORT)
print 'wait for connection...'

while True:
    conn, addr = s.accept()
    print 'Connected by ', addr

    while True:
    	conn.send("点点滴滴")

        #data = conn.recv(1024)
        #print data

# conn.close()