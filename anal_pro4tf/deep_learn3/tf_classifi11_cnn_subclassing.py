# CNN : 이미지의 특징을 뽑아 크기를 줄이고, 이를 일차원 배열로 만들어 완전연결층(여러 층의 Dense)으로 전달해 이미지(텍스트)를 분류
# Keras를 이용한 레이어 구성 : Subclassing API 사용
import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPool2D, Dropout
from tensorflow.keras import Model, datasets

#=========================================================
# Data를 골고루 섞어주기 위해 tf.data.Dataset.from_tensor_slices 연습
import numpy as np
x = np.random.sample((5, 2))
print(x)
# dset = tf.data.Dataset.from_tensor_slices(x) # 입력 파이프라인 사용가능한 객체 생성
# print('dset : ', dset)
dset = tf.data.Dataset.from_tensor_slices(x).shuffle(10000).batch(5) # batch로 묶음꾸러미 생성
print(dset)
for a in dset:
    print(a)




#=========================================================
print()
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()
print(train_images.shape, type(train_images), train_images.ndim)

# CNN 처리를 위해 3차원 자료를 4차원으로 구조 변경. channel을 추가(흑백:1, 칼라:3)
train_images = train_images.reshape((60000, 28, 28, 1))
print(train_images.shape)
train_images = train_images / 255.0 # 정규화
test_images = test_images.reshape((10000, 28, 28, 1))
test_images = test_images / 255.0 # 정규화

# train dataset 섞어주기
train_ds = tf.data.Dataset.from_tensor_slices((train_images, train_labels)).shuffle(60000).batch(28)
test_ds = tf.data.Dataset.from_tensor_slices((test_images, test_labels)).batch(28)
print(train_ds)
print(test_ds)