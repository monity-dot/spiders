import requests
import re
from bs4 import BeautifulSoup
import os,time
import webbrowser
url='http://mobile.pinduoduo.com/search_result.html?search_key=%E8%8F%A0%E8%90%9D&search_type=goods&source=index&options=1&search_met_track=manual&refer_page_el_sn=99884&refer_page_name=search_result&refer_page_id=10015_1623484485319_dcv7xh1wv5&refer_page_sn=10015&page_id=10015_1623490361848_b3uqnn1tvr&bsch_is_search_mall=&bsch_show_active_page=&flip=0%3B0%3B0%3B0%3B51cdaf28-159a-e9ea-b077-c5180dd6f91d%3B%2F10%3B8%3B2%3B74180ffef27a923b7ecc9ca452d2fbf3&item_index=2'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
print(soup)
url_list_data=soup.find_all('div')
print(url_list_data)