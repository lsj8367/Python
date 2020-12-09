# agg() : 함수를 수행하는 함수,  apply()
import pandas as pd
import matplotlib.pyplot as plt

tips = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/tips.csv")
print(tips.info())
print(tips.head(5))

#tips.rename(columns={"sex":"gender"}, inplace = True)
tips['gender'] = tips['sex']
del tips['sex']
print(tips.head(5))

# 그룹별 작업 : 성별, 흡연자별 그룹화
tip_pct_group = tips['tip'].groupby([tips['gender'],tips['smoker']])
print(tip_pct_group)
print(tip_pct_group.sum())
print(tip_pct_group.mean())
print(tip_pct_group.min())

result = tip_pct_group.describe() # 요약통계량
print(result)

# agg
print(tip_pct_group.agg('sum'))
print(tip_pct_group.agg('mean'))
print(tip_pct_group.agg('min'))
print(tip_pct_group.agg('var'))

# 사용자 정의 함수
def diffFunc(group):
    diff = group.max() - group.min()
    return diff

result2 = tip_pct_group.agg(['sum', 'mean', 'max', 'var', diffFunc]) # 내장함수는 따옴표 붙여서 호출하지만, 사용자 정의함수는 따옴표 X
print(result2, type(result2))

result2.plot(kind = 'barh', title = 'agg result', stacked = True) # 누적막대그래프 stacked
plt.show()

print()

# apply()

print(tip_pct_group.agg('sum')) # 부르고
print()
print(tip_pct_group.apply(sum)) # 부르지않다가 그래프 닫으면 출력
print()
print(tip_pct_group.apply(diffFunc))
