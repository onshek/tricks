#! /usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipreacher'


import time
import itchat
import datetime
import tushare as ts


stock_symbol = input('请输入股票代码 \n>  ')
price_low = input('请输入最低预警价格 \n>  ')
price_high = input('请输入最高预警价格 \n>  ')


# 登陆微信
def login():
    itchat.auto_login()


# 获取股价并发提醒
def stock():
    time = datetime.datetime.now()    # 获取当前时间
    now = time.strftime('%H:%M:%S') 
    data = ts.get_realtime_quotes(stock_symbol)    # 获取股票信息
    r1 = float(data['price'])
    r2 = str(stock_symbol) + ' 的当前价格为 ' + str(r1)
    content = now + '\n' + r2
    itchat.send(content, toUserName='filehelper')
    print(content)
    # 设置预警价格并发送预警信息
    if r1 <= float(price_low):
        itchat.send('低于最低预警价格', toUserName='filehelper')
        print('低于最低预警价格')
    elif r1 >= float(price_high):
        itchat.send('高于最高预警价格', toUserName='filehelper')
        print('高于最高预警价格')
    else:
        itchat.send('价格正常', toUserName='filehelper')
        print('价格正常')


# 定时开启，循环脚本
def timer(sched_timer):
    flag = 0
    while True:
        now = datetime.datetime.now()
        if now == sched_timer:
            stock()
            flag = 1
        else:
            if flag == 1:
                sched_timer = sched_timer + datetime.timedelta(seconds = 3)
                flag = 0


if __name__ == '__main__':
    login()
    sched_timer = datetime.datetime(2017, 2, 15, 10, 30, 0, 0)
    print('run the task at {0}'.format(sched_timer))
    timer(sched_timer)
    time.sleep(2)


