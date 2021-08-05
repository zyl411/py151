# -*- coding: utf-8 -*-
#@contact: 406975460@qq.com
#@Author: zyl
#@file: do_mysql.py
#@Time: 2021/8/3 17:12
import pymysql

class DoMysql:

    def __init__(self):
        host = "test.lemonban.com"
        user = "future"
        password = "123456"
        port = 3306
        self.mysql = pymysql.connect(host=host, user=user, password=password, port=port)
        self.cursor=self.mysql.cursor()

    def fetch_one(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def fetch_all(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()  #关闭游标
        self.mysql.close()  #关闭连接

if __name__ == '__main__':
    mysql=DoMysql()
    result=mysql.fetch_one('SELECT max(mobile_phone) FROM futureloan.member')
    print(result[0])
    print(type(result[0]))
    mysql.close()