import requests
import re
from bs4 import BeautifulSoup
import os,time
import webbrowser
url='http://mobile.pinduoduo.com/goods_comments.html?goods_id=88274123555&_oc_refer_ad=0&_x_query=%E8%8F%A0%E8%90%9D&refer_page_el_sn=99369&refer_rn=&refer_page_name=goods_detail&refer_page_id=10014_1624104595418_pij8t0yc5f&refer_page_sn=10014&mall_id=428894768'

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}
res = requests.get(url,headers=headers)

soup=BeautifulSoup(res.text,'html.parser')
print(soup)
data=soup.find_all('li')
#datax=re.findall('</span>(.*?)</li>',str(data))
#print(data)
data_good_comments=re.findall('<li class="_2kK8WYHF">(.*?)</li>',str(soup))

print(data_good_comments)

for i in data_good_comments:
    if (i.research()):
        print(re.search(r'span class',data_good_comments[j]),re.M|re.I)

print(data_good_comments)
data_bad_comments=re.findall('<li class="_2kK8WYHF _3Kcid9Mj">(.*?)</li>',str(data))
print(data_bad_comments)