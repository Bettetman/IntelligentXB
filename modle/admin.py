#!/usr/bin/evn python
#coding:utf-8
from utility.ConnectMySQL import  SQLHelper
from utility.HandFile import FileHelper
class Admin(object):
    def __init__(self):
    #拿数据的接入工具
        self.__SqlHelper = SQLHelper()
        self.__FileHelper = FileHelper()
     
    #操作xiaobing表
    def getSQLData(self,adminString):
        return self.__SqlHelper.GetSQLOneInformation(adminString)
    
    def getAllSQLData(self,adminString,select_returnkand=1):
        SQLString = "select * from xiaobing where `key` LIKE 'dd';"
        SQLString= SQLString.replace("dd",adminString)
#        print SQLString
        if(select_returnkand==1):
            return self.__SqlHelper.GetSQLInformationTuple(SQLString)
        else:
            return self.__SqlHelper.GetSQLInformationDic(SQLString)
        
    #操作account表    
    def checkInSql(self,name):
        sqlString = "select * from accountlogin where telNum= 'name'".replace("name", name)
        print sqlString
        return self.__SqlHelper.GetSQLOneInformation(sqlString)
    
    def insertSQL(self,tel,password):
        sqlString ="INSERT INTO accountlogin (telNum, PassWord) VALUES ('kk', 'aa');".replace('aa', password)
        sqlString = sqlString.replace('kk', tel)
        self.__SqlHelper.insertSQL(sqlString)

    #操作历史数数据表
    def getHistoryData(self,AdminString):
        return   self.__SqlHelper.GetSQLInformationDic(AdminString)
    
    def insertHistoryData(self,AdminString):
        self.__SqlHelper.insertSQL(AdminString)
        
    #操作文件
    def writeBuffer(self,getBufferString):   
        if self.__FileHelper.writeFile(getBufferString) is None:
            pass
        else:
            self.__FileHelper.reSetBufferNum()
            #保存数据从文件缓存区到数据库 同时清空缓存区
            pass
            self.__FileHelper.emptiedBuffer()
            self.__FileHelper.writeFile(getBufferString)
        
    def getBuffer(self):
        return self.__FileHelper.readFile_returnList()
        