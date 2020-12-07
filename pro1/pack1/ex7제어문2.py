# for
# for target in object:
#    statement
#    ...

for i in [1, 2, 3, 4, 5]:
    print(i, end = ' ')
    
print()

# colors = ['r', 'g', 'b'] # list type
# colors = {'r', 'g', 'b'} # set type
colors = ('r', 'g', 'b') # tuple type

for v in colors:
    print(v, end = ' ')
    
print()
soft = {'java':'웹용언어', 'python':'만능언어', 'mysql':'db처리'}
for i in soft.items():
    #print(i) # 반환값  tuple
    print(i[0] + ' ' + i[1])

print()

for k, v in soft.items():
    print(k, ", ", v)
    
print()

for k in soft.keys():
    print(k, end = " ")

print()

for v in soft.values():
    print(v, end = " ")
    
print('------------------------')

for gu in [2, 3]:
    print('----{}단---'.format(gu))
    for i in [1,2,3,4,5,6,7,8,9]:
        print('{} * {} = {}'.format(gu, i, gu * i))

print()
# for 사용 시 요소값 뿐만 아니라 인덱스도 얻고 싶은경우
li = ['a', 'b', 'c']
for i, v in enumerate(li):
    print(i, v) #인덱스와 밸류값

print()

datas = [1, 2, 3, 4, 5]
for i in datas:
    if i == 3:
        #continue
        break
    print(i, end = " ")
else:
    print("반복문 정상 수행시 처리됨")

print()

# 한명이 5회 시험을 본다고 할 때 70점 이상일 경우만 합격처리
jumsu = [95, 70, 60, 68, 100]
number = 0
for jum in jumsu:
    number += 1
    if jum < 70:continue
    print('%d 번째 합격함'%number)

print()
l1 = [3, 4, 5]
l2 = [0.5, 1, 2]
for a in l1:
    for b in l2:
        print(a + b, end = " ")
    print()
result = [a + b for a in l1 for b in l2]
print(result)
for d in result:
    print(d, end = " " )
print('\n자료 검색 후 문자열 자르기헤서 분리된 문자열 수 출력')

import re
ss = """
미중갈등 속에 시진핑 중국 국가주석이 오는 25일 중국의 6.25참전 70주년을 맞아 미국에 맞서 북한을 도왔다는 뜻의 '항미원조'를 부각시키고 있는 가운데 북한 김정은 국무위원장이 평남 회창군의 중국인민지원군 열사능원을 참배했다.
김 위원장은 특히 마오쩌둥 전 주석의 장남으로 6·25 전쟁에서 전사한 마오안잉의 묘를 찾아 자신 명의의 꽃바구니를 올렸다.
북한 노동당기관지 노동신문은 22일 "김정은 동지께서 중국 인민지원군 조선전선 참전 70돌에 즈음해 평안남도 회창군에 있는 중국인민지원군 열사능원을 찾고 열사들에게 숭고한 경의를 표했다"고 보도했다.
김 위원장은 이 자리에서 "극히 곤난한 형편에서도 항미원조 보가위국의 기치 밑에 우리를 희생적으로 지지성원한 중국인민지원군의 불멸의 공적과 영웅적 위훈은 우리 인민의 기억 속에 생생히 남아있다"고 말했다.
김 위원장은 "중국인민지원군의 조선전선 참전은 조국해방전쟁의 승리에 역사적 기여를 했다"면서, "조중(북중) 두 나라 군대와 인민이 자기 운명을 하나로 연결시키고 생사고락을 같이하면서 피로써 쟁취한 위대한 승리는 세월이 흐르고 세기가 바뀐 오늘에 와서도 변함없이 실로 거대한 의의를 가진다"고 강조했다.
한국 중국 일본 한국 중국인민지원군
"""
ss2 = re.sub(r'[^가-힣\s]', '',ss) # 한글, 공백 이외의 자료는 제거
print(ss2)

print()
ss3 = ss2.split(' ') # 공백을 구분자로 문자열 분리
print(ss3)

cou = {} # 단어의 발생횟수용 dict타입 선언 
for i in ss3:
    if i in cou:
        cou[i] += 1
    else:
        cou[i] = 1
print(cou)

print()
for test_str in ['111-1234', '일일일-일이삼사','222-1234', '2222-1234']:
    if re.match(r'^\d{3}-\d{4}$', test_str):
        print(test_str, "전화번호 맞음")
    else:
        print(test_str, '아님')

print("사전형 자료 -------")
from time import localtime
print(localtime())
act = {6:'잠', 9:'아침먹고 출발', 18:'공부', 24:'휴식'}
print(act)
hour = localtime().tm_hour
print('현재시간:', hour)
print(sorted(act.keys()))

for act_time in sorted(act.keys()):
    if hour < act_time:
        print(act[act_time])
        break
    else:
        print('넌 뭐니')
        
print("사전형 자료 - 과일 값 계산")
price = {'사과':1000, '감':500, '배':'3000'}
guest = {'사과':5, '감':2} # 고객 구매 목록
bill = sum(price[f] * guest[f] for f in guest)
print('고객이 구매한 과일 가격 총액:{}원'.format(bill))

print()
datas = [1, 2, 'a', True, 3.4]
li = [i * i for i in datas if type(i) == int]
print(li)

print()
datas = {1,1,2,2,3} # set type이라서 중복이 제거
se = {i * i for i in datas}
print(se)

print()
id_name = {1:'tom', 2:'james'}
name_id = {val:key for key, val in id_name.items()}
print(name_id)

print()
temp = [1, 2, 3, 1, 2, 3]
for i in temp:
    print(i, end = " ")
print()
print([i for i in temp]) # 중복 포함출력
print({i for i in temp}) # 똑같은거 여러번 넣어도 중복은 제거

print()

temp2 = list()
print(type(temp2))
for i in temp:
    temp2.append(i + 100)
print(temp2)

temp2 = [i + 100 for i in temp]
print(temp2)

print()
aa = [(1,2),(3,4),(5,6)]
for a, b, in aa:
    print(a + b, end = " ")

print('\n ----range() 함수와  함께하기---')
print(list(range(1,6)))
print(list(range(0,11,3)))
print(list(range(-10,-101,-30)))
print(set(range(1,6)))
print(tuple(range(1,6)))

print()
for i in range(6):
    print(i, end = " ")
print()

tot = 0
for i in range(1, 11):
    tot += i
print('합은' + str(tot))

print()
for i in range(2, 5):
    for j in range(1, 10):
        print('{0}*{1}={2}'.format(i, j, i * j), end = ' ')
    print()
print()

# 주사위를 두번 던져서 나온 숫자들의 합이 4의 배수가 되는 경우만 출력

for i in range(1, 7):
    a = i # 주사위 1
    for j in range(1, 7):
        b = j # 주사위 2
        hap = a + b
        if(hap % 4 == 0):
            print(a, b)
        
print()

# n-gram : 문자열에서 n개의 연속된 일부문자를 추출하는 방법
sss = 'hello'

for i in range(len(sss) - 1): # 2-gram
    print(sss[i], sss[i + 1], sep ='')
print()

for i in range(len(sss) - 2): # 2-gram
    print(sss[i], sss[i + 1], sss[i + 2], sep ='')













