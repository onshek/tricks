import numpy as np
import tushare as ts 

stockList = ['600977', '603711', '603776', '603533', '300027',
			 '300133', '300251', '002905', '603103', '']
df = ts.get_realtime_quotes(stockList) #Single stock symbol
df['price'] = df['price'].astype(dtype=float)
df['pre_close'] = df['pre_close'].astype(dtype=float)
df['change'] = round((df['price'] / df['pre_close'] - 1) * 100, 2)
print(df[['time', 'name', 'price', 'pre_close', 'change']])
