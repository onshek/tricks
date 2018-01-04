__author__ = 'ipreacher'

import time
import datetime
import requests
import pandas as pd
from bs4 import BeautifulSoup

cur_time = time.localtime()
format_time = datetime.datetime(cur_time[0], cur_time[1], cur_time[2],
                                cur_time[3], cur_time[4], cur_time[5])
now_time = '{:%Y-%m-%d %H:%M:%S}'.format(format_time)
print(now_time)

stock_dict = {
    '160716': '嘉实基本面50指数',
    '070018': '嘉实回报混合',    
    '260108': '景顺长城新兴成长混合',
    '110022': '易方达消费行业股票',   
    '000457': '上投摩根核心成长股票',  
    '164906': '交银中证海外中国互联网',    
    '241001': '华宝兴业海外中国混合',    
    '378006': '上投摩根全球新兴市场混合QDII',    
    '003243': '上投摩根中国世纪灵活配置混合型证券投资基金'
}

#text = pd.Series(index=stock_dict.values())
for stock in stock_dict.keys():
    r = requests.get('http://fund.eastmoney.com/' + stock + '.html?spm=search')
    soup = BeautifulSoup(r.text, 'html.parser')
    body = soup.body
    item = body.find_all('span', attrs={'id': 'gz_gszzl'}) 
    s = item[0].get_text()
    #text[stock_dict[stock]] = s
    print(stock_dict[stock], s)    