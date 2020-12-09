# 선형회귀분석 : 독립변수(연속형)가 종속변수(연속형)에 얼마나 영향을 주는지 알아보기위한 분석방법
# 방법1 : model 없음
import statsmodels.api as sm
from sklearn.datasets import make_regression
import numpy as np

np.random.seed(12)

x, y, coef = make_regression(n_samples = 50, n_features = 1, bias = 100, coef = True) # n_features = 독립변수
print(x)    # 독립변수 2차원 행렬
print(y)    # 종속변수 1차원 배열
print(coef) # 기울기(회귀 계수값)

# y = f(x)   y = wx + b형식    y = coef * x + bias
y_pred = coef * 66 + 100
print('y_pred: ', y_pred)

xx = x
yy = y

print('=================')
# 방법 2 - LinearRegression : model 있는경우
from sklearn.linear_model import LinearRegression
model = LinearRegression()
print(model)
print(xx)
print(yy)
fit_model = model.fit(xx, yy)   # 독립변수와 종속변수로 모형 추정 - 기울기, 절편 등을 얻음
print("기울기 : ", fit_model.coef_)
print("절편 : ", fit_model.intercept_)
# 잔차가 최소가되는 추세선을 갖은 모델이 완성. 이 모델로 새로운 값을 예측
y_new = fit_model.predict(xx[[0]]) # 예측1
print("y_new : ", y_new)
y_new = fit_model.predict([[66]]) # 예측2
print("y_new : ", y_new)

np.random.seed(1)
x_new, _, _ = make_regression(n_samples = 3, n_features = 1, bias = 100, coef = True)
print(x_new)
y_new = fit_model.predict(x_new) # 예측3
print("y_new : ", y_new)

print('---------------')
# 방법3 - ols() : model 있음
import statsmodels.formula.api as smf
import pandas as pd

x1 = xx.flatten() # 차원축소
print(xx.shape, ' ', x1.shape)
y1 = yy
data = np.array([x1, y1])
df = pd.DataFrame(data.T)
df.columns = ['x1', 'y1']
print(df.head(3))

model2 = smf.ols(formula = 'y1 ~ x1', data = df).fit()
print(model2.summary()) # w:89.4743 b:100.0000
print(model2.predict()[0])  # -52.17214291381565

# 새로운 값으로 예측
print(x1[:2]) # dataframe형식으로 했으니까 이쪽도 dataframe형식으로 추출   [-1.70073563 -0.67794537]
x_new2 = pd.DataFrame({'x1' : [-1.7, -0.6, 8, 88, 888]})

print('x_new2 : ', x_new2)
y_new2 = model2.predict(x_new2)
print('y_new2 : ', y_new2)
