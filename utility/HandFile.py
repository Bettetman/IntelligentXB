#!/usr/bin/evn python
#coding:utf-8
from utility.Config import FileNameConfig
import json
class FileHelper():
    def __init__(self):
        self.__maxBuffer = 5
        self.__currentBufferNum = 1
    
    def writeFile(self,writeInf):
        fileName = FileNameConfig[0]
        if(self.__currentBufferNum<self.__maxBuffer):
            with open(fileName,"a") as file:
#                 file.write(writeInf)
                json.dump(writeInf,file)
                file.writelines("\n")
                self.__currentBufferNum+=1
                print self.__currentBufferNum
        else:
            return self.__currentBufferNum
        
    def reSetBufferNum(self):
        self.__currentBufferNum = 0     
           
    def emptiedBuffer(self):
        fileName = FileNameConfig[0]
        with open(fileName,"w") as file:
            file.write("")    
                
    def readFile_returnList(self,fileName = FileNameConfig[0]):
         with open(fileName,"r") as fileinf:
              returnString = []
              for iline in   fileinf.readlines():
                  returnString.append(json.loads(iline))
              return returnString        