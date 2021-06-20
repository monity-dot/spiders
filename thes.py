import requests
import re
from bs4 import BeautifulSoup
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}
res = requests.get('https://bbs.mihoyo.com/ys/obc/content/1057/detail?bbs_presentation_style=no_header',headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
data=soup.find_all('td')
g=re.findall('<td class="h3">(.*?)</td>, <td colspan="2"><div class="obc-tmpl__icon-text-num">(.*?)<span class="obc-tmpl__icon-text">(.*?)</span>',str(data))
#print(data)
h=re.sub('<td class="h3">'," ",str(g))
i=re.sub('<span class="obc-tmpl__icon-text">'," ",str(h))
j=re.sub('<.*?>',"",str(i))
k=['攻击方式','生命值','攻击力','防御力','元素精通','暴击率','暴击伤害','治疗加成','受治疗加成']
m=''
p=''
for eachk in k:
    l=re.findall(eachk+'''.*?', ' ', '(.*?)'\)''',j)
    m+=(eachk+','+str(l)+',')
    p+=str(l)
n=re.sub(',',"</item><item>",m)
print(m)
print(n)
p=p.replace("['","\"")
p=p.replace("']","\",")

p=p.replace("\', \'","\",\"")
print(p)