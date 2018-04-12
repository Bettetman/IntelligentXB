#!/usr/bin/evn python
#coding:utf-8
import socket
ip_port = ("127.0.0.2",9997)
client2 = socket.socket()
client2.connect(ip_port)
while True:
    data  =  client2.recv(1024)
    print data 
    inputSendData= raw_input("client:")
    client2.send(inputSendData)
    if inputSendData.lower()=="exit":
        client2.close()
