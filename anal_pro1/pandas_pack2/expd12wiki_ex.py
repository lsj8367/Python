# replace(',','') 가격 메뉴이름 따와서 dataframe에 넣어라
# 칼럼명 name, pay
# 상품 전체 가격의 평균, 가장비싼 메뉴 최대가격 : , 최소가격
# 표준편차 구하기
# body > div.wrapper.scrolled > div.container > article > section > div.section-body > div > div:nth-child(2) > div.info
import urllib.request as req
import pandas as pd
from bs4 import BeautifulSoup
url = 'https://www.bbq.co.kr/menu/menuList.asp'

bbq = req.urlopen(url)

soup = BeautifulSoup(bbq, 'lxml')
#print(soup)
# body > div.wrapper > div.container > article > section > div.section-body > div > div.box > div.info > p.name

listname = soup.select("div.box > div.info > p.name")
listpay = soup.select("div.box > div.info > p.pay")

#print(listname)
#print(listpay)
import re
datas = {'names' : [], 'pay': []}

for i,j in zip(listname, listpay):
    names = i.string
    menu = re.sub(r'[→(랜덤)]','',names)
    datas['names'].append(menu)
    #print(i.string)
    a = j.string.replace(',','')
    a = a.replace('원', '')
    datas['pay'].append(int(a))

#print(datas)

bbqdf = pd.DataFrame(datas, columns=['names', 'pay'])
print(bbqdf) # 데이터프레임 완성
print("평균값 : ", round(bbqdf.mean(axis=0),2)) # 가격 평균
print("최댓값 : ", bbqdf.loc[bbqdf['pay'].idxmax()]) # 가격최대
print("최소값 : ", bbqdf.loc[bbqdf['pay'].idxmin()]) # 가격 최소
print("표준편차 : ", bbqdf.std()) # 표준편차

#print(bbqdf.loc[bbqdf['pay'].idxmax()].names) # 최대값의 상품명만 얻고싶을때