#!/usr/bin/evn python
#coding:utf-8
import  SocketServer
from utility.Config import IpConfig as ip_port
class Myserver(SocketServer.BaseRequestHandler):
    def setup(self):
        pass

    def handle(self):
        conn = self.request
        print conn 
        conn.send("hello")
        flag = True
        while flag:
            data = conn.recv(1024)
            if data.lower() !="exit":
                print data
                conn.send("SB")
            else: 
                flag = False

    def finish(self):
        pass
    
if __name__ == '__main__':
    sk = SocketServer.ThreadingTCPServer(ip_port[0],Myserver)
    sk.serve_forever()
    