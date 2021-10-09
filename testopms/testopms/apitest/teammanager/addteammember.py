#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：testopms -> addteammember.py
@IDE    ：PyCharm
@Author ：Mr. XieYueLv
@Date   ：2021/7/25 15:13
@Desc   ：
=================================================='''
from apitest.project.addproject import Addproject
from apitest.login.loginopms import Login
import requests
host = "http://119.45.58.158:8289"


class AddTeamMember():

    def __init__(self, res = requests.sessions.session(), username = "观日落"):
        self.res = res
        self.username = username

    def search_member(self):
        url = host + "/user/ajax/search?term=" + str(self.username)
        Login(res=self.res).login()
        re = self.res.get(url)
        print(re.json())
        userid = re.json()[0]["value"]
        return userid

    def add_member(self):
        projectid = Addproject(res=self.res).addproject("谢谢2", "3Q")["id"]
        url = host + "/team/add/" + str(projectid)
        data = {"username":self.username, "projectid":projectid, "userid":self.search_member()}
        re = self.res.post(url=url, data=data)
        print(re.text)
        # print(re.json()[])
        return re.json()

if __name__ == '__main__':
    value = AddTeamMember().search_member()
    AddTeamMember().add_member()

















