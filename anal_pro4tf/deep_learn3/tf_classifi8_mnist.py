# MNIST dataset : 손글씨 이미지 분류
import tensorflow as tf
import sys

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
# print(x_test, x_test.shape, ' ', y_train.shape) # (60000, 28, 28)   (10000,)
# print(y_test, y_test.shape) # (10000, )
print(x_train[0])
"""
for i in x_train[0]:
    for j in i:
        sys.stdout.write('%s  '%j)
    sys.stdout.write('\n')
"""
'''
import matplotlib.pyplot as plt
plt.imshow(x_train[0].reshape(28, 28), cmap = 'Greys')
plt.show()
'''
print(y_train[0]) # 5

# 모델에 적용하기 위해
x_train = x_train.reshape(60000, 784).astype('float32') # 28 * 28 배열을 784행으로 바꿈
x_test = x_test.reshape(10000, 784).astype('float32')
print(x_train[0])
print()
x_train /= 255 # 0 ~ 1 정규화
x_test /= 255
print(x_train[0])
print('레이블 종류 : ', set(y_train)) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

print()
print(y_train[0]) # 5
# label 자료에 대해 one-hot encoding
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)
print(y_train[0])

# train data의 일부를 validation data로 분리하기
x_val = x_train[50000:60000]
y_val = y_train[50000:60000]
x_train = x_train[0:50000]
y_train = y_train[0:50000]
print(x_val.shape, x_train.shape)

'''
# model
model = tf.keras.Sequential()

model.add(tf.keras.layers.Dense(512, input_shape = (784, )))
model.add(tf.keras.layers.Activation('relu'))
model.add(tf.keras.layers.Dropout(0.2)) # 과적합 방지를 목적으로 20% 정도는 학습에서 배제  

# L1 regularization : 가중치의 절댓값에 비례하는 비용이 추가됨(가중치의 L1 norm)
# L2 regularization(=weight decay) : 가중치의 제곱에 비례하는 비용이 추가됨(가중치의 L2 norm)
model.add(tf.keras.layers.Dense(512, kernel_regularizer = tf.keras.regularizers.l2(0.001))) # 가중치 규제
model.add(tf.keras.layers.Activation('relu'))
model.add(tf.keras.layers.Dropout(0.2)) 

model.add(tf.keras.layers.Dense(10))
model.add(tf.keras.layers.Activation('softmax'))

model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

print(model.summary())

from tensorflow.keras.callbacks import EarlyStopping
early_stop = EarlyStopping(patience = 5)


history = model.fit(x_train, y_train, epochs = 1000, batch_size = 256, validation_data = (x_val, y_val), verbose = 2, callbacks = [early_stop])

print(history.history.keys())
print('loss : ', history.history['loss'])
print('val_loss : ', history.history['val_loss'])
print('accuracy : ', history.history['accuracy'])
print('val_accuracy : ', history.history['val_accuracy'])

# 시각화
import matplotlib.pyplot as plt
plt.plot(history.history['loss'], label = 'loss')
plt.plot(history.history['val_loss'], label = 'val_loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend()
plt.show()

# 모델 평가
score = model.evaluate(x_test, y_test, batch_size = 128, verbose = 2)
print('evaluate loss : ', score[0])
print('evaluate acc : ', score[1])
'''

# 모델 저장 및 읽기
# model.save('mnist_model.hdf5') # 모델 저장
model = tf.keras.models.load_model('mnist_model.hdf5') # 모델 읽기

# 기존 자료로 예측
import matplotlib.pyplot as plt
print(x_test[:1], x_test[:1].shape)
plt.imshow(x_test[:1].reshape(28, 28), cmap = 'Greys')
plt.show()

import numpy as np
pred = model.predict(x_test[:1])
print('예측값 : ', np.argmax(pred, 1))
print('실제값 : ', np.argmax(y_test[:1])) #  y값이 one-hot encoding 되어있어 가장 큰값이 어디에있냐고 물어야함

# 내가 그린 이미지 분류결과 확인
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open('nice.png')
img = np.array(im.resize((28, 28), Image.ANTIALIAS).convert('L'))
print(img, img.shape)

data = img.reshape([1, 784])
# print(data)
data = data / 255.0
# print(data)

plt.imshow(data.reshape(28, 28), cmap = 'Greys')
plt.show()

new_pred = model.predict(data)
print('분류 예측 결과 : ', np.argmax(new_pred, 1))




