# -*- coding: utf-8 -*-
#@contact: 406975460@qq.com
#@Author: zyl
#@file: learn_eval_json.py
#@Time: 2021/7/30 17:33

# python与json的区别有3个：
# python--None、False、True;;;json--null、false、true
# json序列化与反序列化
# 1、序列化--将dict序列化为str或者file
# dumps(),dump()
# 2、反序列化--将str或者file反序列化为dict
# loads(),load()
# 备注：dumps()和loads()操作字符串；dump()和load()操作文件

import json
params='{"status":1,"code":"10001","data":null,"msg":"登录成功"}'  #这个是json，所有的元素必须都用双引号
d=json.loads(params)

print(type(d),d)
# 打印的结果为：<class 'dict'> {'status': 1, 'code': '10001', 'data': None, 'msg': '登录成功'}--从json变为了字典
