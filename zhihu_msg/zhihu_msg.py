#! /usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipreacher'


import os
import zhihuapi as api
import urllib.request


# 配置 cookie
def set_cookie():
    if os.path.isfile('cookie'):
        print('cookie 已存在')
    else:
        print('由于 Terminal 本身对输入内容长度的限制')
        cookie_content1 = input('请先输入 cookie 的前一半\n>  ')
        cookie_content2 = input('请继续输入 cookie 的后一半\n>  ')
        cookie_content = cookie_content1 + cookie_content2
        with open('cookie', 'w') as f: 
            f.write(cookie_content)
        print('cookie 已保存')

    with open('cookie') as f:
        api.cookie(f.read())
    print('cookie 已配置完成')


r1 = []
r2 = []
r5 = []


# 拉取关注者名单，page 根据名单页数确定
def followers(me, page):
    for i in range(page):    
        data = api.user(me).followers(offset=(20 * i))
        for j in range(len(data)):
            r1.append(data[j]['name'])    # 关注者的昵称
            r2.append(data[j]['url_token'])    # 关注者的个性域名


# 获取私信地址
def hash_id():
    for i in range(len(r2)):
        r3 = api.user(r2[i]).detail()
        r4 = [r3['id']]
        r5.append(r4)
    print(r5)

# 群发私信
def send_msg():
    for i in range(len(r5)):
        print(str(r5[i][0]))
        api.action.message(str(r5[i][0]), 'Hi, %s!\n'
                                        'Thanks for your following~\n'
                                        #'Happy Valentine\'s Day!\n'
                                        '[This message is sent by https://github.com/ipreacher/tricks/tree/master/zhihu_msg]'
                                        % str(r1[i][0]))
        print('正在向_' + str(r1[i][0]) + '_发送私信...')
    print('私信已群发完毕！\n'
        '更多有意思的小玩意，请戳---->\n'
        '[https://github.com/ipreacher/tricks]')


if __name__ == '__main__':
    set_cookie()
    me = input('请输入你的个性域名 \n>  ')
    page = int(input('请输入你的关注者页数 \n>  '))
    followers(me, page)
    hash_id()
    send_msg()

