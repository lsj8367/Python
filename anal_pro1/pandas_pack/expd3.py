# 산술연산
from pandas import Series, DataFrame
import numpy as np

s1 = Series([1,2,3], index = ['a','b','c'])
s2 = Series([4,5,6,7], index = ['a','b','d','c'])
print(s1 + s2) # index명이 같은 인자끼리 연산, 불일치 시 NaN
print(s1.add(s2)) # 위와 같음
print(s1 * s2) #  - + * /, subtract, multiply, divide 다 똑같음

print()
df1 = DataFrame(np.arange(9.).reshape(3,3), columns = list('kbs'), index = ['서울', '대전', '부산']) # arange(.) 주면 dtype=float
df2 = DataFrame(np.arange(12.).reshape(4,3), columns = list('kbs'), index = ['서울', '대전', '제주', '광주'])
print(df1)
print(df2)
print(df1 + df2)
print(df1.add(df2))
print(df1.add(df2, fill_value = 0))
# sub, mul, div ... 다같음

print()
seri = df1.iloc[0]
print(seri, type(seri)) # type : <class 'pandas.core.series.Series'>
# Series의 색인을 DataFrame에 칼럼에 맞추고 아래 행으로 전파 BroadCasting
print(df1 - seri) # df1 테이블의 각행마다 0, -1, -2 해준값 출력됨

print('~~~' * 10)
# NaN 값 처리
df = DataFrame([[1.4, np.nan],[7, -4.5], [np.NaN, None], [0.5, -1]], columns = ['one','two'])
# np.nan, np.NaN, None 다 NaN으로 입혀진다.
print(df)
print(df.isnull())
print(df.notnull())
print(df.drop(1)) # 1행삭제
print()
print(df.dropna()) # NaN이 들어있는 모든행을 삭제
print(df.dropna(how = 'any')) # 열에 NaN이 하나라도 있으면 그 행 삭제
print(df.dropna(how = 'all')) # 모든열 값이 NaN이어야만 그 행 삭제

print('------------------')
print()
print(df.dropna(axis='columns')) #NaN이 포함된 열이 있는 경우 삭제
print(df.dropna(axis='rows'))# NaN이 포함된 행이 있는경우 삭제
print(df.dropna(subset=['one'])) #특정 칼럼에  NaN이 있는경우 해당 행 삭제
print()
print(df.fillna(0)) # NaN에 fillna() 안 값으로 채우기
#print(df.fillna(method='ffill')

# 기술적 통계와 관련된 연산 메소드
print(df.sum()) # 중간값 mean, max, min, ...
print(df.sum(axis = 0)) # 열단위 합
print(df.sum(axis = 1)) # 행단위 합

print()
print(df.mean(axis = 0)) # 열단위
print(df.mean(axis = 1)) # 행단위
print()
print(df)
print(df.mean(axis = 1, skipna = False))
print(df.mean(axis = 1, skipna = True)) # 특정 행에 모든 값이 NaN일때, NaN으로 표시

print()
print(df.mean(axis = 0, skipna = False))
print(df.mean(axis = 0, skipna = True))

print()
print(df.max()) # 그냥 최대값을 반환
print(df.max(axis=0))

print(df.idxmax()) # 최대값이 있는 인덱스 번호
print(df.idxmax(axis=0))

# 요약 통계량
print(df.describe())
print(df.info())

print()
dfWords = DataFrame({'계절' : ['봄', '여름', '가을', '봄']})
print(dfWords.describe())
print(dfWords.info())

