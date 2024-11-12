import requests
import threading
from concurrent.futures import ThreadPoolExecutor,wait
from bs4 import BeautifulSoup
import random
import parsel

url1='https://namefake.com/'
headers = {
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'
}
session =requests.Session()
for page in range(100):
    random_num = random.randrange(10000000, 99999999)
    proxy = f"7651076-b73d0fb0:a1d09de6-US-{random_num}@gate-us.kkoip.com:16700"
    responce = session.get(url=url1, headers=headers, proxies={'http': proxy, 'https': proxy})
    sel = parsel.Selector(responce.text)
    soup = BeautifulSoup(responce.text,'html.parser')  # body > div:nth-child(7) > div > div.col-sm-9.col-sm-push-3 > div:nth-child(48)
    for i in range(20):
        key = str(soup.select('div.rght_h46')[i].text)
        value = str(soup.select('div.left_h46')[i].text)
        # company = soup.select('body > div:nth-child(7) > div > div.col-sm-9.col-sm-push-3 > div:nth-child(48)')[0].text
        # age = soup.select('body > div:nth-child(7) > div > div.col-sm-9.col-sm-push-3 > div:nth-child(14)')[0].text
        # contury=sel.css('div.rght_h45ed::text').get()
        # print(company,age,contury)
        dic = {
            key: value
        }
        print(dic)

