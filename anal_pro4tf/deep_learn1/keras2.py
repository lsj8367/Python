# Keras를 이용해 논리 모델을 생성한 후 분류 결과 확인
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation   # Dense 완전연결체
from tensorflow.keras.optimizers import SGD, Adam, RMSprop

x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0],[0],[0],[1]]) # and 게이트

"""
model = Sequential()
model.add(Dense(5, input_dim = 2))
model.add(Activation('relu'))
model.add(Dense(1))
model.add(Activation('sigmoid')) # 이항분류 이므로 출력층 활성화 함수는 sigmoid 사용
"""

model = Sequential()
model.add(Dense(5, input_dim = 2, activation = 'relu')) # 입력 2 + bias 1 * 출력 5 = Param 15
model.add(Dense(5, input_dim = 2, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid')) # Dense가 두개라서 위에서 출력 5개 내보낸것을 input으로 받아서 1개를 출력한다.

print(model.summary()) # 전체 구조에 대한 parameter
print(model.input)  # 입력 구조
print(model.output) # 출력구조
print(model.weights)  # 가중치(weight), 편향(bias)
print('---------------------')

model.compile(optimizer = Adam(0.01), loss='binary_crossentropy', metrics=['accuracy']) # learning rate = 학습률(lr)

history = model.fit(x, y, epochs = 500, batch_size = 1, verbose = 1)
loss_metrics = model.evaluate(x, y)
print('loss_metrics : ', loss_metrics)

pred = (model.predict(x) > 0.5).astype('int32')
print('pred :', pred.flatten())

print('***' * 10)
print('loss : ', history.history['loss'])
print('accuracy : ', history.history['accuracy']) # accuracy는   compile의 metrics 값과 맞춰준다.

# 시각화
import matplotlib.pyplot as plt
plt.plot(history.history['loss'], label = 'train loss')
plt.xlabel('epochs') # 반복횟수
plt.ylabel('loss') # 손실
plt.legend(loc = 'best') # 컴퓨터가 알아서 주게끔 loc
plt.show()

import pandas as pd
pd.DataFrame(history.history).plot(figsize = (8, 5))
plt.show()
