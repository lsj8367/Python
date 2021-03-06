# -*- coding: utf-8 -*-
"""tfrnn8로이터뉴스분류.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_bJRcKUgjnLvsWonGvHuME3iHvxWqBE8
"""

# reuter news data : 46개의 카테고리 뉴스기사가 나뉘어져 있다.
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import reuters
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.utils import to_categorical

np.random.seed(3)
tf.random.set_seed(3)

(x_train, y_train), (x_test, y_test) = reuters.load_data(num_words = 1000, test_split = 0.2) # 8 : 2 나누기
print(x_train.shape, y_train.shape)
#print(x_train)

category = np.max(y_train) + 1
print('category 수 : ', category)
print(x_train[0]) # 워드 인덱싱이 되어 있는 상태
print(y_train[0]) # 3

import matplotlib.pyplot as plt
plt.hist([len(s) for s in x_train], bins = 50)
plt.xlabel('length of data')
plt.ylabel('number of data')
plt.show()

# 인덱싱된 단어 확인
word_index = reuters.get_word_index()
print(word_index)

index_to_word = {}
for key, value in word_index.items():
    index_to_word[value] = key
print(index_to_word)
print(index_to_word[1])
print(index_to_word[10996])
print(index_to_word[1000])

print(x_train[0])
print(' '.join([index_to_word[x] for x in x_train[0]]))

# 데이터 전처리
x_train = sequence.pad_sequences(x_train, maxlen=100)
x_test = sequence.pad_sequences(x_test, maxlen=100)
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
print(x_test)
#print(y_test)

# model
model = Sequential()
model.add(Embedding(1000, 100))
model.add(LSTM(100, activation='tanh'))
# from tensorflow.keras.layers import Conv1D, GlobalMaxPooling1D
# model.add(Conv1D(256, kernel_size = 3, padding = 'same', activation = 'relu', strides = 1))
# model.add(GlobalMaxPooling1D())
model.add(Dense(46, activation='softmax'))
print(model.summary())

model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
history = model.fit(x_train, y_train, batch_size = 128, epochs = 30, validation_data = (x_test, y_test), verbose = 2)
print('test accuracy : %.4f'%(model.evaluate(x_test, y_test)[1]))

# 시각화
vloss = history.history['val_loss']
loss = history.history['loss']
x_len = np.arange(len(loss))
plt.plot(x_len, vloss, marker = '.', c = 'red', label = 'validation_loss')
plt.plot(x_len, loss, marker = 's', c = 'blue', label = 'train_loss')
plt.legend()
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()