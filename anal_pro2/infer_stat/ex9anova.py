# ANOVA : 독립변수(Factor - 여러 개의 Factor level로 구성)는 범주형, 종속변수 : 연속형
# 여러 개의 Factor level(집단)에 대한 평균 차이 검정. 분산분석, 변량분석
# f값 = Between Variable / Within Variable
# 종속변수의 변화 폭이 우연 보다 필연에 위해 발생했는 분석하는 것.
# 집단 간 분산이 집단 내 분산보다 충분히 큰 것인가를 파악.
# 선행 조건 : 독립성, 정규성, 등분산성

# * 서로 독립인 세 집단의 평균 차이 검정
# 실습) 세 가지 교육방법을 적용하여 1개월 동안 교육받은 교육생 80명을 대상으로 실기시험을 실시, three_sample.csv
import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols
data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/three_sample.csv")
print(data.head(5), len(data)) # 80

# 교육방법(독립변수-Factor : 1개, Factor level : 3개 - 범주형), 시험점수에 차이 <- 종속변수: 연속형
# 일원분산분석(one-way ANOVA)
# 귀무 : 세가지 교육방법을 적용하여 시험을 실시한 결과 점수에 차이가 없다.
# 대립 : 세가지 교육방법을 적용하여 시험을 실시한 결과 점수에 차이가 있다.
print(data.describe()) # 요약통계량으로 이상치를 확인함

# 이상치(outlier) 확인을 위해 시각화
import matplotlib.pyplot as plt
#plt.boxplot(data.score)
#plt.hist(data.score)
#plt.show()

data = data.query('score <= 100') # 걸러내기
print(data.describe())
print(len(data)) # 78로 줄었음

# 등분산성 확인 - 만족하면 anova검정, 만족하지 않는다면 - welch_anova검정 실시
result = data[['method','score']]
print(result.head(3))
m1 = result[result['method'] == 1]
m2 = result[result['method'] == 2]
m3 = result[result['method'] == 3]
score1 = m1['score']
score2 = m2['score']
score3 = m3['score']
print("등분산 확인 : ", stats.levene(score1, score2, score3).pvalue) # 등분산성 확인 p-value : 0.11322850654055751 > 0.05 만족
print("등분산 확인 : ", stats.fligner(score1, score2, score3).pvalue)
print("등분산 확인 : ", stats.bartlett(score1, score2, score3).pvalue) # 비모수 검정 + 데이터 적을경우

# 정규성 확인 - 만족하면 anova검정, 만족하지 않는다면 - kruscal-wallis test
# 집단 하나에 검정
print(stats.shapiro(score1))
print(stats.shapiro(score2))
print(stats.shapiro(score3))
# 두 개 검정
print('정규성 확인 :', stats.ks_2samp(score1, score2))
print('정규성 확인 :', stats.ks_2samp(score1, score3))
print('정규성 확인 :', stats.ks_2samp(score2, score3)) # 두개만 만족하고 하나는 안할수도 있는데 그건 문장을 더 첨부하여 부연설명이 필요하다.
# 정규성 만족

print()
# 교차표 : 교육방법별 건수
data2 = pd.crosstab(index = data['method'], columns = 'count')
data2.index = ['방법1', '방법2', '방법3']
print(data2)
# 교차표 : 교육방법별 만족여부
data3 = pd.crosstab(data.method, data.survey)
data3.index = ['방법1', '방법2', '방법3']
data3.columns = ['만족', '불만족']
print(data3)

print("\nANOVA 검정 - linear model을 사용")
import statsmodels.api as sm
#regModel = ols('data["score"] ~ data["method"]', data = data).fit() # 학습시키는것 fit
regModel = ols('data["score"] ~ C(data["method"])', data = data).fit() # 학습시키는것 fit # C() 해당칼럼이 범주형임을 명시적으로 기술하는것.
print(regModel) # RegressionResultsWrapper object

table = sm.stats.anova_lm(regModel, type=1)
print(table) # 유의확률 p : 0.939639 > 0.05 이므로  귀무가설 채택, 세가지 교육방법을 적용하여 시험을 실시한 결과 점수에 차이가 없다.
# 요인     자유도     제곱합     제곱평균    F값
# 회귀        1     SSR    MSR   MSR/MSE
# 잔차      n-2    SSE    MSE
# 합         n-1    SST
# SSR(잔차제곱합) SSE(오차제곱합) SST(총제곱합)

# 참고 : 다중회귀 모델로 ANOVA 검정
"""
regModel2 = ols('data["score"] ~ C(data["method"] + data["survey"])', data = data).fit()
table2 = sm.stats.anova_lm(regModel2, type=2)
print(table2)
"""

# 사후 검정 : ANOVA는 전체에 대한 평균의 차이여부만 알려줌
# 각 그룹 간의 차이를 알고자 한다면 Post Hoc Test를 하게 된다.
from statsmodels.stats.multicomp import pairwise_tukeyhsd

turkeyResult = pairwise_tukeyhsd(data.score, data.method)
print(turkeyResult) 

# 시각화
turkeyResult.plot_simultaneous()
plt.show()
