# -- coding: utf-8 --
import csv
from fake_useragent import UserAgent
import random
import re
import requests
import time

from config import *

base_url = "https://mp.weixin.qq.com/cgi-bin/appmsg"
params = {
    "action": "list_ex",
    "begin": None, #请求的页数
    "count": "5",  #一次请求返回信息个数
    "fakeid": None,
    "type": "9",
    "token": None,
    "lang": "zh_CN",
    "f": "json",
    "ajax": "1"
}

def write_csv(path, data):
    with open(path, "a", encoding='utf-8') as f:
        spamwriter = csv.writer(f)
        spamwriter.writerow(data)

def process_single(cfg):
    print("公众号{}从{}页开始抓取".format(cfg["name"], cfg["begin"]))
    global cnt
    cnt = cfg["cnt"]
    params["token"] = cfg["token"]
    params["fakeid"] = cfg["fakeid"]
    while True:
        index = int(cfg["begin"])    
        result = getInfo(index, cfg)
        while(len(result['app_msg_list'])):
            index += 1
            getInfo(index, cfg)
            if (result['base_resp']['ret'] == 200040):
                getInfo(index, cfg)
        print("睡眠一天")
        time.sleep(86400)


def getInfo(begin, cfg):
    ua = UserAgent(path='fake_useragent.json')
    # ua代理
    headers = {
        "Cookie": cfg["cookie"],
        "User-Agent": ua.random
    }
    #参数begin
    params["begin"] = str(begin * 5)
    #随机暂停
    random_sleep(5, 10)
    result = requests.get(base_url, headers=headers, verify=False, params = params,).json()
    try:
        app_msg_list = result['app_msg_list']
        for item in app_msg_list:
            #print(item["digest"])
            global cnt
            data = [
                cfg["name"],
                cnt,
                begin,
                #str(item["aid"]),
                item['title'],
                #item['digest'],
                item['link'], 
                #str(item['create_time']), 
                #str(item['update_time'])
            ]
            path = 'results/'+cfg["name"]+'.csv'
            write_csv(path, data)
            print(cnt, begin, item["title"])
            cnt += 1
        print("公众号{}第{}页爬取成功".format(cfg["name"], begin))
    except:
        if(result['base_resp']['ret'] == 200040):
            print(result['base_resp']['ret'])
            print(result['base_resp']['err_msg'])
            print("token过期, 更换token")
            params['token'] = getToken()

    return result

def getToken(cfg):
    ua = UserAgent(path='./fake_useragent.json')
    cookies = {}
    s = requests.Session()
    url = 'https://mp.weixin.qq.com'

    headers = {
        'User-Agent': ua.random,
        "Host": "mp.weixin.qq.com",
        'Referer': 'https://mp.weixin.qq.com/'
    }

    for item in cfg["cookie"].split(';'):
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

def main():
    for d in gongzhonghao_list:
        if d["name"] not in ok_list:
            process_single(d) 


if __name__ == '__main__':
    main()
    ##path = 't.csv'
    #data = [1,2,3,5,6,6]
    #write_csv(path, data)

