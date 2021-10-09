#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：testopms -> knowledge_share.py
@IDE    ：PyCharm
@Author ：Mr. XieYueLv
@Date   ：2021/10/3 14:48
@Desc   ：
=================================================='''

from apitest.login.loginopms import Login
host = "http://192.168.48.144:8285"

class Knowledge():

    def share(self):
        url = host + "/knowledge/add"
        data = {"sortid": 1,
                "title": "技能分享",
                "summary": "jmeter技术分享",
                "content": "工具基本使用",
                "id": 1}
        Login().login()
        ress = Login().res.post(url, data=data)
        return ress.json()


if __name__ == '__main__':
    print(Knowledge().share())