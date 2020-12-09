# 네이버 영화 정보 읽기
from bs4 import BeautifulSoup

# 방법 1
import urllib.request

url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
data = urllib.request.urlopen(url)
soup = BeautifulSoup(data, 'lxml')
#print(soup)
#print(soup.select('div.tit3'))
#print(soup.select('div[class=tit3]'))
for tag in soup.select('div[class=tit3]'):
    print(tag.text.strip()) # 양쪽 공백 자를거면 strip 왼쪽 lstrip 오른 rstrip

print()
# 방법 2
import requests
data = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")
print(data.status_code, ' ', data.encoding) # 몇가지 정보 얻을 수 있다
datas = data.text
#print(datas)
datas = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.nhn").text
soup = BeautifulSoup(datas, 'lxml')
#print(soup)
#m_list = soup.findAll('div', 'tit3') # tag명, 속성 형식
m_list = soup.findAll('div', {'class':'tit3'}) # tag명, 속성 형식
print(m_list)

# 순위 표시
count = 1
for i in m_list:
    title = i.find('a')
    #print(title)
    print(str(count) + "위:" + title.string)
    count += 1



