# dataFrame의 모양 관련작업
import numpy as np
import pandas as pd

# 행열 전환, 인덱스 기준 쌓기
df = pd.DataFrame(1000 + np.arange(6).reshape(2, 3), index = ['대전', '서울'], columns = ['2017', '2018', '2019'])
print(df)
print(df.T)  # 행렬 전환
df_row = df.stack() # 인덱스 기준 쌓기
print(df_row)
df_col = df_row.unstack() # 인덱스 기준 쌓기 복원
print(df_col)

print()
# 범주화
price = [10.3, 5.5, 7.8, 3.6]
cut = [3, 7, 9, 11] # 구간 기준값
result_cut = pd.cut(price, cut) # cut(대상, 구간) 기준으로 데이터 자름
print(result_cut) # (3, 7]  (a, b] => a < x <= b
print(pd.value_counts(result_cut)) # 구간으로 자른 갯수 합계

# Series
datas = pd.Series(np.arange(1, 1001))
print(datas.head(3))
print(datas.tail(3))

result_cut2 = pd.qcut(datas, 3) # qcut : 나눌데이터, 나눌 구간수를 뒤에 적어줌
print(result_cut2)
print(pd.value_counts(result_cut2))

print('\n자료 합치기 - DataFrame 병합(Merge)')
df1 = pd.DataFrame({'data1':range(7), 'key':['b','b','a','c','a','a','b']})
print(df1)
df2 = pd.DataFrame({'key':['a','b','d'], 'data2':range(3)})
print(df2)

print()
print(pd.merge(df1, df2, on='key')) # on은 공통칼럼 여기서는 'key'기준으로 병합, inner join과 비슷함
print(pd.merge(df1, df2, on='key', how='inner'))
print()
print(pd.merge(df1, df2, on='key', how='outer')) # int가 float형으로 바뀜, full outer join
print()
print(pd.merge(df1, df2, on='key', how='left')) # int가 float형으로 바뀜, left outer join
print()
print(pd.merge(df1, df2, on='key', how='right')) # int가 float형으로 바뀜, right outer join

print() # 공통 칼럼명이 없는 경우
df3 = pd.DataFrame({'key2':['a','b','d'], 'data2':range(3)})
print(df3)
print(pd.merge(df1, df3, left_on = 'key', right_on= 'key2')) # 공통칼럼이 없는경우 지정해서 inner join 가능 

print()
print(pd.concat([df1, df3])) # 자료 이어 붙이기
print(pd.concat([df1, df3], axis=0)) # 자료 이어 붙이기
print()
print(pd.concat([df1, df3], axis=1)) # 자료 이어 붙이기

# Series도 가능하다
# Numpy의 ndarray는 np.concatenate()