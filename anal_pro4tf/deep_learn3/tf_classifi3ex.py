from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import tensorflow as tf

df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/diabetes.csv', header=None)
print(df.head(5))
print(df.info())
print(df.isna().sum()) # 결측치 없음
print(df.iloc[:, 8].unique()) # [0 1] 이항분류임
data = df.values
x = data[:, 0:8]
y = data[:, -1]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 12)
print(x_train.shape, x_test.shape)
model = Sequential()
model.add(Dense(10, input_dim = 8, activation = 'relu')) # relu, elu, sigmoid
model.add(Dense(8, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid')) # hidden이 아니고 이항분류기 때문에 sigmoid

#opti = tf.keras.optimizers.Adam(0.01)
model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

early_stop = EarlyStopping(monitor='loss', patience=5) # 학습 조기종료
history = model.fit(x_train, y_train, batch_size = 32, epochs=1000, verbose = 1, callbacks = [early_stop])

loss, acc = model.evaluate(x_test, y_test, batch_size = 32, verbose=1)
print("예측정확도 : {}%".format(acc * 100))

pred = model.predict(x_test)
print("실제값 ", y_test[:5])
print("예측 결과 : ", np.where(pred[:5] > 0.5, 1, 0).flatten())

# 시각화
plt.plot(history.history['loss'])
plt.xlabel('loss')
plt.show()


# function api
print('---------------')

from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model
inputs = Input(shape = (7, ))
outputs = Dense(1, activation = 'sigmoid')(inputs)
model2 = Model(inputs, outputs)

model2.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model2.summary())
history2 = model2.fit(x, y, validation_split = 0.3, epochs=10, batch_size=1, verbose=2)

meval = model2.evaluate(x, y)
print(meval)

