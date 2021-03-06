# 데이터 간 단위의 차이가 클 경우 정규화 / 표준화

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import SGD, Adam
from sklearn.preprocessing import MinMaxScaler, minmax_scale, StandardScaler, RobustScaler
# MinMaxScaler => 정규화 (요소값 - 최소값) / (최대값 - 최소값)
# StandardScaler : 표준화 (요소값 - 평균) / 표준편차
# RobustScaler : 중앙값과 IQR을 사용. 이상치의 영향을 최소화 시키고자 할 때 유용함
import pandas as pd
import numpy as np

np.random.seed(123)

data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/Advertising.csv')
print(data.head(2))
del data['no'] # no칼럼 삭제
print(data.head(2))

"""
# scaling : 정규화 1
scaler = MinMaxScaler(feature_range=(0, 1))
#scaler = MinMaxScaler()
xy = scaler.fit_transform(data)
print(xy[:2])
abc = scaler.inverse_transform(xy)
print(abc[:2])
"""
xy = minmax_scale(data, axis = 0, copy = True) # 원본데이터를 보존하고 싶다면 axis = 0, copy = True
print(xy[:2])

# train / test 로 분리 : 과적합 방지 - 편향된 분리 X, 시계열 데이터인 경우에는 shuff 하면 안됨, 중복 데이터는 X
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(xy[:, 0:-1], xy[:, -1])
print(x_train[:2], x_train.shape) # tv radio newspaper (140, 3)
print(x_test[:2], x_test.shape) # sales (60, 3)
print(y_train[:2], y_train.shape) # sales (140,)

model = Sequential()
# model.add(Dense(1, input_dim = 3))
# model.add(Activation('linear'))

model.add(Dense(1, input_dim = 3))
model.add(Activation('linear'))
model.add(Dense(20))
model.add(Activation('linear'))
model.add(Dense(10))
model.add(Activation('linear'))
model.add(Dense(1))
model.add(Activation('linear'))

print(model.summary())
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

import tensorflow as tf
tf.keras.utils.plot_model(model, 'abc.png')

model.compile(optimizer = Adam(lr = 0.001), loss = 'mse', metrics = ['mse'])
model.fit(x_train, y_train, epochs=100, batch_size = 64, verbose=1, validation_split=0.3) # validation_split=0.3 train data의 30%를 학습시 검정데이터로 사용 

loss = model.evaluate(x_test, y_test) # 모델 평가는 test dataset을 사용
print('loss : ', loss)

from sklearn.metrics import r2_score
print('설명력 : ', r2_score(y_test, model.predict(x_test)))

pred = model.predict(x_test)
print('실제값 : ', y_test[:3], ', 예측값 : ', pred[:3])
