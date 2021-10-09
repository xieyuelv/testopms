#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：testopms -> read_yml.py
@IDE    ：PyCharm
@Author ：Mr. XieYueLv
@Date   ：2021/7/31 21:21
@Desc   ：
=================================================='''

import yaml
import os


class Readyaml():

    def __init__(self, yamlpath="D:\\接口资料\\testopms\\conf\\db.yaml"):
        self.yamlpath = yamlpath

    def readyaml(self):
        if not os.path.isfile(self.yamlpath):
            raise FileNotFoundError("文件路径不存在，请检查路径是否存在:{}".format(self.yamlpath))
        rcn = open(self.yamlpath, "r", encoding="utf-8").read()
        data = yaml.load(rcn, Loader=yaml.FullLoader)
        return data

if __name__ == '__main__':
    data = Readyaml().readyaml()
    print(type(data))
    print(data)
    print(os.path.abspath(".")) # 当前路径
    print(os.path.dirname(os.path.abspath("."))) # 当前路径的上一级
    print(os.path.dirname(os.path.abspath(".")) + "\conf\db.yaml")
    yamlpath = os.path.dirname(os.path.abspath(".")) + "\conf\db.yaml"
    print(type(Readyaml().readyaml()["MYSQL"]["port"]))












