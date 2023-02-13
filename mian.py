#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : B1ain
# Action    : B站
# Desc      : B站主模块

import requests, json, sys, re
import time
from datetime import datetime, timedelta

import os
import bilibili
import uidtoroomid
import traceback


class bzMonitor():
    def __init__(self, ):
        self.reqHeaders = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
            'Content-Type': 'application/x-www-form-urlencoded',

            'Connection': 'close',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
        }
        self.uid = uidtoroomid.main()  # 这里添加关注人的uid

    # 获取各用户的json连接
    def getbzurl(self):
        try:
            # self.bzurl = []
            for i in self.uid:
                bilibili.bililive(i)
                # url = 'host_uid=%s&o' % (i)
                # self.bzurl.append(url)
        except Exception as e:
            print(traceback.format_exc())
            # self.echoMsg('Error', e)
            # sys.exit()



# 格式化输出
    def echoMsg(self, level, msg):
        if level == 'Info':
            print('[Info] %s' % msg)

        elif level == 'Error':
            print('[Error] %s' % msg)




if __name__ == '__main__':
    b = bzMonitor()
    b.getbzurl()
