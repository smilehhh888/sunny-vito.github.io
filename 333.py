import requests
import json
headers1={
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'

}
data1 = {
'nType': 'prcmNotices',
'pType': '',
'prcmPrjName': '',
'prcmItemCode': '',
'prcmOrgName': '',
'startDate': '2024-01-01',
'endDate': '2024-10-21',
'prcmPlanNo': '',
'page': 1,
'pageSize': 18
}
url="http://www.ccgp-hunan.gov.cn/mvc/getNoticeList4Web.do"
responce = requests.post(url=url,headers=headers1,data=data1)
result = json.loads(responce.text)
for i in result['rows']:
    NOTICE_TITLE = i['NOTICE_TITLE']
    AREA_NAME = i['AREA_NAME']
    print(NOTICE_TITLE,AREA_NAME)
