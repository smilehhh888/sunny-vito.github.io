import json
from concurrent.futures import ThreadPoolExecutor, wait
import requests
import parsel
import threading
import re
import socks
import traceback
import socket
import urllib3
import random

# 设置socks5代理
# proxie_ip = "7651076-b73d0fb0:a1d09de6-US-24240189@gate-us.kkoip.com"
# proxie_port = 16700

"""
全局代理
socks.set_default_proxy(socks.SOCKS5, proxie_ip, proxie_port)
socket.socket = socks.socksocket

"""



headers = {
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
}

params = {
    'id': 'com.pingvigames.hidden.objects.find.items',
    'gl': 'US',
}
proxies1={
    "https": 'http://127.0.0.1:10809'
}
session = requests.Session()

with open("11111.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
#
# def save_data(data):
#     with open("./data2.txt", 'a', encoding='utf-8') as wr:
#         wr.write(data + '\n')

#

class Test():

    def func(self, package):
        try:
            a = str(self.sess())
            url1 = f'https://play.google.com/store/apps/details?id={package.strip()}&pcampaignid=merch_published_cluster_promotion_battlestar_collection_new_games&gl=US' # 通过更改gl值来修改谷歌商城的国家
            url2 = "https://api.sealionproxy.com/check/myip?t={RAND}"
            response = session.get(url=url1, headers=headers)
            response2 = session.get(url=url2, headers=headers)
            data2 = json.loads(response2.text)
            ip = data2['ip']
            print(ip)
            print(a)
            # self.save_data('ip2.txt',ip+' '+a)
            response.encoding = 'utf-8'
            sel = parsel.Selector(response.text)
            try:
                starRating = "".join(sel.css('div.TT9eCd::text').getall())
                if starRating=="":
                    starRating="NULL"
            except Exception:
                pass

            UIuSk = sel.css('div span.UIuSk::text').get()
            button = sel.css('span.VfPpkd-vQzf8d::text').get()
            if button == 'Install':
                button = True
            else:
                button = False

            data = json.dumps({
                "url":f'https://play.google.com/store/apps/details?id={package.strip()}&gl=US',
                "ip": ip,
                UIuSk: UIuSk,
                "AfwdI": sel.css('h1 span.AfwdI::text').get(),
                "starRating":starRating ,
                "download_count": sel.css('div.wVqUob div.ClM7O::text').get(),
                "contentRating": sel.css('div.g1rdde span span::text').get(),
                "install": button,
                "country": 'US'
            })

            # self.save_data('str2.txt',data)
            print(data)
            del data,a,url2,url1,data2,ip,UIuSk,button

        except Exception as e:
            # print(f"Error: {e}")
            err_msg = str(e.args).replace("\r", "").replace("\n", "").replace("\t", "") # e.args 返回一个包含错误信息的元组，元组中的每个元素可能都是一个字符串,将错误信息转为一行
            # self.save_data('error2.txt', err_msg)

    def sess(self):
        random_num = random.randrange(10000000, 99999999)
        proxy = f"http://7651076-b73d0fb0:a1d09de6-US-{random_num}@gate-us.kkoip.com:16700" #
        session.proxies = {
            'http': proxy,
            'https': proxy
        }
        print(proxy)
        return random_num

    def save_data(self, filename, data):
        with open(filename, 'a', encoding='utf-8') as wr:
            wr.write(data + '\n')



    # test = Test()
    # for line in lines:
    # test.func('com.pingvigames.hidden.objects.find.items')


 # def sess():
        #     random_num = random.randrange(10000000, 99999999)
        #     proxy = f"http://7651076-b73d0fb0:a1d09de6-US-{random_num}@gate-us.kkoip.com:16700"  #
        #     session.proxies = {
        #         'http': proxy,
        #         'https': proxy
        #     }
        #     print(proxy)
        #     pass


# def sess():
#     random_num = random.randrange(10000000, 99999999)
#     proxy = f"http://7651076-b73d0fb0:a1d09de6-US-{random_num}@gate-us.kkoip.com:16700"  #
#     session.proxies = {
#         'http': proxy,
#         'https': proxy
#     }
#     print(proxy)

# def func(packge):
#     try:
#         url1 = f'https://play.google.com/store/apps/details?id={packge.strip()}&pcampaignid=merch_published_cluster_promotion_battlestar_collection_new_games&gl=US'
#         url2 = "https://api.sealionproxy.com/check/myip?t={RAND}"
#         response = session.get(url=url1, headers=headers)
#         response2=session.get(url=url2,headers=headers)
#         data =json.loads(response2.text)
#         ip = data['ip']
#         response.encoding = 'utf-8'
#         sel = parsel.Selector(response.text)
#         URL = response.url
#         # daili = proxy
#         AfwdI = sel.css('h1 span.AfwdI::text').get()  # 游戏名
#         UIuSk = sel.css('div span.UIuSk::text').get()  # 包含广告
#         # pj = sel.css('div.wVqUob div.g1rdde::text').get()
#         starRating = sel.css('div.TT9eCd::text').getall()[0]  # 评分
#         download_count = sel.css('div.wVqUob div.ClM7O::text').get()  # 下载量
#         contentRating = sel.css('div.g1rdde span span::text').get()  # 适应年龄段
#         button = sel.css('span.VfPpkd-vQzf8d::text').get()  # 下载按钮
#         country = sel.css("div.AJ34ce div.yVZQTb::text").get()  # 国家
#         if button == 'Install':
#             button = True
#         else:
#             button = False
#
#         data = json.dumps({
#             "url": URL,
#             "ip":ip,
#             # "proxy": daili,
#             UIuSk: UIuSk,
#             "AfwdI": sel.css('h1 span.AfwdI::text').get(),
#             # "pj": sel.css('div.wVqUob div.g1rdde::text').get(),
#             "starRating": sel.css('div.TT9eCd::text').getall()[0],
#             "download_count": sel.css('div.wVqUob div.ClM7O::text').get(),
#             "contentRating": sel.css('div.g1rdde span span::text').get(),
#             "install": button,
#             "contury": country
#         })
#         # save_data(data)
#         print(data)
#
#     except Exception as e:
#         print(traceback.format_exc())

def safe_pop(lines: list, _lock: threading.Lock):
    with _lock:
        try:
            package = lines.pop()
            if package is not None and package != "":
                return package
            return None
        except Exception:
            return None


def worker(lines: list, _lock: threading.Lock):
    test = Test()
    while True:
        package = safe_pop(lines, _lock)
        if package is None:
            break
        test.func(package)
        # print(f"剩余列表长度: {len(lines)}")


futures = []
mutex = threading.Lock()
with ThreadPoolExecutor(50)as t:
#     # for line in lines:
#     #     url1 = f'https://play.google.com/store/apps/details?id={line.strip()}&pcampaignid=merch_published_cluster_promotion_battlestar_collection_new_games&gl=US'
#     #     t.submit(func, url1)
    for _ in range(50):
        futures.append(t.submit(worker, lines, mutex))
wait(futures)
# for package in lines:
#     sess()
#     func(package)


