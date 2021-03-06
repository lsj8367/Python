'''
구글 검색 기능 이용 : 검색결과의 개수만큼 브라우저의 탭을 열어 a tag의 결과 출력
'''
import requests
from bs4 import BeautifulSoup
import webbrowser # 브라우저띄우기

def searchFunc():
    base_url = "https://www.google.com/search?q={0}"
    sword = base_url.format('파이썬')
    print(sword)
    plain_text = requests.get(sword, headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'})
    print(plain_text)
    soup = BeautifulSoup(plain_text.text, 'lxml')
    #print(soup)
    #link_data = soup.select('a')
    #rso > div:nth-child(3) > div > div.yuRUbf
    link_data = soup.select('div > div.yuRUbf > a')
    #print(link_data)
    for link in link_data[:3]:
        #print(link)
        #print(type(link), ' ', type(str(link)))
        #print(str(link).find('https'), ' ', str(link).find('onmousedown') - 2) # onmousedown글자 앞으로 2칸 시작위치와 끝위치     9   66    이렇게 나옴
        urls = str(link)[str(link).find('https') : str(link).find('onmousedown') - 2] # str(link)[시작 : 끝] 슬라이싱
        print(urls) # https://namu.wiki/w/Python 이런 형식
        
        webbrowser.open(urls)
        
searchFunc()
