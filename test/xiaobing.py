#!/usr/bin/evn python
#coding:utf-8
from modle.admin import Admin
from collections import Counter
class Xiaobing():
    def __init__(self,name = "xiaobing"):
       self.name = name 
       self.__admin = Admin()
       print "创建",self.name,"成功"
       
    def setName(self,value):
        self.name = value
        
    def respand(self,giveString): 
        answer =self.__admin.getAllSQLData(giveString, 1)
        if answer==():
            list_answer = []
            list_giveStr = giveString.split()
            list_getanswer = []
            if len(list_giveStr) !=1 :
                for i in list_giveStr:
                    answer = self.__admin.getAllSQLData(i, 1)
                    if answer == ():
                        pass
                    else:
                        list_answer.append(answer)
                
                for item in list_answer:
                    for value in item:
                         print list_getanswer.append(value[1])
                
                return Counter(list_getanswer).most_common(1)[0][0]
                    
            else:
                return "i dont know how to answer"
        else:
            return answer
    def addInf(self):
        pass