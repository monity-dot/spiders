import requests
import re
from bs4 import BeautifulSoup
import os,time
import webbrowser
scihub_1='https://sci-hub.ren/'
doi=input("输入DOI")
url=scihub_1+doi
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
data=soup.find_all('a')
data=re.findall('<a href="#" onclick="location.href=\'(.*?)\'">⇣ save</a>',str(data))
data=str(data)
data=data.replace("['","")
data=data.replace("']","")
webbrowser.open(data)