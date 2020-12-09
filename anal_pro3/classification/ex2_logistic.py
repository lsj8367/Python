# Logistic Regression : 날씨 예보 (비가 올까?)
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np
from sklearn.model_selection._split import train_test_split

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/weather.csv")
print(data.head(2), data.shape, data.columns) # (366, 12)
#print(data.info())
data2 = pd.DataFrame()
data2 = data.drop(['Date', 'RainToday'], axis = 1)
data2['RainTomorrow'] = data2['RainTomorrow'].map({'Yes' : 1, 'No' : 0})
print(data2.head(2)) # RainTomorrow : 종속, 나머지 변수 : 독립

# data2를 무작위로 섞어 7:3 비율로 train(모델 학습용), test(모델 검정용) dataset을 생성
train, test = train_test_split(data2, test_size = 0.3, random_state = 42)
print(train.head(3), train.shape) # (256, 10)
print(test.head(3), test.shape)   # (110, 10)

#my_formula = 'RainTomorrow ~ MinTemp + MaxTemp + ...'
col_select = " + ".join(train.columns.difference(['RainTomorrow'])) # RainTomorrow를 제외한나머지 칼럼들만 추출 +로
my_formula = 'RainTomorrow ~ ' + col_select
print(my_formula)
#model = smf.glm(formula = my_formula, data = train, family = sm.families.Binomial()).fit()
model = smf.logit(formula = my_formula, data = train).fit()

print(model.summary())
print(model.params)
print('예측값:', np.rint(model.predict(test)[:3]))
print("실제값:", test.RainTomorrow[:3])

# 정확도
con_mat = model.pred_table() # glm()은 X
print('혼동(혼돈)행렬: \n', con_mat)
print('분류정확도: ', (con_mat[0][0] + con_mat[1][1]) / len(train)) # 0.87109375

from sklearn.metrics import accuracy_score
pred = model.predict(test)
print('분류정확도: ', accuracy_score(test['RainTomorrow'], np.around(pred)))


