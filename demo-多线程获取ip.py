import threading
from concurrent.futures.thread import ThreadPoolExecutor
import requests
import random
import json
url2 = "https://api.finemob.com/check/myip?t={RAND}"
headers = {
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
}

session = requests.Session()
def sess(_lock:threading.Lock):
    try:
        with _lock:
            random_num = random.randrange(10000000, 99999999)
            proxy = f"7651076-b73d0fb0:a1d09de6-US-{random_num}@gate-us.kkoip.com:16700"
            res = session.get(url=url2.format(RAND=random_num),proxies={'http':proxy,'https':proxy},headers=headers)
            data = json.loads(res.text)
            print(data['ip'])

    except Exception as e:
        print(e)

metux = threading.Lock()
with ThreadPoolExecutor(100) as t:
    for _ in range(100):
        t.submit(sess,metux)

# import requests
# import random
# import json
# import socket
#
# from requests import session

# headers = {
#     'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
# }
# def socks5():
#     random_num = random.randrange(10000000, 99999999)
#     socket.set_default_proxy(socks.SOCKS5,f"7651076-b73d0fb0:a1d09de6-US-{random_num}@gate-us.kkoip.com,16700")
#     socket.socket=socks.socksocket
#     s = socket.create_connection('www.google.com',80)
#     pass
# for _ in range(10):
#     socks5()
#     res =requests.get(url=url,headers=headers)
#     data = json.loads(res.text)
#     print(data['ip'])
# session = requests.Session()
# url2 = "https://api.finemob.com/check/myip?t={RAND}"
# response2 = session.get(url=url2, headers=headers)
# data2 = json.loads(response2.text)
# ip = data2['ip']
# print(ip)
#
#
# def sess():
#     random_num = random.randrange(10000000, 99999999)
#     proxy = f"7651076-b73d0fb0:a1d09de6-US-{random_num}@gate-us.kkoip.com:16700"  # 7651076-b73d0fb0:a1d09de6-US-61965013@gate-us.kkoip.com:16700 https://api.finemob.com/check/myip
#     session.proxies = {
#         'http': proxy,
#         'httos': proxy
#     }
#     print(proxy)
#     return random_num

    # res = session.get(url+str(random_num), headers=headers)
    # data = json.loads(res.text)
    # print(data['ip'])
