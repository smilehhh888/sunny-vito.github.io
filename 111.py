import threading

import requests
from  bs4 import BeautifulSoup
import re
from concurrent.futures import ThreadPoolExecutor

cookies = {
    'OTZ': '7786317_24_24__24_',
    'AEC': 'AVYB7cp0CSI-CszAciSr-S3VTYk1qt5RNldHpp9m0wfzuQ3ovgRPIC7JoA',
    'NID': '518=ATjHLI3UyzV9q50LgKpISZuRszuhvQE1AuU81FrYVAphq-MbOPbdMs0XK2nc_uMEim3NHfc8YK5vDaE4dlkUXiZ6u-sBeR9eWux8wV3A1Olq26AG-MFuJOaJHVu-gRj1xgb1mHqUyzp-LsZx5JwPWv93ow__d2-G8xPR748U1M2UMKMRSKJ790GRa4NalYF-ZKTzpXlSHLpL4el5hdHHsAGl01o',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'OTZ=7786317_24_24__24_; AEC=AVYB7cp0CSI-CszAciSr-S3VTYk1qt5RNldHpp9m0wfzuQ3ovgRPIC7JoA; NID=518=ATjHLI3UyzV9q50LgKpISZuRszuhvQE1AuU81FrYVAphq-MbOPbdMs0XK2nc_uMEim3NHfc8YK5vDaE4dlkUXiZ6u-sBeR9eWux8wV3A1Olq26AG-MFuJOaJHVu-gRj1xgb1mHqUyzp-LsZx5JwPWv93ow__d2-G8xPR748U1M2UMKMRSKJ790GRa4NalYF-ZKTzpXlSHLpL4el5hdHHsAGl01o',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-form-factors': '"Desktop"',
    'sec-ch-ua-full-version': '"129.0.6668.101"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="129.0.6668.101", "Not=A?Brand";v="8.0.0.0", "Chromium";v="129.0.6668.101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'x-browser-channel': 'stable',
    'x-browser-copyright': 'Copyright 2024 Google LLC. All rights reserved.',
    'x-browser-validation': 'g+9zsjnuPhmKvFM5e6eaEzcB1JY=',
    'x-browser-year': '2024',
    'x-client-data': 'CKy1yQEIk7bJAQijtskBCKmdygEI9YDLAQiUocsBCJ3+zAEI6ZjNAQiFoM0BCP2lzgEIk8bOAQi9x84BCM/HzgEIp8jOAQivyM4BCJDKzgEImMrOAQjBys4BCJjLzgEYnLHOAQ==',
}

params = {
    'id': 'com.StudioWheel.Bard',
    'pcampaignid': 'merch_published_cluster_promotion_battlestar_collection_new_games',
    'gl': 'US',
}
proxies1={
    "https":'http://127.0.0.1:10809'
}
# _lock = threading.Lock



def fun(url):
    response = requests.get(url=url, params=params, cookies=cookies, headers=headers, proxies=proxies1)
    soup = BeautifulSoup(response.text, 'html.parser')
    span_tag = soup.select("div div div h1 ")[0]
    title = span_tag.span.text
    pj = soup.select('.g1rdde')[0].text
    print(title, pj)

with open("爬虫/线程池和进程池/11111.txt", "r+", encoding='utf-8') as f:
    lines = f.readlines() # 读取文件的所有行并返回一个包含所有行的列表
with ThreadPoolExecutor(10) as t:
    for line in lines:
        url1 = f'https://play.google.com/store/apps/details?id={line.strip()}&pcampaignid=merch_published_cluster_promotion_battlestar_collection_new_games&gl=US'
        print(url1)
        # t.submit(fun, url1)







