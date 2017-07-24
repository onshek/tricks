#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import itchat
import urllib.request


@itchat.msg_register(itchat.content.TEXT)
def start(msg):
    if msg['Text'][: 8] == 'https://':
        print('正在链接到图片地址...')
        save(msg['Text'])     


def save(url):

    web = urllib.request.urlopen(url)
    data = web.read()
    with open('ins.jpg', 'wb') as f:
        f.write(data)
    print('正在发送到微信...')
    itchat.send(msg='@img@ins.jpg', toUserName='filehelper')
    print('执行完毕！\n')
    os.remove('ins.jpg')
    


if __name__ == '__main__':
    itchat.auto_login()
    itchat.run()