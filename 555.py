# "rn": "开捞条！！！！"
import re

import requests


url1 = "https://www.douyu.com/gapi/rknc/directory/mixListV1/2_1227/2?readList=148986%2C10272864%2C2140364%2C9662891%2C9648364%2C11255806%2" \
       "C11824248%2C4514420%2C4794419%2C11738208%2C908352%2C12043021%2C4183243%2C9553643%2C2264536%2C7152710%2C9354254%2C11049492%2C119309" \
       "13%2C9190461%2C11454363%2C12282155%2C12246576%2C7392406%2C6807565%2C12276301%2C11541000%2C11295120"
headers = {
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}
responce = requests.get(url=url1,headers=headers)
nn_list = re.findall('"nn":"(.*?)"',responce.text)
nr_list = re.findall('"rn":"(.*?)"',responce.text)
for i,j in zip(nn_list,nr_list):
       print(i+"|||"+j)