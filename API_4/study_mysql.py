# -*- coding: utf-8 -*-
#@contact: 406975460@qq.com
#@Author: zyl
#@file: study_mysql.py
#@Time: 2021/8/3 15:11

import pymysql

# 1、建立连接--数据库的连接信息
host="test.lemonban.com"
user="future"
password="123456"
port=3306
mysql=pymysql.connect(host=host,user=user,password=password,port=3306)
# 2、新建一个查询页面
cursor=mysql.cursor()
# 3、编写sql
sql='SELECT max(mobile_phone) FROM futureloan.member'
# 4、执行结果
cursor.execute(sql)
# 5、查看结果
result=cursor.fetchone()
print(type(result),result)
print(type(result),result[0])
# 6、关闭查询
cursor.close()
# 7、关闭数据库连接
mysql.close()

# tuple:元祖