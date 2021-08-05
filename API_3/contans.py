# -*- coding: utf-8 -*-
#@contact: 406975460@qq.com
#@Author: zyl
#@file: contans.py
#@Time: 2019/4/17 18:25



import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # API_3
print(base_dir)

case_file = os.path.join(base_dir, 'data', 'cases.xlsx')
print(case_file)
