#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：testopms -> organization_manage.py
@IDE    ：PyCharm
@Author ：Mr. XieYueLv
@Date   ：2021/10/6 23:52
@Desc   ：
=================================================='''

from apitest.login.loginopms import Login
from common.read_yml import Readyaml
host = Readyaml().readyaml()["host"]

class Organization():

    def organization(self):
        url = host + "/user/add"
        data = {"username": "谢谢",
                "password": "opms123456",
                "depart": "1462290164626094232",
                "position": "1462292006260420932",
                "realname": "谢谢",
                "sex": 1,
                "birth": "2021-10-13",
                "email": "2537320578@qq.com",
                "webchat": "",
                "qq": "",
                "phone": "18776496279",
                "tel": "",
                "address":"" ,
                "emercontact": "xiexie",
                "emerphone": "18924355943",
                "id": 0}
        Login().login()
        ress = Login().res.post(url, data=data)
        return ress.text

if __name__ == '__main__':
    Organization().organization()
