#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：testopms -> staff_photo.py
@IDE    ：PyCharm
@Author ：Mr. XieYueLv
@Date   ：2021/10/3 15:34
@Desc   ：
=================================================='''

from apitest.login.loginopms import Login
from common.read_yml import readyaml
host = readyaml("D:\接口资料\\testopms\conf\db.yaml")["host"]

class Photo():

    def photo(self):
        url = host + "/uploadmulti"
        filename = "D:\\下载文件\\测试上传.jpg"
        file = {"uploadFiles":open(filename,"rb")}
        Login().login()
        ress = Login().res.post(url, files=file)
        print(ress.text)
        # return ress.text

if __name__ == '__main__':
    Photo().photo()
