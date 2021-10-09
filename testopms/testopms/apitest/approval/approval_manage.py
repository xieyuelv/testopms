#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：testopms -> approval_manage.py
@IDE    ：PyCharm
@Author ：Mr. XieYueLv
@Date   ：2021/10/3 0:50
@Desc   ：
=================================================='''

from apitest.login.loginopms import Login
host = "http://192.168.48.144:8285"

class Approval():

    def leave(self):
        url = host + "/leave/add"
        data = {"type": 1,
                "started": "2021-10-02",
                "ended": "2021-10-06",
                "days": 3,
                "reason": "555",
                "picture":"",
                "approverid": ",1467191338628906628",
                "id": 0}
        Login().login()
        ress = Login().res.post(url, data=data)
        return ress.json()

if __name__ == '__main__':
    print(Approval().leave())