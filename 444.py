import requests
import re
str1 = '<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" /><link rel="search" type="application/opensearchdescription+xml' \
       '" href="/content-search.xml" title="百度搜索"  title="百度搜索2" />'

# 需求 匹配 百度搜索 百度搜索2
print(re.findall('title=".*?"',str1))
print(re.findall('title="(.*?)"',str1))
print(re.findall('title="(.*)"',str1))

str2 = '卫1星a俯?瞰c祖:国\南1/北*春<耕>好|风光'
result =  re.sub("[\\\\/:*?\"<>|]","",str2)
print(result)

str3= re.findall("[\u4e00-\u9fa5]",str2)
result2 = "".join(str3)
print(result2)