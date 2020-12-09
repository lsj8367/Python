# 선형회귀 방법 4 - linregress() : 모델 있음

from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# IQ에 따른 시험점수 값 예측
score_iq = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/score_iq.csv")
print(score_iq.head(3))
print(score_iq.info())

x = score_iq.iq # 영향을 주는 변수
y = score_iq.score # 영향을 받는 변수

# 상관관계 확인
print(np.corrcoef(x, y))
print(score_iq.corr())
# plt.scatter(x, y)
# plt.show()

# iq가 score에 영향을 준다고 가정 - 인과관계가 있으므로 회귀분석이 가능
model = stats.linregress(x, y)
print(model)
# x(독립변수)에대한 결과
print('기울기 : ', model.slope)
print('절편 : ', model.intercept)
print('상관계수 : ', model.rvalue)
print('결정계수 : ', model.rvalue ** 2)
print('유의확률(p-value) : ', model.pvalue)
print('표준오차 : ', model.stderr)
# y_hat = model.slope * x + model.intercept
print("점수 예측: ", model.slope * 80 + model.intercept) # iq자리에 임의로 값을 넣어 예측결과를 봄
print("점수 예측: ", model.slope * 157 + model.intercept)

# predict가 없어서 np.polyval() 사용
#print("점수 예측: ", np.polyval([model.slope, model.intercept], np.array(score_iq['iq'])))
newdf = pd.DataFrame({'iq' : [55, 66, 77, 88, 157]}) # 임의의 iq
print("점수 예측: ", np.polyval([model.slope, model.intercept], newdf))
