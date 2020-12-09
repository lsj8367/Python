# RI,Na,Mg,Al,Si,K,Ca,Ba,Fe,Type
# 유리 식별 데이터베이스로 여러 가지 특징들에 의해 7가지의 label(Type)로 분리된다.
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier

dframe = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/glass.csv")
#print(dframe.head(3))
dType = dframe.Type
dframe = dframe[dframe.columns.difference(['Type'])] # 표준화 하기위해서 유리 타입은 제거
#print(dType)
#print(dframe.head(3))

data = pd.DataFrame(StandardScaler().fit_transform(dframe), columns = dframe.columns) # 표준화
df = pd.concat([data, dType], axis = 1) # 표준화한것과 제외한 타입을 다시 붙임
print(df.head(3))

x = df[df.columns.difference(['Type'])] # 독립변수
y = df['Type'] # 종속변수
print(x)
print(y)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 123)

# model 생성하기
model = XGBClassifier(booster = 'gbtree')
model.fit(x_train, y_train)

# 예측하기
pred = model.predict(x_test)
print("실제값 :", np.array(y_test[:5]))
print("예측값 : ", pred[:5])
print("분류정확도 : ", accuracy_score(y_test, pred))

# import seaborn as sns
# import matplotlib.pyplot as plt
# cols = df.columns
# sns.pairplot(df[cols])
# plt.show()



