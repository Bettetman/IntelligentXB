#!/usr/bin/evn python
#coding:utf-8
from test.xiaobing import Xiaobing 
from modle.account import Account
from modle.admin import Admin
from modle.history import History
def handle():
    #账户测试过
#     acount1 = Account()
#     acount1.LoginAccount()
#     acount1.checkIsRight()
#        
    #测试小冰
#     xb = Xiaobing()
#     print xb.respand("wang")
    
    #测试历史记录
    his = History()
  
    his.getBufferData()
 
#     print his.getSQLData()
#     his.writeInBuffer(("2015-11-11 12:22:07", "ok", "see you"))
         
if __name__ == '__main__':
    handle()
     
