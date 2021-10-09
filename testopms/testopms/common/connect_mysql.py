#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：testopms -> connect_mysql.py
@IDE    ：PyCharm
@Author ：Mr. XieYueLv
@Date   ：2021/8/1 14:50
@Desc   ：
=================================================='''
from common.read_yml import Readyaml
import pymysql
connect2 = pymysql.Connect(
            host = Readyaml().readyaml()["MYSQL"]["ip"],
            port = Readyaml().readyaml()["MYSQL"]["port"],
            user= Readyaml().readyaml()["MYSQL"]["username"],
            password = Readyaml().readyaml()["MYSQL"]["password"],
            db = Readyaml().readyaml()["MYSQL"]["db"],
            charset = Readyaml().readyaml()["MYSQL"]["charset"]
        )

class DbConnect():

    def __init__(self, connect=connect2):
        self.connect = connect

    def connect_mysql2(self):
        cur = self.connect.cursor()
        return cur

    def get_data_fetchone(self):
        sql = "SELECT * FROM aiopms.pms_users"
        cursor = DbConnect().connect_mysql2()
        cursor.execute(sql)
        result = cursor.fetchone()
        return result

    def get_data_fetchall(self):
        sql = "SELECT * FROM aiopms.pms_users"
        cursor = DbConnect().connect_mysql2()
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def close_connect(self):
        DbConnect().connect_mysql2().close()
        self.connect.close()

if __name__ == '__main__':
    print(DbConnect().get_data_fetchone())
    # DbConnect().connect_mysql()
    # print(Readyaml().readyaml())
    print(DbConnect().get_data_fetchall()[1][2])