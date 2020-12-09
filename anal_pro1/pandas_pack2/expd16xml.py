# BeautifulSoup으로 XML data 처리
from bs4 import BeautifulSoup

with open('my.xml', mode = 'r', encoding = 'utf-8') as f:
    xmlfile = f.read()
    print(xmlfile, type(str))
    
soup = BeautifulSoup(xmlfile, 'html.parser')
print(type(soup))
#print(soup.prettify()) # 다듬고 보기
itemTag = soup.findAll('item')
print(itemTag[0])

print()
nameTag = soup.find_all('name')
print(nameTag[0]['id']) # 0번째name태그의 id값
print()

for i in nameTag:
    print(i['id'])

print('---------------')

for i in itemTag:
    nameTag = soup.findAll('name')
    for j in nameTag:
        print("id : ", j['id'] + 'name, ' + j.string)
        tel = i.find('tel')
        print('tel :', tel.string)

        print()
        
        for j in i.find_all('exam'):
            print('kor :' +  j['kor'] + ' eng :' + j['eng'])

print("**************************")
# 웹에서 XML 문서 읽기  - 도서관 정보
import urllib.request as req

url = "http://openapi.seoul.go.kr:8088/sample/xml/SeoulLibraryTime/1/5/"
plainText = req.urlopen(url).read().decode()
print(plainText)

xmlObj = BeautifulSoup(plainText, 'lxml')
libData = xmlObj.select('row')

for d in libData:
    name = d.find('lbrry_name').text
    addr = d.find('adres').text
    print('도서관명 : ' + name, ' 주소 :' + addr)
    



