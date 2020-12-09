# Beautifulsoup 모델을 이횽해 XML과 HTML 문서 읽어 처리

html_data = """
<html><body>
<h1>제목태그</h1>
<p>웹페이지를 분석</p>
<p>원하는 자료 추출</p>
</body></html>
"""
print(type(html_data))  # <class 'str'>

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_data, 'html.parser')
print(type(soup))  # <class 'bs4.BeautifulSoup'>
h1 = soup.html.body.h1  # html태그안의 body태그 안의 h1을 추출
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling  # 두번째 p태그가 p태그끼리 동급이기 때문에 시블링 처리를 해줘서 다음 태그속성을 부름
# next_sibling하면 </p>로 태그 뒤로 이동함 그래서 시작점까지 맞춰주려고 2번사용

# print(h1) # <h1>제목태그</h1>
print("h1 : ", h1.string)  # 제목태그 >>> 태그안의 값만 추출    <>여기값<>
print("p1 : ", p1.string)
print("p2 : ", p2.string)

print("\nfind() 메소드로 찾기")

html_data2 = """
    <html><body>
    <h1 id='title'>제목태그</h1>
    <p>웹페이지를 분석</p>
    <p id='my'>원하는 자료 추출</p>
    </body></html>
"""
soup2 = BeautifulSoup(html_data2, 'lxml')
print(soup2.p)
print(soup2.p.string)
print(soup2.find('p').string)
print(soup2.find('p', id='my').string)
print("#title:" + soup2.find(id='title').string)  # #은 id
print("#my:" + soup2.find(id='my').string)  # #은 id

print("\nfind_all() 메소드로 여러 개의 대상을 찾기")
html_data3 = """
    <html><body>
    <h1 id='title'>제목태그</h1>
    <p>웹페이지를 분석</p>
    <p id='my'>원하는 자료 추출</p>
    <div>
        <a href="https://www.naver.com">naver</a><br>
        <a href="https://www.daum.net">daum</a>
    </div>
    </body></html>
"""
soup3 = BeautifulSoup(html_data3, 'lxml')
print(soup3)
# print(soup3.prettify())

print(soup3.find('a'))  # 제일 첫번째 a태그 출력
print(soup3.find('a').string)  # a태그 안의 값
print(soup3.find(['a']))
print(soup3.find_all(['a']))
print(soup3.findAll(['a']))  # 여러개의 태그를 찾을때 []
print(soup3.findAll('a'))  # 단수 태그
print()
links = soup3.findAll('a')

for i in links:
    href = i.attrs['href']  # a태그의 attribute중 href
    text = i.string  # <>값</> 
    print(href, ' ', text)

print(soup3.find_all('p'))
print(soup3.find_all(['p', 'h1']))

print("정규 표현식")
import re
links2 = soup3.findAll(href=re.compile(r'^https://'))
print(links2)
for i in links2:
    print(i.attrs['href'])

print("***" * 10)
print('Css selector 사용')

html_data4 = """
<html><body>
<div id='hello'>
    <a href="https://www.naver.com">naver</a>
    <ul class='world'>
        <li>안녕</li>
        <li>반갑다</li>
    </ul>
</div>
</body></html>
"""
soup4 = BeautifulSoup(html_data4, 'lxml')
aa = soup4.select_one("div#hello > a").string # div태그의 id가 hello인것 안의 a태그의 값
print("aa : ", aa)

ul = soup4.select("div#hello > ul.world > li") # div태그의 id가 hello인것 중 ul에서 class가 world인것에 대한 li (여러개)
for i in ul:
    print("li : ", i.string)


