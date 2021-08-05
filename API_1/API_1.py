# -*- coding: utf-8 -*-
#@contact: 406975460@qq.com
#@Author: zyl
#@file: API_1.py
#@Time: 2019/4/10 10:34


#注册：http://test.lemonban.com/futureloan/mvc/api/member/register
import requests
class HttpRequest:
#注册接口
    def register_request(self,method):
        register_url='http://test.lemonban.com/futureloan/mvc/api/member/register'
        param={'mobilephone': '18688773467', 'pwd': '123456'}
        resp = requests.get(register_url, params=param)
        print('响应码:',resp.status_code)
        print('响应cookies',resp.cookies)
        # print('响应cookies',resp.request._cookies)
#登录接口
    def login_request(self,method):
        login_url='http://test.lemonban.com/futureloan/mvc/api/member/login'
        param={'mobilephone': '18688773467', 'pwd': '123456'}
        resp1 = requests.post(login_url, data=param)
        print('响应码:',resp1.status_code)
        print('响应cookies',resp1.cookies)
        # print('响应cookies',resp.request._cookies)
        if resp1.status_code == 200:
            pass
        else:
            print('对不起，登陆失败，请校验账号名和密码')
        return resp1.cookies
#充值接口
    def recharge_request(self,method,cookies):
        recharge_url='http://test.lemonban.com/futureloan/mvc/api/member/recharge'
        param={'mobilephone': '18688773467', 'amount': '1000'}
        resp2 = requests.post(recharge_url, data=param,cookies=resp1.cookies)
        print('响应码:',resp2.status_code)
        print('响应报文:', resp2.text)

if __name__ == '__main__':
    resp=HttpRequest().register_request('get')
    resp1=HttpRequest().login_request('post')
    resp2=HttpRequest().recharge_request('post',resp1.cookies)


