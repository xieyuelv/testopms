#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：testopms -> test_addteammenber.py
@IDE    ：PyCharm
@Author ：Mr. XieYueLv
@Date   ：2021/7/29 0:31
@Desc   ：
=================================================='''

from apitest.teammanager.addteammember import AddTeamMember
import pytest
import allure

# 测试添加项目成员
# @pytest.mark.skip
@allure.step("测试")
@allure.story("添加项目成员")
@pytest.mark.parametrize("username",[("李白"),("")])
def test_add_teammember(username):
    at = AddTeamMember(username=username).add_member()
    pytest.xfail(reason="功能未完成")
    assert at["code"] == 1










