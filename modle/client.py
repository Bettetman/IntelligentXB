#!/usr/bin/evn python
#coding:utf-8
import socket
from account import Account
import time
class Client():
    def __init__(self,):
        self.__ip_port = ('127.0.0.2',9997)
    def startaClient(self):
        account1 = Account()
        if account1.startInit():
            client2 = socket.socket()
            client2.connect(self.__ip_port)
            while True:
                getData  =  client2.recv(1024)
                print getData 
                inputSendData= raw_input("%s client:"%account1.getTelNum)
                timeData =  time.strftime("%Y-%m-%d %X", time.localtime())
                client2.send(inputSendData)
                account1.his.writeInBuffer((timeData, getData, inputSendData))
                if inputSendData.lower()=="exit":
                    client2.close()
        else:
            print "启动服务器失败"
if __name__ == '__main__':
     Client().startaClient()
