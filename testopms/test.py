#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：locust -> test.py
@IDE    ：PyCharm
@Author ：Mr. XieYueLv
@Date   ：2021/8/15 1:04
@Desc   ：
=================================================='''

# import time
#
# now_time_stamp = time.time()
# print(now_time_stamp)
# time_data = time.ctime(now_time_stamp)
# print(type(time_data))
# print(time_data.split(" ")[3])
# import requests
# res = requests.sessions.session()
# def login():
#     url = "http://192.168.48.141:8282/login"
#     data = {"username": "lock", "password": "opms123456"}
#     ress = res.post(url=url, data=data)
#     return ress.json()
#
#
# def add_project():
#     url  = "http://192.168.48.141:8282/project/add"
#     data = {"name": "xieyuelv",
#      "aliasname": "谢谢",
#      "started": "2021-08-23",
#      "ended": "2021-08-23",
#      "desc": "test",
#      "id": 0}
#     login()
#     ress = res.post(url=url,data=data)
#     return ress.json()
#
# # lg = login()
# # print(lg)
# # get_manager()
# ap = add_project()
# print(ap)


# k = 1000
# sum = 0
# while k > 1:
#     print(k)
#     k = k / 2
# print(sum)

# import re
# str1 = "Python's features"
# str2 = re.match(r'(.*)on(.*?).*',str1)
# print(str2.group(1))


# def adder(x):
#     def wrapper(y):
#         return  x + y
#     return wrapper
# adder5 = adder(5)
# print(adder5(adder5(6)))


# b1 = [1,2,3]
# b2 = [2,3,4]
# b3 = [val for val in b1 if val in b2]
# print(b3)

# import re
#
# line = "Cats are smarter than dogs"
# print(re.match('(.*?) are (.*?) than (.*)',line).group(2))




#获取并打印google首页的html
# import urllib.request
# # response=urllib.request.urlopen('http://123.56.170.43:7272/')
# # html=response.read()
# # print(html)
# url = "http://123.56.170.43:7272/"
# re_sp = urllib.request.Request(url=url).get_header("headers")
# print(re_sp)


# a = {"a":1}
# print(a['a'])
#
# b = [8,3,2,6,19,7]
# b.reverse()
# print(b)
# b.sort(reverse=True)
# print(b)



#-*-coding:utf-8-*-
# Time:2017/9/21 19:02
# Author:YangYangJun


# from openpyxl import Workbook
# from openpyxl.reader.excel import load_workbook
#
# import os
# import time
#
#
#
# def writeExcel():
#     # 获取文件路径
#     excelPath = os.path.join(os.getcwd(), 'ExcelData')
#     print ("****")
#     print (excelPath)
#     # 定义文件名称
#     #  invalid mode ('wb') or filename: 'Excel2017-09-21_20:15:57.xlsx'   这种方式明明文件，会提示保存失败，无效的文件名。
#     # nameTime = time.strftime('%Y-%m-%d_%H:%M:%S')
#     nameTime = time.strftime('%Y-%m-%d_%H-%M-%S')
#     excelName = 'Excel' + nameTime + '.xlsx'
#     ExcelFullName= os.path.join(excelPath,excelName)
#     print (ExcelFullName)
#
#     wb = Workbook()
#
#     ws = wb.active
#
#     tableTitle = ['userName', 'Phone', 'age', 'Remark']
#
#     # 维护表头
#     #        if row < 1 or column < 1:
#     #          raise ValueError("Row or column values must be at least 1")
#     # 如上，openpyxl 的首行、首列 是 （1,1）而不是（0,0），如果坐标输入含有小于1的值，提示 ：Row or column values must be at least 1，即最小值为1.
#     for col in range(len(tableTitle)):
#         c = col + 1
#         ws.cell(row=1, column=c).value = tableTitle[col]
#
#     # 数据表基本信息
#     tableValues = [['张学友', 15201062100, 18, '测试数据！'], ['李雷', 15201062598, 19, '测试数据！'],['Marry', 15201062191, 28, '测试数据！']]
#
#     for row in range(len(tableValues)):
#         ws.append(tableValues[row])
#     #wb.save(ExcelFullName)
#     wb.save(filename=ExcelFullName)
#     return ExcelFullName
#
# def readExcel(ExcelFullName):
#     wb = load_workbook(ExcelFullName)
#     #wb = load_workbook(filename=ExcelFullName)
#
#     # 获取当前活跃的worksheet,默认就是第一个worksheet
#     #ws = wb.active
#     # 当然也可以使用下面的方法
#     # 获取所有表格(worksheet)的名字
#     sheets = wb.get_sheet_names()
#     print (sheets)
#     # # 第一个表格的名称
#     sheet_first = sheets[0]
#     # # 获取特定的worksheet
#     #
#     ws = wb.get_sheet_by_name(sheet_first)
#     print ("***")
#     print (sheet_first)
#     print (ws.title)
#     print ("^^^")
#     # 获取表格所有行和列，两者都是可迭代的
#
#     rows = ws.rows
#     print (rows)
#
#     columns = ws.columns
#
#     # 迭代所有的行
#
#     for row in rows:
#
#         line = [col.value for col in row]
#
#         print (line)
#
#     # 通过坐标读取值
#
#     print (ws['A1'].value)  # A表示列,1表示行
#
#     print (ws.cell(row=1, column=1).value)
#
# if __name__ == '__main__':
#     ExcelFullName = writeExcel()
#     readExcel(ExcelFullName)


# 检查两个字符串的组成元素是否一样
# from collections import Counter
# def diff(one, two):
#     return Counter(one) == Counter(two)
#
# print(diff("asd","asd1"))
#
# # 打印N次字符串
# n = 3
# s = "我的fauk\n"
# print(s * n)
#
# # 大写第一个字母
# a = "我的-as dsa"
# print(a.title())

import random
print(random.randint(1,1000))
print(random.choice("asdfghjk"))
print(random.sample("asdfgqwer",3))









