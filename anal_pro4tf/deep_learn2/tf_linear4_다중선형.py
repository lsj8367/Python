# 다중선형회귀 모델 작성 후 TensorBoard라는 시각화툴을 사용
# TensorBoard - 모델의 구조 및 학습 진행 흐름을 시각화 해준다.

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers
import numpy as np
import matplotlib.pyplot as plt

x = np.array([[70, 85, 80], [71, 89, 78], [50, 80, 60], [69, 80, 60], [50, 30, 10]])
y = np.array([73, 82, 72, 65, 34])
print('Sequential Api 사용===================')
model = Sequential()
#model.add(Dense(1, input_dim = 3, activation = 'linear')) # layyer 1개
model.add(Dense(6, input_dim = 3, activation = 'linear', name = 'a')) # layer 3개
model.add(Dense(3, activation = 'linear', name = 'b'))
model.add(Dense(1, activation = 'linear', name = 'c'))
print(model.summary())

opti = optimizers.Adam(lr=0.01)
model.compile(optimizer = opti, loss = 'mse', metrics=['mse'])
history = model.fit(x, y, batch_size=1, epochs = 100, verbose=1)
print(history.history)

'''
plt.plot(history.history['loss'])
plt.xlabel('epochs')
plt.ylabel('loss')
plt.show()
'''

print('predict : ', model.predict(x).flatten())
new_data = np.array([[20, 99, 10], [90, 90, 90], [5, 7, 9]])
print('예상점수 : ', model.predict(new_data).flatten())

print('\nFunction Api 사용============')
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model

inputs = Input(shape = (3, ))
#outputs = Dense(1, activation = 'linear')(inputs)
#linear_model = Model(inputs, outputs)

output1 = Dense(6, activation = 'linear', name = 'a')(inputs) # 레이어 3개인 경우
output2 = Dense(3, activation = 'linear', name = 'b')(output1)
outputs = Dense(1, activation = 'linear', name = 'c')(output2)
linear_model = Model(inputs, outputs)

opti = optimizers.Adam(lr=0.01)
linear_model.compile(optimizer = opti, loss = 'mse', metrics=['mse'])

#************tensorboard 출력 준비*************
from tensorflow.keras.callbacks import TensorBoard
tb = TensorBoard(log_dir = '.\\mylog', histogram_freq = True, write_graph = True) # 현재폴더 하위로 mylog폴더 생성됨
# 실행 방법 : tensorboard --logdir mylog/ << anaconda prompt
#*******************************************

history = linear_model.fit(x, y, batch_size=1, epochs = 100, verbose=0, callbacks = [tb])
print(history.history)

print('predict : ', linear_model.predict(x).flatten())
new_data = np.array([[20, 99, 10], [90, 90, 90], [5, 7, 9]])
print('예상점수 : ', linear_model.predict(new_data).flatten())
