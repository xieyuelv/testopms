#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：locust -> locustfile.py
@IDE    ：PyCharm
@Author ：Mr. XieYueLv
@Date   ：2021/8/14 14:21
@Desc   ：
=================================================='''

from locust import HttpUser, task, constant_pacing


# import requests
# res = requests.sessions.session()


class getTest(HttpUser):

    # wait_time = constant_pacing(3)
    def on_start(self):
        print("用户初始化开始。。。")
        url = "http://119.45.58.158:8989/login"
        data = {"username": "lock", "password": "opms123456"}
        with self.client.post(url=url, data=data, name="post登录请求", timeout=10) as respones:
            if respones["code"] != 1:
                print(respones.json())
                respones.failure(respones.json()["message"])

    def on_stop(self):
        print("用户结束。。。")

    # def __init__(self):
    #     pass

    # @task
    # def getProfile(self):
    #     self.client.get("/profile",name="get个人页请求")
    #     print("测试get个人页请求")

    # @task
    # def getLogin(self):
    #     self.client.get("/login",name="get请求登录")
    #     print("get请求登录")
    # @task



    @task
    def add_project(self):
        url = "http://119.45.58.158:8989/project/add"
        data = {"name": "谢谢",
                "aliasname": "谢谢2",
                "started": "2021-08-23",
                "ended": "2021-08-23",
                "desc": "test",
                "id": 0}
        with self.client.post(url=url, data=data, name="添加项目") as respone:
            if respone["code"] == 1:
                respone.success("添加成功")
        # return ress.json()

    # def get_time(self):
    #     import time
    #     now_time_stamp = time.time()
    #     time_data = time.ctime(now_time_stamp)
    #     now_data = time_data.split(" ")[3]
    #     return now_data
    #
    # def clock(self):
    #     url = "http://192.168.48.132:8181/checkwork/ajax/clock"
    #     heards = {"Cookie":"beegosessionID=f43afc8d40793f033df5a402703c5ee9; Hm_lvt_750463144f16fe69eb3ac11bea1c4436=1628927342; Hm_lpvt_750463144f16fe69eb3ac11bea1c4436=1628960592"}
    #     data = {"clock":getTest().get_time()}
    #     ress = res.post(url=url,data=data)
    #     print(ress.text)

# if __name__ == '__main__':
#     getTest().add_project()
    # getTest().clock()
    # @task
    # def getLogin(self):
    #     with self.client.get("/",name="get请求登录") as response:
    #         if "测试驿栈" in response.text:
    #             response.success()

    # @task
    # def postLogin(self):
    #     url = "/login"
    #     data = {"username":"lock","password":"opms123456"}
    #     with self.client.post(url=url,data=data,name="post登录请求",timeout=10) as respones:
    #         if respones["code"] != 1:
    #             print(respones.json())
    #             respones.failure(respones.json()["message"])


