#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：testopms -> test_addproject.py
@IDE    ：PyCharm
@Author ：Mr. XieYueLv
@Date   ：2021/7/25 1:08
@Desc   ：
=================================================='''
import os
import logging
import allure
import pytest
import subprocess
from apitest.project.addproject import Addproject

# @pytest.mark.parametrize("name,aliasname",[("谢谢5","3Q"),("谢谢6","3Q")])
# def test_addproject_one(name, aliasname):
#     aj = Addproject().addproject(name=name, aliasname=aliasname)
#     assert aj["code"] == 0



@allure.feature("测试报告")
class TestAddProject():

    @pytest.mark.testmark
    @pytest.mark.parametrize("name, aliasname, exp_code", [("","asd", 1),("asd", "", 0)])
    def test_addproject(self, name, aliasname, exp_code):
        res = Addproject(name=name, aliasname=aliasname).addproject()
        print(res, res["code"])
        assert res["code"] == exp_code

    # @pytest.mark.testmark
    # @allure.story("声明家具作为参数")
    # @pytest.fixture()
    # def test_addproject_two(self, test_one):
    #     self.name=2
    #     return self.name
    #
    # @pytest.mark.testmark
    # @allure.story("重跑用例")
    # # @pytest.mark.flaky(reruns=3)  # 失败重跑
    # def test_print(self, test_addproject_two, test_one):
    #
    #     try:
    #         i = 0
    #         a = test_addproject_two/i
    #         print(a)
    #         assert a==i
    #     except Exception as e:
    #         logging.debug(e)
    #         print(e)
    #
    # @pytest.mark.testmark
    # @allure.story("普通case")
    # @pytest.fixture(scope="module")
    # def test_one(self):
    #     print("six")
    #     yield
    #     print("seven")
    #
    #
    # @pytest.mark.testmark
    # def test_two(self, test_one):
    #     print("666")
    #
    # @pytest.mark.testmark
    # def test_three(self):
    #     print("333")

if __name__ == '__main__':
    # 生成allure的报告
    # os.system("pytest D:\接口资料\\testopms\case\\test_addproject\\test_addproject.py --alluredir ./report/allure")
    # os.system("allure serve ./report/allure")
    pytest.main("-m", "testmark")










