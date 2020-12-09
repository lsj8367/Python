# 홍길동전(완판본)을 스크래핑 한 후 가장 많이 등장하는 단어 10위까지 출력
import urllib.request as req
from bs4 import BeautifulSoup
from konlpy.tag import Okt
url ='http://www.seelotus.com/gojeon/gojeon/so-seol/hong-kil-dong-wan-pan-bon.htm'

okt = Okt()
data = req.urlopen(url)
#print(data)

soup = BeautifulSoup(data, 'lxml')
#print(soup)
#body > table > tbody > tr > td > p:nth-child(4)


datas = soup.select('body > table > tr > td > p')
#print(datas)
list = []
for i in datas:
    if i.string != None:
        a = i.string
        list += okt.nouns(a)
        
print(list)

list_dict = {}

for i in list:
    if len(i) > 1:
        if i in list_dict: # 중복이되면 숫자늘림(빈도수 출력)
            list_dict[i] += 1
        else:
            list_dict[i] = 1
#print(list_dict)

import pandas as pd
df = pd.DataFrame([list_dict.keys(), list_dict.values()])
df = df.T
df.columns = ['단어', '빈도수']
df2 = df.sort_values(by=['빈도수'], axis=0, ascending=False)
print(df2)

df2 = df2.head(10)
df2.to_excel('홍길동.xlsx', sheet_name='Sheet1', index=False)


