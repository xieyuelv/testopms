#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：testopms -> clock_in.py
@IDE    ：PyCharm
@Author ：Mr. XieYueLv
@Date   ：2021/10/2 23:49
@Desc   ：
=================================================='''
from apitest.login.loginopms import Login
# import requests
host = "http://192.168.48.143:8284"

class Clock():

    def clock(self):
        url = host + "/checkwork/ajax/clock"
        data = {"clock":"00:42:10"}
        Login().login()
        ress = Login().res.post(url, data=data)
        return ress.text

    def get_time(self):
        import time
        now_time_stamp = time.time()
        time_data = time.ctime(now_time_stamp)
        now_data = time_data.split(" ")[4]
        print(type(now_data))
        return now_data

if __name__ == '__main__':
    print(Clock().clock())
    print(Clock().get_time())
