# 두 집단의 가설검정 – 실습 시 분산을 알지 못하는 것으로 한정하겠다.
# * 서로 독립인 두 집단의 평균 차이 검정(independent samples t-test)
# 남녀의 성적, A반과 B반의 키, 경기도와 충청도의 소득 따위의 서로 독립인 두 집단에서 얻은 표본을 독립표본(two sample)이라고 한다.
# 실습) 남녀 두 집단 간 파이썬 시험의 평균 차이 검정
from scipy import stats
import pandas as pd
from numpy import average

male = [75, 85, 100, 72, 86]
female = [63, 76, 52, 100, 70]
# t-test를 위한 통계적 질문 : 남녀의 시험 평균이 우연히 같을 확률은 얼마나 될까?
print('mail:', average(male)) # 83.6
print('femail:', average(female)) # 72.2
# 평균이 11.4점 차이가 나는데 이것이 우연히 발생할 확률은 얼마나 되는가?
# 귀무 : 두 집단 간 파이썬 시험의 평균에 차이가 없다.
# 대립 : 두 집단 간 파이썬 시험의 평균에 차이가 있다.
# 선행조건 : 정규성, 등분산성을 만족해야함
#two_sample = stats.ttest_ind(male, female) # 두집단의 가설검정 메소드
two_sample = stats.ttest_ind(male, female, equal_var = True) # 정규분포의 분산은 같다. 가 기본값
print(two_sample) # Ttest_indResult(statistic=1.2118063278722324, pvalue=0.26016072398920453)
# 해석 : pvalue=0.260160723 > 0.05이므로 귀무가설 채택 , 귀무 : 두 집단 간 파이썬 시험의 평균에 차이가 없다.

print("\n----------------------------")
# 실습2) 두가지 교육방법에 따른 평균 시험 점수에 대한 검정 수행 two_sample.csv
data = pd.read_csv("testdata/two_sample.csv")
print(data.head(3))
ms = data[['method', 'score']]
print(ms.head(2))
print(ms.method.unique()) # [1 2] 만 가짐
# 귀무 : 두가지 교육방법에 따른 평균 시험 점수에 차이가 없다.
# 대립 : 두가지 교육방법에 따른 평균 시험 점수에 차이가 있다.

m1 = ms[ms['method'] == 1] # 방법1
m2 = ms[ms['method'] == 2] # 방법2

score1 = m1['score']
score2 = m2['score']

#print(score1)
print()
#print(score2)

# NaN 결측값 확인
print(score1.isnull().sum()) # 0
print(score2.isna().sum()) # 2개존재
# sco1 = score1.fillna(0) # 결측값을 0으로 채운기 또는 dropna()
# sco2 = score2.fillna(0)
sco1 = score1.fillna(score1.mean()) # 결측값 평균으로 채우기
sco2 = score2.fillna(score2.mean())

# 정규성 확인
print('sco1 : ', stats.shapiro(sco1)) # pvalue=0.3679903745651245 > 0.05 : OK
print('sco2 : ', stats.shapiro(sco2)) # pvalue=0.6714189648628235 > 0.05 : OK

# 등분산성 확인 p-value > 0.05
print("levene: ", stats.levene(sco1, sco2))    #pvalue=0.456
print("levene: ", stats.levene(sco1, sco2).pvalue)    #pvalue=0.456
print("fligner: ", stats.fligner(sco1, sco2))  #pvalue=0.44323
print("bartlett: ", stats.bartlett(sco1, sco2))#pvalue=0.26789

print()
result = stats.ttest_ind(sco1, sco2, equal_var = True) # 정규성, 등분산성을 만족
result = stats.ttest_ind(sco1, sco2, equal_var = False) # 정규성 O, 등분산성을 만족 X

# print(stats.wilcoxon(sco1, sco2)) # 정규성 X

print(result) # Ttest_indResult(statistic=-0.18204104173941227, pvalue=0.8569341412171334)
# pvalue = 0.8569 > 0.05 이므로 귀무가설을 채택, 두가지 교육방법에 따른 평균시험 점수에 차이가 없다.
print(average(sco1), ' ', average(sco2)) # 5.199999999999999   5.246666666666667

# 정규성 확인을 위한
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(sco1, kde=False, fit = stats.norm) # 밀도추정 kde 정규분포곡선 fit
plt.show()
