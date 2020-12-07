'''
집합형 자료 처리  - 문자열, 리스트, 튜플, 셀, 딕트
'''
# 문자열 - str
s = 'sequence'
print(len(s), s.count('e')) # 문자열에서 e의 갯수를 구함
print('검색위치: ', s.find('e'), s.find('e', 3), s.rfind('e')) # find로 맨처음 e가 나오는 자리 찾음
# find안에 찾는위치를 설정해줄수도 있다. rfind는 문자 끝에서부터 찾는다.

# 우측의 객체자료는 수정 불가 - int, float, complex, bool, str, tuple
a = 5 # 5 140732785506208
a = 7 # 7 140732785506272 수정이 된것이아니라 인스턴스의 주소를 바꾼것이다. 5의 주소는 허공에 남아있음
print(a, id(a))

ss = 'mbc'
print(ss, 'mbc', id(ss))
ss = 'abc' # 수정 X 마찬가지로 mbc객체 주소를 참조하다가 abc객체의 주소를 참조함
print(ss, 'mbc', id(ss))

print('\n문자열은 참조만 가능')
print(s) #sequence
print(s[0], s[2:4], s[:3], s[3::2]) # ::는 스텝 1씩증가 3번째부터 2씩 점프해서 출력

print(s[-1], s[-4:-1], s[-4:], s[::2])

print()
s2 = 'kbs mbc'
s2 = ' ' + s2[:4] + 'sbs ' + s2[4:] + ' '
print(s2)

print('문자열 분리---')
s3 = s2.split(sep = ' ') # 자르는 구분자는 공백
print(s3)
print(':'.join(s3)) # 문자열 결합

s4 = 'Life is too short'
s5 = s4.replace('Life', 'My leg') # life를 myleg로 바꿈
print(s5)

# 문자열 함수..

print("\nList 집합 자료형----------------------")
# List : 순서가 있고 중복허용. 여러 종류의 값 기억이 가능. 변경 가능. 배열과 유사
a = [1, 2, 3]
print(a, type(a))
b = [10, a, 20.5, True, '문자열', 10]
print(b, id(b))
print(b[0], ' ', b[1], ' ', b[1][1])

print()
family = ['엄마', '아빠', '나', '여동생']
family.append('남동생') # 배열에 값추가
family.insert(0, '할아버지')
family.extend(['삼촌', '조카'])
family += ['이모', '고모']

family.remove('나')
print(family, ' ',len(family), ' ' , family[2])
print(family.index('남동생')) # 남동생은 몇번째에 있는가
print('엄마' in family, ' ', '나' in family)

print()
aa = [1,2,3, ['a', 'b', 'c', 'd'], 4, 5, 4, 5] # 중첩 리스트
aa[0] = 100
aa[3][0] = 'good'
print(aa, id(aa))
print(aa[0], aa[3]) 
print(aa[3][:2]) 

# 요소 삭제
aa.remove(4) # 값에 의한 삭제
print(aa)
del aa[4] # 순서에 의한 삭제
print(aa)

aa[3].remove('c')
print(aa)
del aa[3][0]
print(aa)

print()
aa = [3, 1, 5, 2, 4]
aa.sort() # ascending sort 가 기본값
aa.sort(reverse = True)
print(aa)
print('얕은 복사  / 깊은 복사')

bb = aa
print()

print()
import copy

cc = copy.deepcopy(aa)
print(cc)
print()

aa[0] = 77
print(bb)
print(cc)
print(id(aa), id(bb), id(cc)) # 2201214185024 2201214185024 2201214187520

print('\nList로stack(LIFO)후입선출 처리')
sbs = [10, 20, 30]
sbs.append(40)
print(sbs)
sbs.pop()
print(sbs)
sbs.pop()
print(sbs)

print('\nList로 queue(FIFO)선입선출 처리')
sbs = [10, 20, 30]
sbs.append(40)
print(sbs)
sbs.pop(0)
print(sbs)
sbs.pop(0)
print(sbs)










