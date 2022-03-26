import re

import requests
import json
import time
import datetime
from bs4 import BeautifulSoup
from lxml import etree
import taginfo
from django.template.defaultfilters import striptags



headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

def roominfostr(ridd):
    ridd=str(ridd)

    response = requests.get("https://api.live.bilibili.com/xlive/web-room/v1/index/getInfoByRoom?room_id=" + ridd,
                            headers=headers, timeout=10)
    live_status = json.loads(response.text)['data']['room_info']['live_status']  # 开播状态 1为已开播
    room_id = json.loads(response.text)['data']['room_info']['room_id']
    uid = json.loads(response.text)['data']['room_info']['uid']
    title = json.loads(response.text)['data']['room_info']['title']
    description = json.loads(response.text)['data']['room_info']['description']
    live_start_time = json.loads(response.text)['data']['room_info']['live_start_time']
    online = json.loads(response.text)['data']['room_info']['online']
    timeStamp = live_start_time
    timeStamp = int(timeStamp)
    dateArray = datetime.datetime.fromtimestamp(timeStamp)+ datetime.timedelta(hours=8)
    # timedelta(hours=8)
    # print(dateArray)
    otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
    print(otherStyleTime)
    print(type(otherStyleTime))

    now = datetime.datetime.now() + datetime.timedelta(hours=8)
    dc = now.strftime("%H:%M:%S")
    tzshj = dc
    print("github通知时间是：" + tzshj)

    d1 = now.strftime('%Y-%m-%d %H:%M:%S')
    print("github时间d1是：" + d1)
    d3 = datetime.datetime.strptime(d1, '%Y-%m-%d %H:%M:%S')
    print(d3)

    d2 = datetime.datetime.strptime(otherStyleTime, "%Y-%m-%d %H:%M:%S")
    print(d2)

    timedelay = d3 - d2

    timedelay = str(timedelay)

    online = str(online)
    online = online + '人'
    room_id = str(room_id)
    tags=taginfo.tags(uid)
    uid = str(uid)
    print(tags)
    tags=str(tags)
    description = str(description)
    description = striptags(description)


    if live_status == 1:
        live_status = '已开播'
    else:
        live_status = '未开播'
        otherStyleTime = ''

    roominfostr =  '本次直播主题：' + title + '\n' + '直播间简介：' + description + '\n'+ '直播tag：' + tags + '\n'+ '本次开播时间：' + otherStyleTime + '\n' + '当前直播人气：' + online + '\n' + '房间号：' + room_id + '\n' + '用户UID：' + uid + '\n' + '开播状态：' + live_status + '\n'+ '推送时间：' + tzshj + ' ' + '\n'  + '延时推送：' + timedelay + ' ' + '\n'

    print(roominfostr)
    return roominfostr

def summary(ridd):
    ridd=str(ridd)

    response = requests.get("https://api.live.bilibili.com/xlive/web-room/v1/index/getInfoByRoom?room_id=" + ridd,
                            headers=headers, timeout=10)
    live_status = json.loads(response.text)['data']['room_info']['live_status']  # 开播状态 1为已开播
    room_id = json.loads(response.text)['data']['room_info']['room_id']
    uid = json.loads(response.text)['data']['room_info']['uid']
    title = json.loads(response.text)['data']['room_info']['title']
    description = json.loads(response.text)['data']['room_info']['description']
    live_start_time = json.loads(response.text)['data']['room_info']['live_start_time']
    online = json.loads(response.text)['data']['room_info']['online']
    timeStamp = live_start_time
    timeStamp = int(timeStamp)
    dateArray = datetime.datetime.fromtimestamp(timeStamp)+ datetime.timedelta(hours=8)
    # timedelta(hours=8)
    # print(dateArray)
    otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
    print(otherStyleTime)
    print(type(otherStyleTime))

    now = datetime.datetime.now() + datetime.timedelta(hours=8)
    dc = now.strftime("%H:%M:%S")
    tzshj = dc
    print("github通知时间是：" + tzshj)

    d1 = now.strftime('%Y-%m-%d %H:%M:%S')
    print("github时间d1是：" + d1)
    d3 = datetime.datetime.strptime(d1, '%Y-%m-%d %H:%M:%S')
    print(d3)

    d2 = datetime.datetime.strptime(otherStyleTime, "%Y-%m-%d %H:%M:%S")
    print(d2)

    timedelay = d3 - d2

    timedelay = str(timedelay)

    online = str(online)
    online = online + '人'
    room_id = str(room_id)
    tags=taginfo.tags(uid)
    uid = str(uid)
    print(tags)
    tags=str(tags)
    description = str(description)
    description = striptags(description)


    if live_status == 1:
        live_status = '已开播'
    else:
        live_status = '未开播'
        otherStyleTime = ''

    summary =  '本次直播主题：' + title  + '\n'+ '本次开播时间：' + otherStyleTime + '\n'+ '房间号：' + room_id +  '\n'+ '推送时间：' + tzshj + ' ' + '\n'  + '延时推送：' + timedelay + ' ' + '\n'

    print(summary)
    return summary


def roominfotitle(ridd):
    ridd = str(ridd)

    response = requests.get("https://api.live.bilibili.com/xlive/web-room/v1/index/getInfoByRoom?room_id=" + ridd,
                            headers=headers, timeout=10)

    title = json.loads(response.text)['data']['room_info']['title']
    title=str(title)
    title=striptags(title)
    return title
