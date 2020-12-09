# 광고매체를 통한 광고비 증가로 판매량을 예측하기 위한 회귀모델 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf

advdf = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/Advertising.csv", usecols=[1,2,3,4]) # 0번째는 열에서 제외
print(advdf.head(3))
print(advdf.shape)
print(advdf.index, advdf.columns)
print(advdf.info())

# 상관관계 확인
print(advdf.loc[:,['sales', 'tv']].corr()) # 0.782224

# ols() 사용하여 선형회귀 모델 만들어서 운영
# lm = smf.ols(formula = 'sales ~ tv', data = advdf) # 단일 선형회귀
# lmlearn = lm.fit()
# print(lmlearn.summary())
lm = smf.ols(formula = 'sales ~ tv', data = advdf).fit()
print(lm.summary())

# sales와 tv 자료로 시각화
"""
plt.scatter(advdf.tv, advdf.sales) # 영향을 주는게 tv이므로 x값에 tv를 넣어줌
plt.xlabel("tv(in 1000's)")
plt.ylabel("sales(in 1000's)")
x = pd.DataFrame({'tv' : [advdf.tv.min(), advdf.tv.max()]})
y_pred = lm.predict(x)
plt.plot(x, y_pred, c= 'red')
plt.title('Simple linear Regression')
plt.show()
"""
print(lm.summary().tables[1])

# 예측 : predict()
x_new = pd.DataFrame({'tv':[100]})
print('tv광고비에 대한 판매 예측값: ', lm.predict(x_new))

print('---------------')
# ols() 사용하여 다중선형회귀 모델
lm_mul = smf.ols(formula = 'sales ~ tv + radio + newspaper', data = advdf).fit()
print(lm_mul.summary()) #  P>|t| 0.860 newspaper
print(advdf.corr()) # newspaper와 sales의 상관계수 0.228299 이므로 summary에서 0.860이라는 수치가 나오게된다. 

print("\n선형회귀 모델 만족 조건------")
# 1) 잔차의 독립성 확인 : Durbin-Watson 통계량을 사용하여 회귀 모형의 오차에 자기 상관이 있는지 검정할 수 있습니다.
# 자기 상관은 인접 관측치의 오차가 상관되어 있음을 의미합니다.
# Durbin-Watson 방법으로 확인 : 0 ~ 4 까지의 값을 가짐.  0에 근사하면 양의 상관관계, 4에 근사하면 음의 상관관계
# 2에 근사하면 자기상관이 있다. 다시 말해 잔차끼리 상관관계를 가지지 않는다. 
# Durbin-Watson: 2.084 

print()
# 2) 모형의 선형성 확인 : 예측값과 잔차의 비교 (비슷하게 나와야 함)
fitted = lm.predict(advdf) # 예측값
residual = advdf['sales'] - fitted # 잔차
# sns.regplot(fitted, residual, lowess = True, line_kws = {'color':'red'})
# plt.plot([fitted.min(), fitted.max()], [0, 0], '--', color = 'blue')
# plt.show() # 빨간 실선이 파선을 크게 벗어나지 않으므로 선형성 만족

print()
# 2) 잔차의 정규성 확인 : 잔차가 정규분포를 따라야 함
# Q-Q plot으로 확인
import scipy.stats
# sr = scipy.stats.zscore(residual)
# (x, y), _ = scipy.stats.probplot(sr)
# sns.scatterplot(x, y)
# plt.plot([-3, 3], [-3, 3], '--', color = 'grey')
# plt.show()

print()
# 3) 잔차의 등분산성 확인 : 회귀모형을 통해 예측값들 대소에 관계없이 모든 값들에 대해 잔차의 분산이 동일해야한다는 가정
# sns.regplot(fitted, np.sqrt(np.abs(sr)), lowess = True, line_kws = {'color' : 'red'})
# plt.show()

print()
# 4) 잔차의 등분산성 확인 : Cook's distance는 극단값을 나타내는 지표
from statsmodels.stats.outliers_influence import OLSInfluence
cd, _ = OLSInfluence(lm).cooks_distance
print(cd.sort_values(ascending = False).head())
print(advdf.iloc[[35, 178, 25, 175, 131]])

import statsmodels.api as sm
sm.graphics.influence_plot(lm, alpha = 0.05, criterion='cooks')
plt.show()






