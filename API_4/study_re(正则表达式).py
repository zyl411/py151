# -*- coding: utf-8 -*-
#@contact: 406975460@qq.com
#@Author: zyl
#@file: study_re(正则表达式).py
#@Time: 2021/8/4 15:46

import re

data='{"mobile_phone":"normal_user","pwd":"normal_pwd"}'

p="normal_user"
m=re.search(p,data)
print(m)