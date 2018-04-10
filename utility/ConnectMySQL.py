#!/usr/bin/evn python
#coding:utf-8
import MySQLdb 
from Config import SQLConfig as MySQLconfig
from _mysql import NULL
class SQLHelper():
      
        def __init__(self):
            print "启动数据库成功"
        #查询数据
        def GetSQLInformationTuple(self,sqlString):
            try:
                conn =MySQLdb.connect(**MySQLconfig)
                cur = conn.cursor()
#               cur = con.cursor(cursorclass = MySQLdb.cursors.DictCursor) 以字典的形式获取数据
                reCount=cur.execute(sqlString)
                nSet = cur.fetchall()
         #       print "查询到：",reCount,"条信息"
                return nSet
            except MySQLdb.Error,e:
                print e 
            finally:
                if cur!=NULL:
                    cur.close()
                if conn!=NULL:
                    conn.close()
        def GetSQLInformationDic(self,sqlString):
            try:
                conn =MySQLdb.connect(**MySQLconfig)
                cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
                reCount=cur.execute(sqlString)
                nSet = cur.fetchall()
                print "查询到：",reCount,"条信息"
                return nSet
            except MySQLdb.Error,e:
                print e 
            finally:
                if cur!=NULL:
                    cur.close()
                if conn!=NULL:
                    conn.close()
        def GetSQLOneInformation(self,sqlString):
            try:
                conn =MySQLdb.connect(**MySQLconfig)
                cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
                reCount=cur.execute(sqlString)
                nSet = cur.fetchone()
                print "查询到：",reCount,"条信息"
                return nSet
            except MySQLdb.Error,e:
                print e 
            finally:
                if cur!=NULL:
                    cur.close()
                if conn!=NULL:
                    conn.close()
        
        #插入数据
        def insertSQL(self,sqlString):
            try:
                conn =MySQLdb.connect(**MySQLconfig)
                cur = conn.cursor()
                reCount = cur.execute(sqlString)
                conn.commit()
            except MySQLdb.Error,e:
                print e 
            finally:
                if cur!=NULL:
                    cur.close()
                if conn!=NULL:
                    conn.close()
                
            