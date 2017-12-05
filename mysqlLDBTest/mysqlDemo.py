# coding:utf-8
'''
    Author:minning
    Date:2017/11/17
    代码目的：
    
'''
import MySQLdb

conn = MySQLdb.connect(host='localhost',
                       user='root',
                       passwd='1',
                       db='test')
cursor = conn.cursor()
cursor.execute("SELECT VERSION()")
row = cursor.fetchone()
print "server version:", row[0]
cursor.close()
conn.close()
