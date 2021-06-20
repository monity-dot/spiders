import requests
import re
from bs4 import BeautifulSoup
import os,time
import webbrowser
final_page='https://xueshu.baidu.com/usercenter/paper/show?paperid=14c5cbcadca0ee253935276c74f9c0ee&site=xueshu_se'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}
res = requests.get(final_page,headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
finder=soup.find_all('p')
#print(finder)
finder=re.findall('''<p class="label">DOI：</p>, <p class="kw_main" data-click="{'button_tp':'doi'}">
            (.*?)
        </p>, <p>被引量：</p>, <p class="ref-wr-num">''',str(finder))
print(finder)
