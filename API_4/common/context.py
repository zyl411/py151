# -*- coding: utf-8 -*-
#@contact: 406975460@qq.com
#@Author: zyl
#@file: context.py
#@Time: 2021/8/4 15:27

import re

from API_4.common.config import config
def replace(data):
    p = "#(.*?)#"  # 正则表达式
    while re.search(p, data):
        print(data)
        m = re.search(p, data)  # 从任意位置开始找，找第一个就返回Match object, 如果没有找None
        g = m.group(1)  # 拿到参数化的KEY
        v = config.get('data', g)  # 根据KEY取配置文件里面的值
        print(v)
        # 记得替换后的内容，继续用data接收
        data = str(re.sub(p, v, data, count=1)) # 查找替换,count查找替换的次数

    return data
