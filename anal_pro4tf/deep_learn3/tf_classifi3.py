# 와인 분류(Red, White)
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import tensorflow as tf

wdf = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/wine.csv', header = None)
print(wdf.head(5))
print(wdf.info())
print(wdf.iloc[:, 12].unique())   # 이항분류 [1 0]

dataset = wdf.values
x = dataset[:, 0:12] # feature
y = dataset[:, -1] # label
print(x)
print(y)

# 과적합 방지 목적
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 12)
print(x_train.shape, x_test.shape, y_train.shape) # (4547, 12) (1950, 12) (4547,)

# 모델 설정
model = Sequential()
model.add(Dense(30, input_dim = 12, activation = 'relu')) # relu, elu, sigmoid
#model.add(tf.keras.layers.BatchNormalization()) # 배치 정규화 - Gradient loss 등의 문제 해결
model.add(Dense(15, activation = 'relu'))
model.add(Dense(8, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid')) # hidden이 아니고 이항분류기 때문에 sigmoid

model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# fit() 이전의 훈련되지 않은 모델 평가도 가능
loss, acc = model.evaluate(x_train, y_train, batch_size = 32, verbose = 2)
print('훈련되지 않은 모델 평가 : {:5.2f}%'.format(100 * acc)) # 75.43%

# 모델 실행 및 저장
# 학습 시 모델 저장 폴더 설정
MODEL_DIR = './winemodel/'
if not os.path.exists(MODEL_DIR):
    os.makedirs(MODEL_DIR) # 없는경우엔 폴더를 만듦

# 학습 시 모니터링의 결과를 파일로 저장 가능
chkpoint = ModelCheckpoint(filepath = './winemodel/wine.hdf5', monitor = 'loss', verbose=2, save_best_only = True)

# loss값이 좋아진 구간마다 파일로 저장
# modelpath = "./winemodel/{epoch:02d}-{loss:4f}.hdf5"
# chkpoint = ModelCheckpoint(filepath = modelpath, monitor = 'loss', verbose=2, save_best_only = True)

# 학습 조기 종료 : loss나 accuracy 더 이상 변화가 없을 경우
early_stop = EarlyStopping(monitor='loss', patience=5)

history = model.fit(x_train, y_train, validation_split = 0.3, batch_size = 64, epochs=1000, verbose=2, callbacks = [early_stop, chkpoint])
# validation_data = 이미 구분해놓은 데이터를 사용, validation_split은 앞의 넣은 변수들에 대해서 잘라주는것

# model.load_weights(filepath='./winemodel/wine.hdf5') # 최적의 모델을 저장한 파일 불러옴
loss, acc = model.evaluate(x_test, y_test, batch_size = 64, verbose=2)
print("훈련된 모델의 평가 : {:5.2f}%".format(100 * acc))

print('\nhistory : ', history.history)

vloss = history.history['val_loss']
print('vloss : ', vloss, len(vloss))
loss = history.history['loss']
print('loss : ', loss, len(loss))

acc = history.history['accuracy']
print('acc : ', acc)
acc = history.history['accuracy']

# 시각화
epoch_len = np.arange(len(acc))
plt.plot(epoch_len, loss)
plt.xlabel('epochs')
plt.ylabel('loss')
plt.show()

epoch_len = np.arange(len(acc))
plt.plot(epoch_len, acc)
plt.xlabel('epochs')
plt.ylabel('acc')
plt.show()

print()
# 예측
np.set_printoptions(suppress = True)
new_data = x_test[:5, :]
print(new_data)

pred = model.predict(new_data)
print('pred : ', np.where(pred > 0.5, 1, 0).flatten())
