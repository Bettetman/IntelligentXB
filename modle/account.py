#!/usr/bin/evn python
#coding:utf-8
from modle.admin import Admin
import hashlib
class Account():
    def __init__(self,telNum="",passWord=""):
        self.__telNum = telNum
        self.__passWord = passWord
        self.__admin = Admin()
    
    @property
    def changePassWord(self):
        return self.__passWord
    @changePassWord.setter
    def changePassWord(self,value):
        self.__passWord = value
    
    @property
    def getTelNum(self):
        return self.__telNum
    
    def hashlibpassWord(self):
        hash  = hashlib.md5()
        hash.update(self.__passWord)
        t= hash.hexdigest()
        return t
    
    def save(self):
        if self.__passWord=="" or self.__telNum =="":
            print "你没有设置帐号"
            return False
        else:
            tel = self.getTelNum
            password = self.hashlibpassWord()
            if self.isInSQL():
                self.__admin.insertSQL(tel, password)
                print "插入数据库成功"
                return True
            else:
                print "该账户已经存入了数据库"
                return False
        
    def isInSQL(self):
        if self.__passWord=="" or self.__telNum =="":
            print "你没有设置帐号"
        else:
            name = self.getTelNum
            passwd = self.hashlibpassWord()
            if self.__admin.checkInSql(name) is None:
                return False
            else:
                return True
    def checkIsRight(self):   
        if self.isInSQL():
            t = self.__admin.checkInSql(self.getTelNum)
            print t.get("PassWord")
            if t.get("PassWord") == self.hashlibpassWord():
                print "通过验证"
                return True
            else:
                print "验证失败"
                return False
        else:
            print "验证失败"
            return False
        
    def LoginAccount(self):
        print "欢迎到登陆系统"
        while True:
            t=raw_input("please cin your account:")
            try:
                x=eval(t)
                if type(x)==int:
                    break
            except:
                    print "must cin a telnum"
        self.__telNum =str(x);
        password1 = raw_input("please cin your password:")
        self.__passWord = password1