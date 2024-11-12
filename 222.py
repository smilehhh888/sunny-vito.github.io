import requests
import json
import re
wd = input("请输入关键字：")
url1 ="https://www.baidu.com/sugrec?pre=1&p=3&ie=utf-8&json=1&prod=pc&from=pc_web&sugsid=60277,60885,60875&wd=%E5%8D%97%E9%A3%8E&his=%5B%7" \
      "B%22time%22%3A1723733804%2C%22kw%22%3A%22python%E8%A7%A3%E5%86%B3js%22%2C%22fq%22%3A2%7D%2C%7B%22time%22%3A1723733815%2C%22kw%22%3A%" \
      "22python%E7%88%AC%E8%99%AB%E8%A7%A3%E5%86%B3js%22%2C%22fq%22%3A2%7D%2C%7B%22time%22%3A1724025699%2C%22kw%22%3A%22%E6%96%B0%E7%96%86" \
      "%E5%B7%A5%E7%A8%8B%E5%AD%A6%E9%99%A2%22%2C%22fq%22%3A2%7D%2C%7B%22time%22%3A1724049447%2C%22kw%22%3A%22%E7%88%AC%E8%99%AB%E8%A1%A8%E" \
      "5%8D%95%22%2C%22fq%22%3A2%7D%2C%7B%22time%22%3A1724115026%2C%22kw%22%3A%22csdn%22%2C%22fq%22%3A2%7D%2C%7B%22time%22%3A1724115086%2C" \
      "%22kw%22%3A%22%E7%88%AC%E8%99%AB%E8%8E%B7%E5%8F%96%E7%9A%84%E5%93%8D%E5%BA%94%E5%92%8C%E5%85%83%E7%B4%A0%E7%95%8C%E9%9D%A2%E4%B8%8D%" \
      "E4%B8%80%E6%A0%B7%22%2C%22fq%22%3A4%7D%2C%7B%22time%22%3A1724750349%2C%22kw%22%3A%22%E6%99%BA%E6%85%A7%E5%9B%A2%E5%BB%BA%E5%AE%98%E" \
      "7%BD%91%22%2C%22fq%22%3A2%7D%2C%7B%22time%22%3A1725331216%2C%22kw%22%3A%22%E7%BD%91%E6%98%93%E6%96%B0%E9%97%BB%22%2C%22fq%22%3A2%7" \
      "D%2C%7B%22time%22%3A1729479945%2C%22kw%22%3A%22%E8%B0%B7%E6%AD%8C%22%2C%22fq%22%3A2%7D%2C%7B%22time%22%3A1729488937%2C%22kw%22%3A%" \
      f"22%E8%85%BE%E8%AE%AF%E6%8B%9B%E8%81%98%22%2C%22fq%22%3A10%7D%5D&req=2&csor=2&wd={wd}&cb=jQuery1102009035099994724871_1729493250" \
      "508&_=1729493250516"
headers = {
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

responce = requests.get(url=url1,headers=headers)
data = re.findall('jQuery.*?\((.*?)\)', responce.text)[0]
responce_data = json.loads(data)
for i in responce_data['g']:
      name = i['q']
      print(name)
