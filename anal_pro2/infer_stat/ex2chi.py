# 가설검정 중 교차분석(Chi2) - 독립변수 : 범주형, 종속변수 : 범주형
# 검정통계량 Chi2 = (관측값 - 기대값) ** 2 의 합 / 기대값

import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/pass_cross.csv', encoding = 'euc-kr')
print(data.head(3)) # 표본추출된 데이터 (복원추출)
print(data.shape) # (50, 4) 행, 열


# 귀무 : 벼락치기 공부는 합격여부와 관련이 없다. # =, 0 
# 대립 : 벼락치기 공부는 합격여부와 관련이 있다.
# 가설검정을 실시 : 공부함 ==> 1, 합격 ==> 1

print(data[(data['공부함'] == 1) & (data['합격'] == 1)].shape[0]) # 공부 + 합격이 1인사람 18명
print(data[(data['공부함'] == 1) & (data['불합격'] == 1)].shape[0]) # 공부 1 + 불합격이 1인사람 7명

print('빈도표-=====')
data2 = pd.crosstab(index = data['공부안함'], columns = data['불합격'], margins = True)
data2.columns = ['합격', '불합격', '행합']
data2.index = ['공부함', '공부안함', '열합']
print(data2)

# 기대도수 = (각 행에 주변값) * (각열의 주변합) / 총합
print(25 * 30 / 50) 
print(25 * 20 / 50) 
#       합격    불합격  행합
# 공부함     15   10   25
# 공부안함  15   10   25
# 열합       30   20   50

chi2 = (18 - 15) ** 2 / 15 + (7 - 10) ** 2 / 10 + (12 - 15) ** 2 / 15 + (13 - 10) ** 2 / 10
print('chi2 : ', chi2)
# 자유도 : (행의갯수 - 1) * (열의 갯수 -1) # 3.0
# df : 1
# 95% 신뢰구간에서 유의수준(a) 0.05
# 카이제곱표를 통해 임계치 얻을수 있음 : 3.84
# 결론 : chi2  < 임계치 이므로 귀무 채택역 내에  존재함, 귀무가설을 채택. 벼락치기 공부는 합격여부와 관련이 없다.

# python이 제공하는 모듈을 사용해서 검정
import scipy.stats as stats
chi, p, ddof, expected = stats.chi2_contingency(data2)
print('chi :', chi, "p-value :", p, "ddof(자유도) : ", ddof)
# 결론 : 유의수준 0.05 < p-value = 0.5578 이므로 귀무가설 채택. 벼락치기 공부는 합격여부와 관련이 없다.

# 목적 : 두 범주형 변수간에 독립성 검정, 적합도 검정, 동질성 검정을 할 때 사용 
