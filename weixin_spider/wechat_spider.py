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
    with open(path, "a", encoding='utf-8', newline='') as f:
        spamwriter = csv.writer(f)
        spamwriter.writerow(data)

def random_sleep(start, end, begin, cfg):
    t = random.uniform(start, end)
    print("公众号《{}》在第{}页随机休眠{}秒".format(cfg["name"], begin, t))
    time.sleep(t)

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
    random_sleep(5, 10, begin, cfg)

    result = requests.get(base_url, headers=headers, verify=False, params=params,).json()
    print(result)
    try:
        if len(result['app_msg_list']) == 0:
            print("公众号《{}》已经抓取完毕".format(cfg["name"]))
            return  
        app_msg_list = result['app_msg_list']
        for item in app_msg_list:

            global cnt
            data = [
                cfg["name"],
                cnt,
                begin,
                str(item["aid"]),
                item['title'],
                item['digest'],
                item['link'], 
                str(item['create_time']), 
                str(item['update_time'])
            ]
            path = 'results/'+cfg["name"]+'.csv'
            write_csv(path, data)
            print(cnt, begin, item["title"])
            cnt += 1
        print("公众号《{}》第{}页爬取成功".format(cfg["name"], begin))
    except:
        if result['base_resp']['ret'] == 200013:
            print("公众号《{}》抓取太频繁, 停在了第{}页".format(cfg["name"], begin))
            time.sleep(3600)
        if result['base_resp']['ret'] == 200040:
            print("公众号《{}》token过期, 停在了第{}页".format(cfg["name"], begin))
            print(result['base_resp']['ret'])
            print(result['base_resp']['err_msg'])
            params['token'] = getToken(cfg)
    return result

def process_single(cfg):
    print("公众号《{}》从{}页开始抓取".format(cfg["name"], cfg["begin"]))
    global cnt
    cnt = cfg["cnt"]
    index = int(cfg["begin"])
    params["token"] = cfg["token"]
    params["fakeid"] = cfg["fakeid"]
    while True:
        getInfo(index, cfg)
        index += 1
        if cnt > 50:
            global mp
            mp[cfg["name"]]["cnt"] = cnt
            mp[cfg["name"]]["index"] = index
            break

def main():
    global mp
    mp = {}
    for d in gongzhonghao_list:
        if d["name"] not in ok_list:
            mp[d["name"]] = {
                "cnt": d["cnt"],
                "begin": int(d["begin"])
            }
            process_single(d) 
    print(mp)

if __name__ == '__main__':
    main()
    # path = 'a.csv'
    # data = ["AI算法与图像处理",0,0,"2247522414_1","程明明：“生活歌者，一路向前”,把培养学生作为主要工作。","http://mp.weixin.qq.com/s?__biz=MzU4NTY4Mzg1Mw==&mid=2247522414&idx=1&sn=26b9b74dbbe0f8b75568d9d9e2966dbc&chksm=fd841e8ccaf3979ac2811e7a0d47fa6ab49e9a081fb07e339fb249c80c828f42cc7beeadca91#rd","1664114949","1664114949"]
    # write_csv(path, data)
    
