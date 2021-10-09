#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：testopms -> read_csv.py
@IDE    ：PyCharm
@Author ：Mr. XieYueLv
@Date   ：2021/10/4 14:11
@Desc   ：
=================================================='''

import csv

# 接口的url以及入参数据参数化可以通过新建多个csv文件，其他写用例需要参数化的时候可以通过pytest的parametrize修饰器来参数化，毕竟测试也不能穷举，几个就够了
class Readcsv():

    def __init__(self, csvpath="D:\接口资料\\testopms\conf\data.csv"):
        self.csvpath = csvpath

    def readcsv(self):
        with open(self.csvpath,"r",encoding="utf-8") as file:
            read = csv.reader(file)
            data = []
            for row in read:
                data.append(row)
            return data

if __name__ == '__main__':
    print(Readcsv().readcsv())

# f = open("D:\接口资料\\testopms\conf\data.csv","w",encoding="utf-8")
# write_file = csv.writer(f)
# for i in  data:
#
#     write_file.writerow(str(i)+"\n")
#
# f.close()