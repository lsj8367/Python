# mtcars dataset을 이용해 연비 추정 선형회귀모델 작성 후 처리
import statsmodels.api
import numpy as np
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import pandas as pd
plt.rc('font', family = 'malgun gothic')

mtcars = statsmodels.api.datasets.get_rdataset('mtcars').data
print(mtcars.head(2))
#print(mtcars.describe())
print(mtcars.info())
# mpg, hp 두 변수를 사용
print(np.corrcoef(mtcars.hp, mtcars.mpg)) # -0.7761

# 시각화
# plt.scatter(mtcars.hp, mtcars.mpg)
# plt.xlabel('마력수')
# plt.xlabel('연비')
# slope, intercept = np.polyfit(mtcars.hp, mtcars.mpg, 1)
# plt.plot(mtcars.hp, mtcars.hp * slope + intercept, 'b')
# plt.show()

print("\n단일 선형회귀 분석---------------")
result = smf.ols(formula = 'mpg ~ hp', data = mtcars).fit()
print(result.conf_int(alpha = 0.05)) # default 95% confidence interval
print(result.conf_int(alpha = 0.01))
#print(result.summary())
print("결정계수 : ", result.rsquared)
print(result.summary().tables[1])

print("\다중 선형회귀 분석---------------")
result2 = smf.ols(formula = 'mpg ~ hp + wt', data = mtcars).fit() # wt = 차무게
print(result2.summary())

# 추정치 구하기
result3 = smf.ols(formula = 'mpg ~ wt', data=mtcars).fit()
print(result3.summary().tables[1])
print("결정계수 : ", result3.rsquared)

kbs = result3.predict()
#print(kbs)
print("실제 값 : ", mtcars.mpg[0])
print("예측 값 : ", kbs[0])

# 전체자료에 대한 실제값, 예측값
data = {
    'mpg':mtcars.mpg,
    'mpg_predict' : kbs
}
df = pd.DataFrame(data)
print(df)

print('---' * 10)
# 임의의 차체 무게에 대한 연비 확인작업 가능
mtcars.wt = 6 # 차체 무게가 6톤이면 연비는?
ytn = result3.predict(pd.DataFrame(mtcars.wt))
print('차체 무게가 6톤이면 연비는 ', ytn[0])

mtcars.wt = 0.5 # 차체 무게가 500kg이면 연비는?
tvn = result3.predict(pd.DataFrame(mtcars.wt))
print('차체 무게가 500kg이면 연비는 ', tvn[0])

print()
wt_new = pd.DataFrame({'wt':[2, 3.5, 4.2, 0.3]})
mpg_preds = result3.predict(wt_new)
#print('예상 연비:', mpg_preds)
print('예상 연비:', np.round(mpg_preds.values, 3))
