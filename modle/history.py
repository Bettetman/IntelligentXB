#!/usr/bin/evn python
#coding:utf-8
from modle.account import Account
from modle.admin import Admin
class History():
    def __init__(self):
        self.__account = Account()
        self.__admin = Admin()
        
    @property
    def getTableName(self):
        return self.__account.getTelNum
    
    def getData(self,dataNum=100):
        AdminString = "select * from table limit"
        return self.__admin.getHistoryData(AdminString)
    
    def insertData(self,*History):
        for row in History:
             for key in row:
                time = key[0]
                xiaobing = key[1]
                your = key[2] 
                insertString = "insert into tableNUM (saytime,xiaobing1,your) values('aa','bb','cc')"
                insertString = insertString.replace('NUM',self.getTableName)
                insertString = insertString.replace('aa', time)
                insertString = insertString.replace('bb',xiaobing)
                insertString = insertString.replace('cc',your)
                self.__admin.insertHistoryData(insertString)