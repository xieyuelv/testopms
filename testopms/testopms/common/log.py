#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：testopms -> log.py
@IDE    ：PyCharm
@Author ：Mr. XieYueLv
@Date   ：2021/9/1 0:11
@Desc   ：
=================================================='''

import logging
import datetime
import sys
logger = logging.getLogger('mylogger')
class Log():

    logger.setLevel(logging.INFO)
    rf_handler = logging.StreamHandler(sys.stderr)  # 默认是sys.stderr
    rf_handler.setLevel(logging.DEBUG)
    rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(message)s"))

    f_handler = logging.FileHandler('D:\接口资料\\testopms\log\error.log')
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

    logger.addHandler(rf_handler)
    logger.addHandler(f_handler)

    def info_log(self, mes):
        logger.info(mes)

    def debug_log(self, mes):
        logger.debug(mes)

    def warning_log(self, mes):
        logger.warning(mes)

    def error_log(self, mes):
        logger.error(mes)


if __name__ == '__main__':
    Log().info_log(666)
    Log().debug_log(777)
    Log().warning_log(888)
    Log().error_log(999)
