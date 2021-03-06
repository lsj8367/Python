# CNN : 이미지의 특징을 뽑아 크기를 줄이고, 이를 일차원 배열로 만들어 완전연결층(여러 층의 Dense)으로 전달해 이미지(텍스트)를 분류
# 분류 정확도가 상당히 높다. 연산량이 많아 시스템의 성능이 좋아야 한다.

# MNIST 손글씨 : 흑백 이미지
import tensorflow as tf
from tensorflow.keras import datasets, layers, models

(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()
print(train_images.shape, type(train_images), train_images.ndim)

# CNN 처리를 위해 3차원 자료를 4차원으로 구조 변경. channel을 추가(흑백:1, 칼라:3)
train_images = train_images.reshape((60000, 28, 28, 1))
print(train_images.shape)
train_images = train_images / 255.0 # 정규화
test_images = test_images.reshape((10000, 28, 28, 1))
test_images = test_images / 255.0 # 정규화
# print(train_images[:1])
# print(train_labels[:1])

print()
# 모델 : Sequential 네트워크 : CNN + Dense(완전연결층)
model = models.Sequential()
# CNN
# Conv(원본이미지를 kernel로 합성곱하여 imagemap을 생성) + Pooling(대표값 얻기로 데이터의 크기를 줄임)
input_shape = (28, 28, 1) # (28, 28, 1) <<<<< 구글 제품인 경우 (1, 28, 28) << 다른회사의 경우 
model.add(layers.Conv2D(64, kernel_size=(3, 3), padding = 'same', activation = 'relu', input_shape = input_shape))
# padding = 'valid' X, padding = 'same' 0으로 채움 - 원본이미지 크기가 유지

model.add(layers.MaxPool2D(pool_size = (2, 2), strides = None)) # strides = None은 pool_size와 같은 크기
model.add(layers.Dropout((0.2)))

model.add(layers.Conv2D(64, kernel_size=(3, 3), padding = 'same', strides = (1, 1), activation = 'relu'))
model.add(layers.MaxPool2D(pool_size = (2, 2))) # pool_size = 2
model.add(layers.Dropout((0.2)))

model.add(layers.Conv2D(64, kernel_size=(3, 3), padding = 'same', strides = (1, 1), activation = 'relu'))
model.add(layers.MaxPool2D(pool_size = (2, 2)))
model.add(layers.Dropout((0.2)))

model.add(layers.Flatten()) # Fully Connected Layer : CNN 최종결과를 1차원 자료로 변경하여 완전연결층(Dense)에 전달

model.add(layers.Dense(64, activation = 'relu'))
model.add(layers.Dropout((0.2)))
model.add(layers.Dense(32, activation = 'relu'))
model.add(layers.Dropout((0.2)))
model.add(layers.Dense(10, activation = 'softmax'))

print(model.summary())

model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

from tensorflow.keras.callbacks import EarlyStopping
early_stop = EarlyStopping(monitor='loss', patience=5)
history = model.fit(train_images, train_labels, batch_size=128, epochs=20, validation_split=0.25, callbacks = [early_stop], verbose = 2)

history = history.history
train_loss, train_acc = model.evaluate(train_images, train_labels, verbose = 2)
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose = 2)

model.save('mnist_cnn.hdf5')
model = tf.keras.models.load_model('mnist_cnn.hdf5')

import numpy as np
# predict
print('예측 값 : ', np.argmax(model.predict(test_images[:1])))
print('예측 값 : ', np.argmax(model.predict(test_images[[0]])))
print('실제 값 : ', test_labels[0])

print('예측 값 : ', np.argmax(model.predict(test_images[[1]])))
print('실제 값 : ', test_labels[1])

# 시각화
import matplotlib.pyplot as plt
import numpy as np
import os

def plot_acc(title = None):
    plt.plot(history['accuracy'])
    plt.plot(history['val_accuracy'])
    if title is not None:
        plt.title(title)
    plt.ylabel('acc')
    plt.xlabel('epochs')
    plt.legend(['train data', 'validation data'], loc = 0)

def plot_loss(title = None):
    plt.plot(history['loss'])
    plt.plot(history['val_loss'])
    if title is not None:
        plt.title(title)
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train data', 'validation data'], loc = 0)
    
plot_acc('accuracy')

plt.show()

plot_loss('loss')
plt.show()
