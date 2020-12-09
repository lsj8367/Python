# BeautifulSoup 모듈로 wikipedia 자료 읽기
import urllib.request as req
from bs4 import BeautifulSoup

url = "https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%88%9C%EC%8B%A0"
wiki = req.urlopen(url)
print(wiki)

#soup = BeautifulSoup(wiki, 'html.parser')
soup = BeautifulSoup(wiki.read().decode('utf-8', 'ignore'), 'lxml')
print(soup)
# 웹사이트에서 copy selector
# #mw-content-text > div.mw-parser-output > p:nth-child(13)
print(soup.select("#mw-content-text > div.mw-parser-output > p"))

print('^^^' * 20)
#daum 사이트의 뉴스정보 읽기

url2 = "https://news.v.daum.net/v/20201112100744370"
daum = req.urlopen(url2)
print(daum)
soup2 = BeautifulSoup(daum, 'lxml')

# css selector
print(soup2.select_one("div#kakaoIndex > a").string)
datas = soup2.select("div#kakaoIndex a") #하위멤버중 a태그전체
print(datas)
print()
for i in datas:
    #print(i)
    href = i.attrs['href']
    text = i.string
    print("href:%s, text:%s"%(href, text))
    print("href:{}, text:{}".format(href, text))

print()
# find() 이용
#datas2 = soup2.findAll('a')
datas2 = soup2.find_all('a')
print(datas2)
for i in datas2[:2]:
    href = i.attrs['href']
    text = i.string
    print("href:%s, text:%s"%(href, text))

print() #본문 자료 읽기
#harmonyContainer > section > p:nth-child(13)
datas3 = soup2.select('#harmonyContainer > section > p')
print(datas3)
print()
for i in datas3[:3]:
    print(i.string)