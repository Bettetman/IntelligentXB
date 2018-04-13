#!/usr/bin/evn python
#coding:utf-8
from modle.account import Account
from modle.admin import Admin
from modle.history import History
from utility.HandFile import  FileHelper
import time
def handle():
    #账户测试过
#      acount1 = Account()
#      print acount1.startInit()
#      acount1.delectaAccount("17780614923")
#        
    #测试小冰
#     xb = Xiaobing()
#     print xb.respand("wang")
    
    #测试历史记录
   #his = History()
  
    #his.getBufferData()
 
#     print his.getSQLData()
#     his.writeInBuffer(("2015-11-11 12:22:07", "ok", "see you"))
    #测试Admin
    ###
    #测试filehelper
    fp1= FileHelper()
    fp1.readFile_returnList()

if __name__ == '__main__':
     handle()
