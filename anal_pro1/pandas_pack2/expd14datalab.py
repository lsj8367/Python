from bs4 import BeautifulSoup
import requests # urllib랑은 다르게 제약이있을수 있음
# 보는페이지 코드와 다르다면 headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'})
data = requests.get("https://datalab.naver.com/keyword/realtimeList.naver?age=20s", headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}).text
#print(data)
soup = BeautifulSoup(data, 'lxml')
#print(soup)
list = soup.findAll('span', 'item_title_wrap')
#print(list)

count = 1
for i in list:
    key = i.find('span')
    #print(key)
    print("{}위 : {}".format(count, key.string))
    count += 1