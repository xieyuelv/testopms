#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：testopms -> addproject.py
@IDE    ：PyCharm
@Author ：Mr. XieYueLv
@Date   ：2021/7/24 23:09
@Desc   ：
=================================================='''
import random
import requests
import datetime
from apitest.login.loginopms import Login
from common.read_yml import Readyaml

host = Readyaml().readyaml()["host"]

name = "谢谢" + str(random.sample("abcdefghijklmnopqrtswxyz", 5))
aliasname = "谢谢" + str(random.sample("1234567890", 4))
started = datetime.datetime.now().strftime("%Y-%m-%d")
ended = (datetime.datetime.now() + datetime.timedelta(days=3)).strftime("%Y-%m-%d")
desc = random.choice("qwertyuiopasdfghjklzxcvbnm")

class Addproject():

    def __init__(self, res=requests.sessions.session(), name=name, aliasname=aliasname, started=started, ended=ended, desc=desc):
        self.res = res
        self.name = name
        self.aliasname = aliasname
        self.started = started
        self.ended = ended
        self.desc = desc

    def addproject(self):
        url = host + "/project/add"
        data = {"name": self.name,
                "aliasname": self.aliasname,
                "started": self.started,
                "ended": self.ended,
                "desc": self.desc,
                "id": 0}
        Login(res=self.res).login()
        re = self.res.post(url=url, data=data)
        return re.json()

if __name__ == '__main__':
    # Login().login()
    print(Addproject().addproject())