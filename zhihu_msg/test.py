import zhihuapi as api

with open('cookie') as f:
    api.cookie(f.read())

r5 = [['17aefacb2e682b02cc7ad5455da043dd']]

def send_msg():
    for i in range(len(r5)):
        print(str(r5[i][0]))
        api.action.message(str(r5[i][0]), '这是一条机器人发送的私信，如对您造成打扰，万分抱歉！祝情人节快乐！')
        print('正在发送私信...')
    print('私信已群发完毕！\n更多有意思的小玩意，请戳---->\n[https://github.com/ipreacher/tricks]')

send_msg()