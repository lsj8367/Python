# BeautifulSoup으로 기상청 날씨 정보 읽기
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request

url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
data = urllib.request.urlopen(url).read()
#print(data.decode('utf-8'))

soup = BeautifulSoup(urllib.request.urlopen(url), 'lxml')
#print(soup)
title = soup.find('title').string
wf = soup.find('wf')
#print(title)
#print(wf)
city = soup.find_all('city')
#print(city)
cityDatas = []
for c in city:
    cityDatas.append(c.string)

df = pd.DataFrame()
df['city'] = cityDatas
# print(df)

# df에 최저기온 칼럼 추가
tmefs = soup.select_one('location > data > tmef') # 직계 자식
#print(tmefs) # <tmef>2020-11-15 00:00</tmef>

tmefs = soup.select_one('location data tmef') # 자손관계
#print(tmefs)

tmefs = soup.select_one('location > province + city + data > tmef') # 자손관계 + data 해줄수록 아래의 형식을 지나가게 된다.
''' location > province + city + data + data + data > tmef 이런식으로 가능
<data>
...
</data>
<data>
...
'''
#print(tmefs)

#print(soup.select('data > tmn')[0]) # data 밑에 tmn중 0번째

tempMins = soup.select('location > province + city + data > tmn') # 형제노드1 + 형제노드2      형제노드2 + 형제노드1
tempDatas = []
for t in tempMins:
    tempDatas.append(t.string)
    
df['temp_min'] = tempDatas
df.columns = ['지역', '최저기온'] # 칼럼명 변경
print(df.head(3), ' ', len(df))
print()
