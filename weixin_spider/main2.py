# -- coding: utf-8 --
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
import random, re
from fake_useragent import UserAgent

url = "https://mp.weixin.qq.com/cgi-bin/appmsg"

cfg={
        "name": 'AI算法与图像处理',
        "cnt": 0,
        "begin": "0",
        "token": "251084613",
        "fakeid": "MzU4NTY4Mzg1Mw==",
        "cookie": "appmsglist_action_3879859384=card; _qpsvr_localtk=0.53442903812675; RK=C/2NjrxBMh; ptcz=30c453d3718f08a4550ef4a9815730bfab570de6b0dfd2c0dc27e62e02cedebe; ua_id=k6yXDooqC7mt04RBAAAAABgqWq_ng68Z62M-zF-tJIM=; wxuin=64115639033196; mm_lang=zh_CN; pgv_info=ssid=s3616010930; pgv_pvid=3335243978; xid=f7918bdebaa8eec3785d561153116c9e; cert=uKf_AwMrO3T6wADvk7yHZxbZD2RZoWs_; uuid=d5662417362c5dea2556501bc44df840; ptui_loginuin=1557519267@qq.com; uin=o1557519267; skey=@iGHsdkOM5; sig=h01b7089abc14eb638077dc26882895a125fc1b7c7ea1c7143f42679f72f5b2cb3d63067c0d8cb5e2d6; data_bizuin=3879859384; data_ticket=NKGSRo9K93jdNAwWv4Mw5vVjYbfGC3DKYftCC/wkXzs1ipQyJRkmm+XtCZ9AfdDj; master_key=vLEQgsQKTEvBACHlXVotVsIOjK0h8xlohMil/33JbVM=; master_user=gh_e5c22d354bac; master_sid=UTdOVzhmRXJDNnQzZE1MMGdCRFBOVlFPOGFQV0NQcndBVVo1YkVWR2JEZGtVUUMyQnMySXpmVUpEbEhMTE9LeUpZYlN6V1E1ZGFZV3BzMlo5TnlpeWpYYzg4ZWlHQ2IwX042bkFuMEZrV1BIQWxnbThoVXh6Y01VdFgxRXhvZmRNc3NoVmdsaFNJUGt0YzRI; master_ticket=91ae58b1a14f5874305d28db0c1c891c; bizuin=3879859384; slave_user=gh_e5c22d354bac; slave_sid=UmZiQWxEU3J6dWpPT1JjYVpTcDA4WktGSjlrbDczT2RkTnBJN0dfTEJmU1ZfekhBMWtHS3RKTXBUTk52bGJKQmxUVFRLT3FDeDBVd3hWRU5wMFZFSU5jTF9QUE54cDExRjZDSlhyckR0MzRGZ2VvYkxWcWd0ek5BQ3ZvaVp5aUJET1JPRFZ3Q3hpZEk4cklx; _clck=3879859384|1|f56|0; rewardsn=; wxtokenkey=777"
    },
begin = "0"
token = "251084613"
#需要从微信公众平台获取
fakeid = "MzU4NTY4Mzg1Mw=="
#需要从微信公众平台获取
cookie_str = "appmsglist_action_3879859384=card; _qpsvr_localtk=0.53442903812675; RK=C/2NjrxBMh; ptcz=30c453d3718f08a4550ef4a9815730bfab570de6b0dfd2c0dc27e62e02cedebe; ua_id=k6yXDooqC7mt04RBAAAAABgqWq_ng68Z62M-zF-tJIM=; wxuin=64115639033196; mm_lang=zh_CN; pgv_info=ssid=s3616010930; pgv_pvid=3335243978; xid=f7918bdebaa8eec3785d561153116c9e; cert=uKf_AwMrO3T6wADvk7yHZxbZD2RZoWs_; uuid=d5662417362c5dea2556501bc44df840; ptui_loginuin=1557519267@qq.com; uin=o1557519267; skey=@iGHsdkOM5; sig=h01b7089abc14eb638077dc26882895a125fc1b7c7ea1c7143f42679f72f5b2cb3d63067c0d8cb5e2d6; data_bizuin=3879859384; data_ticket=NKGSRo9K93jdNAwWv4Mw5vVjYbfGC3DKYftCC/wkXzs1ipQyJRkmm+XtCZ9AfdDj; master_key=vLEQgsQKTEvBACHlXVotVsIOjK0h8xlohMil/33JbVM=; master_user=gh_e5c22d354bac; master_sid=UTdOVzhmRXJDNnQzZE1MMGdCRFBOVlFPOGFQV0NQcndBVVo1YkVWR2JEZGtVUUMyQnMySXpmVUpEbEhMTE9LeUpZYlN6V1E1ZGFZV3BzMlo5TnlpeWpYYzg4ZWlHQ2IwX042bkFuMEZrV1BIQWxnbThoVXh6Y01VdFgxRXhvZmRNc3NoVmdsaFNJUGt0YzRI; master_ticket=91ae58b1a14f5874305d28db0c1c891c; bizuin=3879859384; slave_user=gh_e5c22d354bac; slave_sid=UmZiQWxEU3J6dWpPT1JjYVpTcDA4WktGSjlrbDczT2RkTnBJN0dfTEJmU1ZfekhBMWtHS3RKTXBUTk52bGJKQmxUVFRLT3FDeDBVd3hWRU5wMFZFSU5jTF9QUE54cDExRjZDSlhyckR0MzRGZ2VvYkxWcWd0ek5BQ3ZvaVp5aUJET1JPRFZ3Q3hpZEk4cklx; _clck=3879859384|1|f56|0; rewardsn=; wxtokenkey=777"
#需要从微信公众平台获取

params = {
    "action": "list_ex",
    "begin": begin, #请求的页数
    "count": "5",  #一次请求返回信息个数
    "fakeid": fakeid,
    "type": "9",
    "token": token,
    "lang": "zh_CN",
    "f": "json",
    "ajax": "1"
}


import requests

def main():
    print("开始抓取")
    cnt = 0
    while(True):
        index = 0
        result = getInfo(index)
        while(len(result['app_msg_list'])):
            index += 1
            getInfo(index)
            if (result['base_resp']['ret'] == 200040):
                getInfo(index)
        print("睡眠一天")
        time.sleep(86400)


def getInfo(begin):
    ua = UserAgent(path='fake_useragent.json')
    # ua代理
    headers = {
        "Cookie": cookie_str,
        "User-Agent": ua.random
    }

    #参数begin
    params["begin"] = str(begin * 5)
    #随机暂停
    random_sleep(5, 10)
    result = requests.get(url, headers=headers, verify=False, params = params,).json()
    try:
        app_msg_list = result['app_msg_list']
        for item in app_msg_list:
            #print(item["digest"])
            global cnt
            print(cnt, params["begin"], item["title"])
            cnt += 1
    except:
        if(result['base_resp']['ret'] == 200040):
            print(result['base_resp']['ret'])
            print(result['base_resp']['err_msg'])
            print("token过期, 更换token")
            params['token'] = getToken()

    return result

def getToken():
    ua = UserAgent(path='./fake_useragent.json')
    cookies = {}
    s = requests.Session()
    url = 'https://mp.weixin.qq.com'

    headers = {
        'User-Agent': ua.random,
        "Host": "mp.weixin.qq.com",
        'Referer': 'https://mp.weixin.qq.com/'
    }

    for item in cookie_str.split(';'):
        sep_index = item.find('=')
        cookies[item[:sep_index]] = item[sep_index + 1:]

    res = s.get(url=url, headers=headers, cookies=cookies, verify=False)
    if res.status_code == 200:
        print(res.url)
        token = re.findall(r'.*?token=(\d+)', res.url)
        if token:
            token = token[0]
        else:
            print('登陆失败')

    return token

#随机休眠
def random_sleep(start, end):
    # 随机暂停若干时间，暂停时间介于start和end之间
    t = random.uniform(start,end)
    time.sleep(t)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    global cnt
    cnt = 0
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/