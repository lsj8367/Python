# 웹 문서를 읽어 형태소 분석
import urllib
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from urllib import parse # 한글 인코딩용 모듈

okt = Okt()
#para = '이순신'
para = parse.quote('이순신') # 한글 인코딩 
url = "https://ko.wikipedia.org/wiki/" + para
print(url) # https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%88%9C%EC%8B%A0
page = urllib.request.urlopen(url) # 인코딩을 해줘서 넘겨야함
print(page)

soup = BeautifulSoup(page.read(), 'lxml')
#print(soup) # #mw-content-text > div.mw-parser-output > p:nth-child(5)

wordlist = []
for item in soup.select('#mw-content-text > div > p'):
    #print(item)
    if item.string != None:
        #print(item.string)
        ss = item.string
        #print(okt.nouns(ss))
        #wordlist.append(okt.nouns(ss))
        wordlist += okt.nouns(ss)

print('wordlist :', wordlist)
print('단어 수 : ', str(len(wordlist)))
print()

word_dict = {} # 단어의 횟수를 dict type으로 기억
for i in wordlist:
    if i in word_dict: # 중복이되면 숫자늘림(빈도수 출력)
        word_dict[i] += 1
    else:
        word_dict[i] = 1
        
print('word_dict : ', word_dict)

setData = set(wordlist) # 중복 제거 ? : set타입으로 넣었기 때문
print('중복이 없는 단어 수 :', str(len(setData)))

print('\nSeries type으로 처리')
import pandas as pd

woList = pd.Series(wordlist)
print(woList.head(3))
print(woList.value_counts()[:5])

print()
woDict = pd.Series(word_dict)
print(woDict[:3])
print(woDict.value_counts()[:5])

print('\nDataFrame으로 출력 -------')
df1 = pd.DataFrame(wordlist, columns = ['단어'])
print(df1.head(3))
print()

df2 = pd.DataFrame([word_dict.keys(), word_dict.values()])
df2 = df2.T
df2.columns = ['단어', '빈도수']
print(df2.head(5))

df2.to_csv('이순신.csv', sep=',', header=True, index=False)
df3 = pd.read_csv('이순신.csv')
print(df3.head(5))
