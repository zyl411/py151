# -*- coding: utf-8 -*-
#@contact: 406975460@qq.com
#@Author: zyl
#@file: test_register.py
#@Time: 2021/8/3 17:48


import unittest

from ddt import ddt, data

from API_4.common import contants
from API_4.common import do_excel
from API_4.common.http_request import HTTPRequest2
from API_4.common import do_mysql


@ddt
class RegisterTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'register')
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HTTPRequest2()
        cls.mysql=do_mysql.DoMysql()

    @data(*cases)
    def test_register(self, case):
        if case.data.find('register_mobile'):
            sql='select max(mobile_phone) from futureloan.member'  #--数据库查出来是18999923670
            max_phone=self.mysql.fetch_one(sql)[0]  #查询最大手机号码，取的值是字符串
            # 最大手机号码+1
            print(max_phone)
            max_phone=int(max_phone)+1
            print(case.data)
            print(type(case.data))
            case.data=case.data.replace("register_mobile",str(max_phone))  #替换参数值
            print(case.data)
        resp = self.http_request.request(case.method, case.url, case.data)

        try:
            self.assertEqual(case.expected, resp.text)
            self.excel.write_result(case.case_id + 1, resp.text, 'PASS')
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, resp.text, 'FAIL')
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
        cls.mysql.close()

