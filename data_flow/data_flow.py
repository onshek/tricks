#! /usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipreacher'


import time
import random


p=lambda:random.choice('`1234567890-=~!@#$%^&*()_+qwertyuiop[]\{}|asdfghjkl;'"zxcvbnm,./<>?")


def run():
	print('|'.join([p(),p(),p(),p(),p(),p(),p(),p(),p(),p(),p(),p(),p(),p(),p(),p(),
		p(),p(),p(),p(),p(),p(),p(),p(),p(),p(),p(),p(),p(),p(),p(),p(),p(),p(),p(),
		p(),p(),p(),p()]),end='\r') 


if __name__ == '__main__':
	print('数据流开始执行...\n')
	while True:
		try:
			run()
			time.sleep(0.05)
		except KeyboardInterrupt:
			print('\n'
				'\n'
				'数据流已执行完毕！\n'
        		'更多有意思的小玩意，请戳---->\n'
        		'[https://github.com/ipreacher/tricks]')
			break