# [분류분석 문제1]
# 문1] 소득 수준에 따른 외식성향을 나타내고 있다. 주말 저녁에 외식을 하면 1, 외식을 하지 않으면 0으로 처리되었다. 
# 다음 데이터에 대하여 소득수준이 외식에 영향을 미치는지 로지스틱 회귀분석을 실시하라.
# 키보드로 소득수준(양의 정수)을 입력하면 외식 여부 분류 결과 출력하라.
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.model_selection._split import train_test_split

data = pd.read_csv('ex2.csv')
#print(data[data['요일'] == '토'].shape)
data2 = pd.concat([data[data['요일'] == '토'], data[data['요일'] == '일']], ignore_index=True) # 주말만 출력하기
print(data2) # 주말데이터

train, test = train_test_split(data2, test_size = 0.3, random_state = 12)
print(train.head(3), train.shape)
print(test.head(3), test.shape)

formula = '외식유무 ~ 소득수준'
model = smf.logit(formula = formula, data = train).fit()
print(model.summary())
print(model.params)
print('예측값:', np.rint(model.predict(test)[:3]))
print("실제값:", test.외식유무[:3])

from sklearn.metrics import accuracy_score
pred = model.predict(data2)
print('분류정확도: ', accuracy_score(data2['외식유무'], np.around(pred)))

newdf = data2.iloc[:1]
#print(newdf)
a = int(input('소득수준을 입력하세요.'))
newdf = pd.DataFrame({'소득수준' : [a]})
newdata = model.predict(newdf)

if np.around(newdata)[0] == 1:
    print("외식유무 예측  : 외식을 한다.")
else:
    print("외식유무 예측  : 외식을 하지 않는다.")
