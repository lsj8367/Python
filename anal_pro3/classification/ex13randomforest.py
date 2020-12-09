# RandomForestRegressor : 정량적인 연속형 자료 예측

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import load_boston

boston = load_boston()
print(boston.DESCR)

dfx = pd.DataFrame(boston.data ,columns = boston.feature_names)
dfy = pd.DataFrame(boston.target, columns = ['MEDV']) # 집값
df = pd.concat([dfx, dfy], axis = 1)
print(df.head(3))

# 시각화
'''
cols = ['MEDV', 'RM', 'AGE', 'LSTAT'] # LSTAT 하위계층
sns.pairplot(df[cols])
plt.show() # MEDV와 LSTAT가 강한 음의상관관계를 가진것을 확인
'''

x = df[['LSTAT']].values # 독립변수 2차원
y = df['MEDV'].values # 종속변수 1차원

print(x[0])
print(y[0])

# 실습 1 : DecisionTreeRegressor 사용
# model = DecisionTreeRegressor(max_depth = 3).fit(x, y) # max_depth 가지갯수

# 실습 2 : DecisionTreeRegressor 사용
model = RandomForestRegressor(n_estimators = 100, criterion = 'mse', random_state = 123, n_jobs = 1).fit(x, y) # n_jobs는 cpu갯수   # 정량적인 값이기 때문에  criterion = mse

print('predict : ', model.predict(x)[:5])
r2 = r2_score(y, model.predict(x)) # 결정계수 설명력
print("결정계수(설명력) : ", r2)

print('\ntrain / test 로 분리해서 작업---')
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state=123)
model.fit(x_train, y_train)
print('predict2 : ', model.predict(x_test)[:5])

# 결정계수 확인
trainR2 = r2_score(y_train, model.predict(x_train))
print('학습데이터로 작업한 결정계수 :', trainR2)

testR2 = r2_score(y_test, model.predict(x_test))
print('검정데이터로 작업한 결정계수 :', testR2)

# 독립변수의 수를 늘리면 두 사이의 차이가 줄어들 수 있다.

# 새값으로 집값 예측
import numpy as np
x_new = np.array([[10],[50],[1]]) # 'LSTAT' 새값
print('예상 집값 : ', model.predict(x_new)) # MEDV값 예측





