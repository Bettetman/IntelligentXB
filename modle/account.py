#!/usr/bin/evn python
#coding:utf-8
from modle.admin import Admin
from history import History
import hashlib
class Account():
    def __init__(self,telNum="",passWord=""):
        self.__telNum = telNum
        self.__passWord = passWord
        self.__admin = Admin()
        self.his  = History()
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
            if self.isInSQL()==False:
                self.__admin.insertSQL(tel, password)
                print "插入数据库成功"
                return True
            else:
                print "该账户已经存入了数据库"
                return False
        
    def isInSQL(self):
        if self.__passWord=="" or self.__telNum =="":
            print "你没有设置帐号"
            return False
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
#         while True:
#             t=raw_input("please cin your account:")
#             try:
#                 x=int(t)
#                 if type(x)==int:
#                     break
#             except:
#                     print "must cin a telnum"
        x=raw_input("please cin your account:")
        self.__telNum =str(x)
        password1 = raw_input("please cin your password:")
        self.__passWord = password1
    def delectaAccount(self,tel):
        saveCurrcentTel = self.getTelNum
        self.__telNum = tel
        if self.isInSQL():
            self.__admin.delectAccountSQL(tel)
        else:
            print "数据库中没有改账户"
        self.__telNum = saveCurrcentTel
            
        
    def startInit(self):
        self.LoginAccount()
        flag1 = True
        flagReturn = True
        while flag1:
            loginStr = raw_input("你是否要登陆？是输入OK，不是输入NO，登陆输入Sign")
            if loginStr.lower() == "ok":   
                    if self.checkIsRight():
                        flag1 = False
                        flagReturn =True
                    else:
                        pass
            elif loginStr.lower()=="no":
                     flagReturn = False
                     flag1 =False
            elif loginStr.lower() =="sign":
                    self.save()
                    flagReturn = False
            else:
                 flag1 =False
                 flagReturn =False
        return flagReturn