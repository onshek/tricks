__author__ = 'ipreacher'

import zhihuapi as api

with open('/Users/wonderful/Desktop/cookie') as f:
    api.cookie(f.read())

r1 = []
r2 = []
r5 = []

# 拉取关注者的昵称和个性域名，page 根据自己关注者页数确定
def followers(me, page):
    for i in range(page):    
        data = api.user(me).followers(offset=(20 * i))
        for j in range(len(data)):
            r1.append(data[j]['name'])    # 关注者的昵称
            r2.append(data[j]['url_token'])    # 关注者的个性域名

# 分行打印关注者的昵称和个性域名
def show(r):
    for k in range(len(r1)):
        s = (r[k] + '\n')
        print(s)

# 拉取并打印关注者的基本信息，包括序号及其个性域名、昵称、赞同数、感谢数、关注人数


def ff():
    print('关注者基本信息的格式为' + '\n' + '[序号, 个性域名, 昵称, 赞同数, 感谢数, 关注者人数]')
    for i in range(len(r2)):
        r3 = api.user(r2[i]).detail()
        r4 = [i, r3['urlToken'], r3['name'], r3['voteupCount'], r3['thankedCount'], r3['followerCount']]
        r5.append(r4)
        print(r4)
    #print(r5)

# 将关注者的基本信息保存为 txt 文件 
def txt(r):
    f = open('r.txt','w')
    f.write(str(r))
    f.close()

if __name__ == '__main__':
    me = input('请输入你的个性域名\n>  ')
    page = int(input('请输入你的关注者页数\n>  '))
    followers(me, page)
    #show(r1)
    #show(r2)
    ff()
    txt(r5)