# 웹에서 특정 단어 검색 후 '명사'들만 추출해 빈도수를 구한 후 워드클라우드 출력
# pip install pygame
# pip install simplejson
# pip install pytagcloud

from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote

#keyword = input('검색어를 입력하세요 : ') # 원래는 줘야함
keyword = '감기'
print(quote(keyword)) # 인코딩

target_url = "https://www.donga.com/news/search?query={}".format(quote(keyword))
print(target_url)

source_code = urllib.request.urlopen(target_url)
soup = BeautifulSoup(source_code, 'lxml')
#print(soup)

msg = ""
for title in soup.find_all('p', 'tit'): # p태그 속성중 tit만 불러옴
    title_link = title.select('a') # 그중 a태그
    #print(title_link)
    article_url = title_link[0]['href'] # 그안의 href속성 값들 불러옴
    #print(article_url) # https://bizn.donga.com/3/all/20201110/103885653/2...
    
    source_article = urllib.request.urlopen(article_url) # 각각의 a태크 본문 스크래핑 href링크를 하나씩 다 열음
    soup = BeautifulSoup(source_article, 'lxml', from_encoding='utf-8')
    contents = soup.select('div.article_txt') # 열은것에서 div class="article_txt"인 애를 불러와서 읽음
    for imsi in contents:
        item = str(imsi.findAll(text = True)) # 글자만 가져올것임
        #print(item)
        msg = msg + item

# print(msg)

from konlpy.tag import Okt
from collections import Counter
nlp = Okt()

nouns = nlp.nouns(msg) # 명사만 추출
result = [] # 두글자 이상의 단어만 담기위한 list 변수
for imsi in nouns: 
    if len(imsi) > 1: # 두글자 이상의 것만 list에 넣기
        result.append(imsi)

print(result)
count = Counter(result) # 똑같은 단어 셈해주기
print(count)

tag = count.most_common(50) # 상위 50개의 명사만 작업에 참여

import pytagcloud
taglist = pytagcloud.make_tags(tag, maxsize = 100) # 태그를 생성, color 등등 설정을 안주면 빈도에따라서 색과 크기가 자동으로 나뉘게 됨
print(taglist) # 한글 글꼴이 없으면 깨지기 때문에 글꼴 다운


# tag_image 생성 후 저장
# output = 이름 fontname은 json안에 Name값
pytagcloud.create_tag_image(taglist, 'word.png', size = (1000, 600), fontname = 'korean', rectangular = False) # word.png로 저장됨
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# img = mpimg.imread('word.png') #이미지 로드
# plt.imshow(img)
# plt.show()

import webbrowser
webbrowser.open('word.png') # 웹브라우저로 띄우기