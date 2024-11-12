import requests
import json
page=1
for page in range(10):
    url1 = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1729489020101&countryId=&cityId=&bgIds=&productId=&categoryI" \
       f"d=40001001,40001002,40001003,40001004,40001005,40001006,40002001,40002002&parentCategoryId=&attrId=&keyword=&pageIndex={page}&pageSize=1" \
       "0&language=zh-cn&area=cn"
    headers1 = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    }
    responce = requests.get(url=url1,headers=headers1)
    responce_data = json.loads(responce.text)
    for data in responce_data['Data']['Posts']:
        RecruitPostName = data['RecruitPostName']
        RequireWorkYearsName = data['RequireWorkYearsName']
        print(RequireWorkYearsName,RecruitPostName)
    page+=1
