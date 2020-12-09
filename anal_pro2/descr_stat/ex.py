# 기술통계 : 자료를 정리 및 요약하는 기초적인 통계작업. 추론 통계의 기본자료로 많이 사용됨
# 도수분포표
import pandas as pd

frame = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/ex_studentlist.csv')
print(frame.head(3))
print(frame.shape) # 행렬확인
print(frame.info())
print(frame.describe())

# 평균, 분산, 표준편차, 빈도수, 변수 간의 상관관계...

# bloodtype을 나타내는 변수의 빈도 수 1 : groupby
data1 = frame.groupby(['bloodtype'])['bloodtype'].count()
print(data1) # 빈도수 출력

# bloodtype을 나타내는 변수의 빈도수 2 : crosstable
print("\nOne-way tables----")
data2 = pd.crosstab(index = frame['bloodtype'], columns = 'count')
print(data2)

print('\nTwo-way tables=====')
data3 = pd.crosstab(index = frame['bloodtype'], columns = frame['sex']) # 성별 혈액형별 인원수
print(data3)

print()
data4 = pd.crosstab(index = frame['bloodtype'], columns = frame['sex'], margins = True) # 성별 혈액형별 인원수 + 합계
print(data4)
data4.columns = ['남', '여', '행합']
data4.index = ['A', 'AB', 'B', 'O', '열합']
print(data4)

print()
print(data4 / data4.loc['열합', '행합']) # 행과 열의 비율
print(data4 / data4.loc['열합']) # 열 비율 합

print()
print(data4.div(data4['행합'], axis = 0)) # div는 나누기
print()
print(data4.T / data4['행합'])
