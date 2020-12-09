# Pandas 모듈 : 고수준의 자료구조를 지원. Series, DataFrame
from pandas import Series # 인덱싱된 1차원 배열 형태
import numpy as np
obj = Series([3, 7, -5, 4]) #List타입 가능
#obj = Series((3, 7, -5, 4)) # tuple타입 가능
#obj = Series({3, 7, -5, 4}) # TypeError: 'set' type is unordered
print(obj, type(obj)) # 자동으로  인덱스가 부여(명시적)

obj2 = Series([3, 7, -5, 4], index = ['a','b','c','d']) # 색인을 직접 지정
print(obj2)
print(obj2.sum(), np.sum(obj2), 'python 내장함수 :', sum(obj2))
print(obj2.sum(), obj2.mean(), obj2.std()) #내장된 Numpy 함수 그대로 사용

print(obj2.values) # 배열 값을 반환
print(obj2.index) # 행번호(색인명) 반환

print('\n슬라이싱-----------')
print(obj2['a'], ', ', obj2[['a']]) # obj2[['a']] : 인덱스과 값이 같이나옴
print()
print(obj2['a':'c'], '\n' , obj2[['a','b']])
print()
print(obj2[2]) # 인덱스 명을 부여해도 순서번호 사용이 가능
print(obj2[1:4])
print(obj2[[2, 1]])
print(obj2 > 0)
print('a' in obj2)
print('kbs' in obj2)

print('\ndict type으로 Series 객체 생성')
names = {'mouse':5000, 'keyboard':25000, 'monitor':450000} # 키로 데이터를 찾는 dict type 순서가 없음
print(names)
obj3 = Series(names)
print(obj3, ' ', type(obj3)) # 키가 index명으로 들어가게 된다.
obj3.index = ['마우스', '키보드', '모니터']
print(obj3)
print(obj3[0], ' ', obj3['마우스'])

obj3.name = '상품가격' # Series객체에 이름부여
print(obj3)

print('********' * 10)
# DataFrame : 여러개의 Series 객체가 합쳐진 형태. 각 칼럼은 다른 종류의 값을 기억 가능
 
from pandas import DataFrame

df = DataFrame(obj3) # Series 객체를 사용해서 DataFrame 객체를 만듦
print(df, type(df))

# dict type
data = {
    'irum' : ['신기해', '홍길동', '강나루', '공기밥', '김밥'],
    'juso' : ('역삼동','역삼동', '서초동', '신사동', '서초동'),
    'nai' : [22, 25, 32, 28, 22],
    # set type은 불가능함.
}
print(type(data))

print()

frame = DataFrame(data)
print(frame)

print(frame['irum']) # 사전 형식으로 자료 읽기
print(frame.irum) # 속성 형식

print()
print(DataFrame(data, columns = ['juso','irum','nai'])) # 순서 변경후 객체 생성

print() # 새로운 칼럼 추가(NaN), 인덱스명 추가
frame2 = DataFrame(data, columns = ['irum', 'juso', 'nai', 'tel'], index = ['a','b','c','d','e'])
print(frame2)

#frame2['tel'] 도가능
frame2.tel = '111-1111'
print(frame2) 

val = Series(['222-2222','333-3333','444-4444'], index = ['b','c','e'])
frame2['tel'] = val # 모든값이 덮어 씌워지는데 덮어지지 않은 index는 결측값(NaN)이 된다.
print(frame2)

print()
print(frame2.T) # 행열 변환

print()
print(frame2.values, type(frame2.values)) # 반환타입 : <class 'numpy.ndarray'>
print(frame2.values[0, 1]) # 신기해의 주소 0행1열
print(frame2.values[0:2]) # 0~1행

print() # 행/열 삭제
#frame3 = frame2.drop('d') # 행삭제 기본
frame3 = frame2.drop('d', axis=0) # 행삭제니까 axis = 0
frame4 = frame2.drop('tel', axis=1) # 열삭제
print(frame4)

print() # 정렬
print(frame2.sort_index(axis=0)) # 행 기준 오름차순
print(frame2.sort_index(axis=0, ascending=False)) # 행 기준 내림차순

print(frame2.sort_index(axis=1))
print(frame2.sort_index(axis=1, ascending=False)) # 열 기준 - 오름차순

print()
print(frame2.rank(axis = 0))

print()
counts = frame2['juso'].value_counts()
print('주소 건수 :\n', counts)
print()
data = {
    'juso':['강남구 역삼동', '중구 신당동', '강남구 대치동'],
    'inwon':[23,25,15]
}
frame = DataFrame(data)
print(frame, type(frame))
# 문자열 자르기
results = Series([x.split()[0] for x in frame.juso])
results2 = Series((x.split()[1] for x in frame.juso))
print(results, ' ', results.value_counts())
print(results2, ' ', results2.value_counts())







