# 단순 선형회귀 분석을 통해 r, 결정계수(r2), p-value, t-value, f-value 등을 이해하기
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/drinking_water.csv")
print(df.head(2))
print(df.corr())

import statsmodels.formula.api as smf
model = smf.ols(formula = '만족도 ~ 적절성', data = df).fit()
print(model.summary())
print()
print("회귀계수 : ", model.params)
print("결정계수 : ", model.rsquared)
print("p값 : ", model.pvalues)
print("실제값 :",df.만족도[0], ', 모델이 예측한 값 :', model.predict()[0]) # 3, 3.7359630488589186

import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family = 'malgun gothic')
plt.scatter(df.적절성, df.만족도)
slope, intercept = np.polyfit(df.적절성, df.만족도, 1) # 1이면 1차식, 2면 2차식 R의 abline
plt.plot(df.적절성, df.적절성 * slope + intercept, 'b')
plt.show()

