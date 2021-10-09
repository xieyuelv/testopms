#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：testopms -> loginopms.py
@IDE    ：PyCharm
@Author ：Mr. XieYueLv
@Date   ：2021/7/24 上午10:54
@Desc   ：
=================================================='''
from common.read_yml import Readyaml
import requests
host = Readyaml().readyaml()["host"]

class Login():

    def __init__(self, res=requests.sessions.session(), username="lock", password="opms123456"):
        self.username = username
        self.password = password
        self.res = res

    def login(self):
        url = host + "/login"
        data = {"username":self.username, "password":self.password}
        res = self.res.post(url=url, data=data)
        print(res.json())
        return res.json()

if __name__ == '__main__':
    print(Login(username="lock",password="opms123456").login())