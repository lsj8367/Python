# JSON

import json

dict = {'name':'tom', 'age':22, 'score':['90','80','100']}
print(dict, type(dict))

print('인코딩-------------')
str_val = json.dumps(dict) # dict타입을 모양만 dict인 str형태로 변환 인코딩시킴
print(str_val, type(str_val))
print(str_val[0:20]) # 문자열 관련 명령어
#print(str_val['name']) # dict 관련 명령 에러발생!

print('디코딩--------')
json_val = json.loads(str_val)
print(json_val, type(json_val))
print(json_val['name'])
#print(json_val[0:20]) # 에러 발생 dict라서

print('^^^^^^^^^^^^' * 10)
#웹에서 json 자료 읽기
import urllib.request as req

url = "http://openapi.seoul.go.kr:8088/sample/json/SeoulLibraryTime/1/5/"
plainText = req.urlopen(url).read().decode()
print(plainText, ' ', type(plainText)) #  <class 'str'>

jsonData = json.loads(plainText)
print(jsonData, ' ', type(jsonData)) # <class 'dict'>
print(jsonData['SeoulLibraryTime']['row'][0]['LBRRY_NAME'])

print()
libData = jsonData.get('SeoulLibraryTime').get('row')
print(libData)

name = libData[0].get('LBRRY_NAME')
print(name)

print('-------------------------')
for ele in libData:
    name = ele.get('LBRRY_NAME')
    tel = ele.get('TEL_NO')
    addr = ele.get('ADRES')
    print(name + "\t" + tel + "\t" + addr)
