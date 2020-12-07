'''
집합형 자료 처리 - 튜플, 셀, 딕트
'''
# tuple : 리스트와 유사하나 읽기 전용, 속도 빠름, 순서 O
# t = ('a', 'b', 'c', 'a') # 괄호 안써도 튜플타입
t = 'a', 'b', 'c', 'a'
print(t, type(t), len(t))
print("검색 건수 : ", t.count('a'))
print("검색 위치 : ", t.index('b'))

print()
p = (1, 2, 3)
print(p)
# p[1] = 10 # err : 'tuple' object does not support item assignment
q = list(p) # 형변환 tuple -> list
q[1] = 10
p = tuple(q)
print(p, ' ', p[1:]) # 슬라이싱 가능함

print()
t1 = (10, 20)
a, b = t1
b, a = a, b
t2 = a, b
print(t2)

aa = (1) # 튜플값에 하나만 넣고싶을때 ,를 찍어줘야한다. # <class 'int'> 또한, 데이터가 한개일때는 괄호를 제거해서는 안된다.
bb = (1,) # <class 'tuple'>
print(type(aa),type(bb))

print('***' * 20)
# set : 순서 X, 중복 불가능
a = {1, 2, 3, 1}
print(a, type(a), len(a))
b = {3, 4}
print(a.union(b)) # 합집합
print(a.intersection(b)) # 교집합
print(a - b, a | b, a & b) # 차, 합, 교집합

# print(b[0]) # err : TypeError: 'set' object is not subscriptable

b.add(5) # 요소 추가
print(b)

b.update({6, 7})   # set 가능
b.update([8, 9])   # list 가능
b.update((10, 11)) # tuple 가능
print(b)

b.discard(7) # 값에 의한 삭제
b.remove(6)  # 값에 의한 삭제
b.discard(7) # 값에 의한 삭제 - 해당 값이 없으면 통과
# b.remove(6)  # 값에 의한 삭제 - 해당 값이 없으면 에러
print(b)

c = set()
print(type(c))
c = b
print(c)
c.clear() # 요소값 전체 제거
print(c)

print('형변환------')
print(a)
print(tuple(a))
print(list(a))

li = [1, 2, 3, 1]
s = set(li) # li 중복값 제거
li = list(s)
print(li)

# dict : 사전 자료형, key:value 쌍으로 이루어짐 (json하고 연동하여 사용하기 편함), 순서 X, key 중복 X
mydic = dict(k1=1, k3 = 3.4, k2='abc')
print(mydic, type(mydic), len(mydic))

dic = {'파이썬':'뱀', '자바':'커피', '스프링':'용수철'}
print(dic, type(dic))
print(dic['자바'])
#print(dic['커피']) # KeyError : 조회할 키값을 넣어줘야함
dic['오라클'] = '예언자' # 추가
print(dic)

print(dic.keys()) # keys, values 반환타입 list
print(dic.values())
print('자바' in dic)
print('마리아' in dic)
print(dic.get('자바'))

