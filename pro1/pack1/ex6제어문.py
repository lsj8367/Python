# 제어문 중 if
var = 5
if var >= 3: # 제어문에 의해 수행되는 명령문들은 띄어쓰기로 블럭화한다.
    print('크구나')
    print('참일때 수행')
else:
    print('작다')
    print('거짓일때 수행')
    
print('end if 1')

print()
jumsu = 45
if jumsu >= 90:
    print('우수')
elif jumsu >= 70:
    print('보통')
    print('만세')
else:
    print('저조')
    
print("end if 2")

print()
# jum = int(input('점수 입력:')) # 형변환 int(), str()
jum = 77
if 90 <= jum <= 100: # &&로 식을 하나씩 연결해줄 필요가 없다.
    grade = '와우'
elif 70 <= jum < 90:
    grade = "홈"
else:
    grade = "허걱"
print(grade)
print("end if 3")

print()

names = ['홍길동', '신기해', '이겨라']
if '홍길동' in names:
    print('내 친구')
else:
    print('누구냐')
print("end if 4")

print()
a = 'kbs'
b = 9 if a == 'kbs' else 11 # 조건이 참이면 b가 9 아니면 11
print(b)

a = 11
b = "mbc" if a == 9 else 'kbs' # a가 9이면 b는 mbc 아니면 kbs
print(b)

print()

a = 3
if a > 5:
    result = a * 2
else:
    result = a + 2
print(result)

print()
result = a * 2 if a > 5 else a + 2; print(result) # 참값 조건 거짓값

a = 3
print((a + 2, a * 2)[a > 5]) # []조건이 참 => 1 거짓 => 0 그래서 tuple 의 값을 수행 

# while문

print('\n\nwhile문 =======')
a = 1
while a <= 5:
    print(a, end = ' ') # 공백을주고 옆으로 찍음
    a += 1

print()
i = 1
while i <= 3:
    j = 1
    while j <= 4:
        print('i:' + str(i) + " / j:" + str(j)) # i는 숫자기때문에 형변환
        j = j + 1
    i = i + 1

print('3의 배수의 합')
i = 1; hap = 0
while i <= 100:
    if i % 3 == 0:
        hap += i
    i += 1
print('합은 : ' + str(hap))

print()
colors = ['red', 'green', 'blue']
a = 0
while a < len(colors):
    print(colors[a], end = ' ')
    a += 1

print()

# import time
# sw = input('폭탄 스위치를 누를까요?[y/n]')
# if sw == 'Y' or sw == 'y':
#     count = 5
#     while 1 <= count: # count값이 1이될때까지
#         print('%d초 남았어요'%count)
#         time.sleep(1) # 자바에서 thread.sleep과 같음
#         count -= 1
#     print('폭발!')
# elif sw == 'N' or sw == 'n':
#     print('작업 취소')
# else:
#     print('y 또는 n을 누르세요')

a = 0
while a < 10:
    a += 1
    if a == 5: continue
    if a == 7: break
    print(a)
else: # while에서의 else는 정상수행했을때 수행한다 정상여부 판단이 가능하다.
    print('while 정상 수행')
    
print('while 수행 후 a : %d'%a)

import random
num = random.randint(1, 10)
# print(num)
while 1:
    print('1 ~ 10 사이의 컴이 가진 예상 숫자 입력:')
    guess = input()
    su = int(guess)
    if su == num:
        print('성공!' * 5)
        break
    elif su < num:
        print('더 큰 수 입력')
    elif su > num:
        print('더 작은 수 입력')






