__author__ = 'ipreacher'

import time
import numpy as np
from zhihu_oauth import ZhihuClient
from zhihu_oauth.exception import NeedCaptchaException

client = ZhihuClient()
client.login_in_terminal()

me = client.me()
t = '你好，感谢关注！\n新的一年里，祝学业进步，工作顺利！\n[This is sent by a robot.]\nipreacher' 
for f in me.followers:
	print(f.name)
	me.message(f, t)
	time.sleep(10 * abs(np.random.randn()))