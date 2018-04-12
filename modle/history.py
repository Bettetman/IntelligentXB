#!/usr/bin/evn python
#coding:utf-8
from modle.account import Account
from modle.admin import Admin
class History():
    def __init__(self):
   #     self.__account = Account()
        self.__admin = Admin()
        self.accountNum = ""
        
    def getTableName(self,):
        if self.accountNum =="":
            return "18428396620"#self.__account.getTelNum
    
    def getSQLData(self,dataNum=100):
        AdminString = "select * from tableNum limit data"
        AdminString = AdminString.replace('Num', self.getTableName())
        AdminString = AdminString.replace('data',str(dataNum))
        return self.__admin.getHistoryData(AdminString)
    
    def writeInBuffer(self,OneLogin):
        self.__admin.writeBuffer(OneLogin,self.getTableName)
    
    def getBufferData(self):
        return self.__admin.getBuffer()
    
    def insertOneData(self,*OneLogin):
                time = OneLogin[0]
                xiaobing = OneLogin[1]
                your = OneLogin[2] 
                insertString = "insert into tableNUM (saytime,xiaobing1,your) values('aa','bb','cc')"
                insertString = insertString.replace('NUM',self.getTableName)
                insertString = insertString.replace('aa', time)
                insertString = insertString.replace('bb',xiaobing)
                insertString = insertString.replace('cc',your)
                self.__admin.insertHistoryData(insertString)