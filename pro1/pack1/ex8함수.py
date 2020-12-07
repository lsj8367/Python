'''
모듈(module)의 멤버 중 함수(function)
 여러개의 수행문을 하나의 이름으로 묶은 실행 단위
 코드관리가 효과적
 프로그램을  논리적으로 구성할 수 있다.
 내장함수와 사용자정의 함수 
'''
# 내장함수 : python 또는 제3자 (third party)가 지원하는 함수
print(sum([3,5,7]), sum((3,5,7)))
print(int(1.7), float(3), str(5) + '오')

a = 10
b = eval('a + 5')
print(b)

print(round(1.2), round(1.6)) # 반올림
import math
print(math.ceil(1.2), math.ceil(1.6)) # 근사치중 큰 수
print(math.floor(1.2), math.floor(1.6)) # 근사치중 작은 수 반환

b_list = [True, False]
print(all(b_list)) # 모두 참일때 참
print(any(b_list)) # 하나라도 참이면 참

b_list = [1,3,2,5,9,6]
res = all(a < 10 for a in b_list)
print('모든 숫자가 10미만이냐', res)
res = any(a < 3 for a in b_list)
print('숫자중 3미만 있냐', res)

print()
x = [10, 20, 30]
y = ['a', 'b']
for i in zip(x, y): # zip => 튜플타입으로 짝을지어줌
    print(i)

# (10, 'a')
# (20, 'b')

# ...

# 사용자 정의함수
print('\n\n사용자정의 함수 =========')
def Dofunc1():
    print('Dofunc1 수행')
    
def dofunc2(name):
    print('안녕', name + '님')

Dofunc1()
print('딴짓 하다가')
Dofunc1()
print('함수명은 함수 객체의 주소를 기억: ', Dofunc1)
print(type(Dofunc1))
dofunc2('paul')
print(dofunc2('paul park'))


print()
def doFunc3(arg1, arg2):
    c = arg1 + arg2
    if c % 2 == 1:
        return
    else:
        return c

print(doFunc3(10, 2))
print(doFunc3(10, 3)) # 인자값 받았을때 return이 없으면 none 출력
print(dir(__builtins__))

OtherFunc1 = Dofunc1 # 주소를 치환
OtherFunc2 = Dofunc1() # 실행결과를 치환

OtherFunc1()
OtherFunc2

print()
def swap(a,b):
    return b, a
print(swap(10, 20))

print()
# if 조건식 안에 함수 사용

def isOddFunc(arg):
    return arg % 2 == 1

print(isOddFunc(5))
print(isOddFunc(6))

myDict = {x:x*x for x in range(11) if isOddFunc(x)}
print(myDict)


