'''
정규표현식

-특정한 규칙을 가진 문자열의 집합을 표현하는데 사용하는 형식 언어.
-Programming Language나 Text Editor 등 에서 문자열의 검색과 치환을 위한 용도로 사용.
-입력한 문자열에서 특정한 조건을 표현할 경우 일반적인 조건문으로는 다소 복잡할 수도 있지만, 정규 표현식을 이용하면 매우 간단하게 표현
-코드가 간단한 만큼 가독성이 떨어져서 표현식을 숙지하지 않으면 이해하기 힘들다는 문제점 
- 파이썬에서 정규식은 re 모듈이 제공

\s         공백문자(스페이스,탭등)
\*          *
\D        숫자가 아닌 문자
^           문자의 시작부분  ex)/^The/i
$           문자열 끝부분                     ex)/end$/ 
\w       알파벳,숫자,밑줄기호(_)
[^0-9]    숫자를 제외한
[0-9]     숫자만
[A-Za-z]알파벳 대소문자
|           or
s{2}      s의 두번 반복  {반복 횟수}
속성
g            전역 매칭
m           여러 줄 매칭
i             대소문자 구분 않음
문자 매칭
*           0회 이상 반복
+           1회 이상 반복
?           0 or 1개의 문자 매칭
.           1개의 문자 매칭
'''
import re
from re import IGNORECASE

ss = '1234 abc가나다ABC_%%%_6_1234마바사abcabc'
print(re.findall(r'123', ss))
print(re.findall(r'가나다', ss))
print(re.findall(r'[0-9]', ss))
print(re.findall(r'[0-9]+', ss))
print(re.findall(r'[a-zA-Z가-힣]{2,3}', ss))
print(re.findall(r'.bc', ss))
print(re.findall(r'..c', ss))
print(re.findall(r'^1+', ss))
print(re.findall(r'[^a-zA-Z가-힣]{2,3}', ss)) # []안에 ^이 들어가면 부정
print(re.findall(r'\d{1,3}', ss))

print("------")
m = re.match(r'[0-9]*', ss)
print(m)
print(m.group()) # match의 결과는 이렇게 출력

print("------")
p = re.compile('the', re.IGNORECASE) # flag 사용
print(p.findall("The dog the dog")) # 대소문자 구분 X

print()
s = '''My name is tom
I am happy'''
print(s)

p = re.compile("^.+", re.MULTILINE)
print(p.findall(s))



