# 일반 텍스트 파일(dict type 모양을 갖춤)을 읽어 dict type으로 처리하기

import ast

with open('abc.txt', 'r') as f1:
    aa = eval(f1.read()) # 보안에 취약함 - eval 함수는 문자를 PHP 함수로 인식하여 출력하는 취약점을 갖고 있다. - 그렇기 때문에 공격자가 eval 함수를 사용하는것을 알게되면, 악성 쿼리문을 인젝션할 수 있다.
    print(aa)
    print(type(aa)) # <class 'dict'>

print()

with open('abc.txt', 'r') as f2:
    bb = f2.read()
    print(bb)
    print(type(bb)) # <class 'str'>
    cc = ast.literal_eval(bb) # str type을 dict type으로 변환을 시킴
    print(cc)
    print(type(cc)) # <class 'dict'>
     

