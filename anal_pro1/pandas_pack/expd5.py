# 그룹화 : groupby, pivot, pivot_table
# 피벗테이블 : 데이터 열 중에서 두 개의 열을 사용하여 데이터 테이블의 행렬을 재구성하여 연산
import numpy as np
import pandas as pd

data = {'city':['강남', '강북', '강남', '강북'],
        'year':[2000, 2001, 2002, 2002],
        'pop':[3.3, 2.5, 3.0, 2.0]
        }
df = pd.DataFrame(data)
print(df)
print()
print(df.pivot('city', 'year', 'pop'))
print() # set_index : 기존의 행 index를 제거하고 첫번째 열을 index로 설정해서 작업
print(df.set_index(['city', 'year']).unstack())
print()
print(df.pivot('year', 'city', 'pop'))
print(df.set_index(['year', 'city']).unstack())

print(df['pop'].describe()) # pop의 요약통계량
hap = df.groupby(['city'])
print(hap.sum)
print(df.groupby(['city']).sum()) # 위 두줄과 결과 동일
print(df.groupby(['city', 'year']).mean())
print('\npivot_table() : pivot과 groupby의 중간')
print(df.pivot_table(index=['city']))
print(df.pivot_table(index=['city'], aggfunc=np.mean)) # 위와 동일
print(df.pivot_table(index=['city','year'], aggfunc=np.mean))
print(df.pivot_table(index=['city','year'], aggfunc=[np.mean, np.sum, len])) # aggfunc = 계산함수 여러개 가능
print()
print(df.pivot_table(values=['pop'], index='city'))
print(df.pivot_table(values=['pop'], index='city', aggfunc=len))
print()
print(df.pivot_table(values=['pop'], index=['year'], columns=['city']))
print(df.pivot_table(values=['pop'], index=['year'], columns=['city'], margins=True)) # 행렬의 합 출력
print(df.pivot_table(values=['pop'], index=['year'], columns=['city'], margins=True, fill_value=0))
