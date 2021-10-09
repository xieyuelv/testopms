#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：testopms -> resume_manage.py
@IDE    ：PyCharm
@Author ：Mr. XieYueLv
@Date   ：2021/10/6 21:23
@Desc   ：
=================================================='''
from apitest.login.loginopms import Login
from common.read_yml import Readyaml
host = Readyaml().readyaml()["host"]
class Resume():

    def resume(self):
        url = host + "/resume/add"
        data = {"realname": "谢谢",
                "phone": "18776496279",
                "sex": 1,
                "birth": "2021-10-13",
                "edu": 7,
                "work": 4,
                "note": "",
                "attachment": "",
                "status": 1,
                "id": 0}
        Login().login()
        ress = Login().res.post(url, data=data)
        print(ress.text)
        return ress.text

if __name__ == '__main__':
    Resume().resume()

