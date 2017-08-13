# -*- coding: utf-8 -*-
import json
import hashlib
import datetime
import urllib.request
from qqbot import qqbotsched
from qqbot import _bot as bot
bot.Login(['-q', '1234'])
contact = bot.List('buddy', 'ipreacher')[0]

def get_time():
    localtime = datetime.datetime.now()    # 获取当前时间
    now = localtime.strftime('%H:%M:%S')
    return now

def ticker_btc():
	url='https://www.okcoin.cn/api/v1/ticker.do?symbol=btc_cny'
	response = urllib.request.urlopen(url,timeout=3)#打开连接，timeout为请求超时时间
	result=response.read().decode('utf-8')#返回结果解码
	json_data=json.loads(result)
	ticker_btc = json_data['ticker']['last']
	return ticker_btc

def ticker_ltc():
	url='https://www.okcoin.cn/api/v1/ticker.do?symbol=ltc_cny'
	response = urllib.request.urlopen(url,timeout=3)#打开连接，timeout为请求超时时间
	result=response.read().decode('utf-8')#返回结果解码
	json_data=json.loads(result)
	ticker_ltc = json_data['ticker']['last']
	return ticker_ltc

def ticker_eth():
	url='https://www.okcoin.cn/api/v1/ticker.do?symbol=eth_cny'
	response = urllib.request.urlopen(url,timeout=3)#打开连接，timeout为请求超时时间
	result=response.read().decode('utf-8')#返回结果解码
	json_data=json.loads(result)
	ticker_eth = json_data['ticker']['last']
	return ticker_eth


#text_1 = '更新时间: ' + str(get_time()) + '\n' + 'BTC: ' + str(ticker_btc()) + ';\n' + 'LTC: ' + str(ticker_ltc()) + ';\n' + 'ETH: ' + str(ticker_eth())
text_2 = 'iRobot is alive.'

'''
@qqbotsched(hour='20', minute='0-55/01')
def mytask(bot):
    return ('更新时间: ' + str(get_time()) + '\n' + 'BTC: ' + str(ticker_btc()) + ';\n' + 'LTC: ' + str(ticker_ltc()) + ';\n' + 'ETH: ' + str(ticker_eth()))
    #bot.SendTo(contact, text_1)
'''

def onQQMessage(bot, contact, member, content):
    #text_1 = mytask(bot)
    if content == 'market':
        text_1 = ('更新时间: ' + str(get_time()) + '\n' + 'BTC: ' + str(ticker_btc()) + ';\n' + 'LTC: ' + str(ticker_ltc()) + ';\n' + 'ETH: ' + str(ticker_eth()))
        bot.SendTo(contact, text_1)
    elif content == 'stop':
        bot.SendTo(contact, 'iRobot is shut down.')
        bot.Stop()
    else:
    	bot.SendTo(contact, text_2)
