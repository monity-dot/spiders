import requests
import re
from bs4 import BeautifulSoup
import os,time
import webbrowser
href_page='https://xueshu.baidu.com/usercenter/paper/show?paperid=14c5cbcadca0ee253935276c74f9c0ee&site=xueshu_se'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}
res = requests.get(href_page,headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
href_finder=soup.find_all('a')
print(href_finder)