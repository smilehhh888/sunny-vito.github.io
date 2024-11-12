import json
from concurrent.futures import ThreadPoolExecutor
import requests
import parsel
import threading

mutex = threading.Lock()

headers = {
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
}

proxies1={
    "https": 'http://127.0.0.1:10809'
}

with open("packages241015（1）.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()


def save_data(data):
    with open("data.txt", 'a', encoding='utf-8') as wr:
        wr.write(data+'\n')

def func(url1):
    try:
        response = requests.get(url=url1, headers=headers, proxies=proxies1)
        response.raise_for_status()
        sel = parsel.Selector(response.text)
        title = sel.css('h1 span.AfwdI::text').get()
        pj = sel.css('div.wVqUob div.g1rdde::text').get()
        code = sel.css('div.TT9eCd::text').getall()[0]
        download = sel.css('div.wVqUob div.ClM7O::text').get()
        tj = sel.css('div.g1rdde span span::text').get()
        button = sel.css('span.VfPpkd-vQzf8d::text').get()
        data = json.dumps({
            "title": title,
            "pj": pj,
            "code": code,
            "download": download,
            "tj": tj,
            "button": button
        })
        save_data(data)
        print(data)
    except Exception as e:
        print(f"Error processing URL: {url1}")
        print(str(e))

thread_pool = ThreadPoolExecutor(100)
for line in lines:
    url1 = f'https://play.google.com/store/apps/details?id={line.strip()}&pcampaignid=merch_published_cluster_promotion_battlestar_collection_new_games&gl=US'
    thread_pool.submit(func, url1)