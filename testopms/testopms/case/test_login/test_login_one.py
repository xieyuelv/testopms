#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：testopms -> test_login_one.py
@IDE    ：PyCharm
@Author ：Mr. XieYueLv
@Date   ：2021/7/24 上午11:48
@Desc   ：
=================================================='''

import pytest
from apitest.login.loginopms import Login
from common.read_csv import Readcsv

class TestLogin():
    @pytest.fixture()
    def test_get_csv_data(self):
        rc = Readcsv().readcsv()
        return rc

    # 测试登录成功
    @pytest.mark.testmark
    def test_login_succeed(self, test_get_csv_data):
        res = Login(username=test_get_csv_data[1][0], password=test_get_csv_data[1][1]).login()
        assert test_get_csv_data[1][2] == str(res["code"])

    # 测试登录失败
    @pytest.mark.testmark
    @pytest.mark.parametrize("username, password, exp_code", [("lock", "", 0),("", "opms123456", 0)])
    def test_login_fail(self, username, password, exp_code):
        res = Login(username=username, password=password).login()
        assert res["code"] == exp_code

    @pytest.mark.testmark
    @pytest.mark.skipif(condition=True, reason="就是要跳过")
    def test_data(self, test_get_csv_data):
        print(test_get_csv_data[1])

if __name__ == '__main__':
    pytest.main("-m","testmark")
