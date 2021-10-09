#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：testopms -> searchproject.py
@IDE    ：PyCharm
@Author ：Mr. XieYueLv
@Date   ：2021/7/25 13:51
@Desc   ：
=================================================='''
from apitest.login.loginopms import Login
import requests
host = "http://119.45.58.158:8289"
res = requests.sessions.session()

def search_project():
    url = host + "/project/manage?status=&keywords=谢谢"
    Login(res=res).login()
    re = res.get(url).text
    print(type(re))
    return re

if __name__ == '__main__':
    print(search_project())








