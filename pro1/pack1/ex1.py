'''
여러줄 주석
또는 문자열 처리
'''
from builtins import isinstance

"""
이것 또한 같은 기능 
"""

# 한줄주석
# 변수
var1 = '안녕파이썬' # '나 " 둘다 사용가능 관계없다 
print(var1) 
var1 = 5; print(var1) # 들어오는 값에따라 타입이 결정된다. 한줄에 문법 2개를 쓰려면 ;을 사용해야한다.

a = 10 # 객체의 주소 기억. 참조형 변수이며 기본형은 없다.
b = 20.5
c = b # b의 주소 치환
print(a, b, c)
print("주소 : ", id(a), id(10), ' ' , id(b), id(20.5), id(c)) # 주소를 참조하기 때문에 변수와 그 뒤의 값의 주소가 같을수밖에 없다
print(a is b, a == b) # is : 주소값 비교, == : 값 비교
print(b is c, b == c)

A = 1; a = 2; # 대소문자 구분
print("A + a : ", A + a, id(A), id(a))

# for = 10 예약어는 변수사용 X
import keyword
print('예약어 목록 : ', keyword.kwlist)

print(10, oct(10),  hex(10), bin(10)) # 10 0o12 0xa 0b1010
print(10, 0o12, 0xa, 0b1010)

# type 확인
print(1, type(1))
print(1.2, type(1.2))
print(1 + 2j, type(1 + 2j))
print(True, type(True))
print("1", type("1"))
print()
print((1,), type((1,)))
print([1], type([1]))
print({1}, type({1}))
print({'k':1}, type({'k':1}))
print()

print(isinstance(1, int))
print(isinstance(1, float))

