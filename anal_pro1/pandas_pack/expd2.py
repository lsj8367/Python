# pandas 연습 계속
from pandas import Series, DataFrame

# Series의 재색인
data = Series([1, 3, 2], index = (1, 4, 2))
print(data)
data2 = data.reindex((1,2,4))
print(data2)

print()
# Series의 재배치 시 값 채우기
data3 = data2.reindex([0,1,2,3,4,5]) # 대응값이 없는 인덱스는 NaN(결측값)으로 채움
print(data3)

print(data2.reindex([0,1,2,3,4,5], fill_value = 777)) # 결측값을 777로 메꿔줌

print(data2.reindex([0,1,2,3,4,5], method = 'ffill')) # 최초 결측값을 제외하고 나머지를 nan의 앞값으로
print(data2.reindex([0,1,2,3,4,5], method = 'pad')) # 같은의미

print(data2.reindex([0,1,2,3,4,5], method = 'bfill')) # 최초 결측값을 제외하고 나머지를 nan의 뒷값으로
print(data2.reindex([0,1,2,3,4,5], method = 'backfill'))

print('------------------')
import numpy as np
import pandas as pd
df = pd.DataFrame(np.arange(12).reshape(4, 3), index = ['1월', '2월', '3월', '4월'],\
                  columns = ['강남', '강북', '강서'])
print(df)
print(df['강남']) # 그냥 강남에 해당하는 자료
print(df['강남'] > 3) # boolean형식
print(df[df['강남'] > 3]) # 조건이 참인 행 출력
print()
print(df < 3)
df[df < 3] = 0 # 조건이 맞는 값들을 0으로 바꿈
print(df)

print('\nDataFrame 관련 슬라이싱 메소드 - loc(), iloc()')
print(df.loc['3월', :]) # '3월' 행 출력
print(df.loc[:'2월']) # 2월 이하의 행 출력
print(df.loc[:'2월', ['강서']]) # 2월 이하의 행, 강서 열 출력

print()
print(df.iloc[2]) # 2행 출력
print(df.iloc[2, :]) # 상동
print(df.iloc[:2,[2]]) # 2월 이하의 행, 강서 열 출력

print(df.iloc[:3]) # 3행 미만
print(df.iloc[:3, 2]) # 3행 미만의행, 2열출력
print(df.iloc[:3, 1:3]) # 3행 미만의 행, 1~2열 출력