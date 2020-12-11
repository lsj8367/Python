#from tensorflow.python.client import device_lib
#print(device_lib.list_local_devices())
#class : airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck

from tensorflow.keras.datasets import cifar10
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Input, Flatten, Dense, Conv2D, MaxPool2D
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from tensorflow.python.keras.engine import input_layer
import numpy as np

NUM_CLASSES = 10
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
print(x_train.shape, type(x_train)) # (50000, 32, 32, 3) <class 'numpy.ndarray'>
print(x_test.shape, type(x_test)) # (10000, 32, 32, 3) <class 'numpy.ndarray'>
print(y_train.shape, type(y_train)) # (50000, 1) <class 'numpy.ndarray'>

print()
# print(x_train[0])
# print(y_train[0])

plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.imshow(x_train[0], interpolation = 'bicubic')
plt.subplot(132)
plt.imshow(x_train[1], interpolation = 'bicubic')
plt.subplot(133)
plt.imshow(x_train[2], interpolation = 'bicubic')
plt.show()

x_train = x_train.astype('float32') / 255.0 # 정규화
x_test = x_test.astype('float32') / 255.0
y_train = to_categorical(y_train, NUM_CLASSES)
y_test = to_categorical(y_test, NUM_CLASSES)
print(x_train[55,22,13,2]) # 0.30980393 0:R, 1:G, 2:B

# 모델구조 : Sequential API 사용
'''
model = Sequential([
    Dense(128, activation = 'relu', input_shape = (32, 32, 3)),
    Flatten(),
    Dense(64, activation = 'relu'),
    Dense(NUM_CLASSES, activation = 'softmax')
])

print(model.summary())
'''
# 모델구조 2: function API 사용
input_layer = Input((32,32,3)) # Input(shape=(32,32,3))
x = Flatten()(input_layer)
x = Dense(512, activation = 'relu')(x)
x = Dense(128, activation = 'relu')(x)
output_layer = Dense(NUM_CLASSES, activation = 'softmax')(x)

model = Model(input_layer, output_layer)
print(model.summary())

opt = Adam(lr = 0.01)
model.compile(optimizer = opt, loss = 'categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, batch_size = 128, epochs = 10, shuffle=True, verbose=2)

print('test acc : %.3f'%(model.evaluate(x_test, y_test, verbose = 0, batch_size = 128)[1]))
print('test loss : %.3f'%(model.evaluate(x_test, y_test, verbose = 0)[0]))

CLASSES = np.array(['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck'])

pred = model.predict(x_test[:10])
pred_data = CLASSES[np.argmax(pred, axis = -1)]
actual_data = CLASSES[np.argmax(y_test[:10], axis = -1)]
print("예측값 : ", pred_data)
print("실제값 : ", actual_data)
print("분류 실패 수 : ", (pred_data != actual_data).sum())

# 시각화
fig = plt.figure(figsize=(15, 3))
fig.subplots_adjust(hspace = 0.4, wspace = 0.5)

for i, idx in enumerate(range(len(x_test[:10]))):
    img = x_test[idx]
    ax = fig.add_subplot(1, len(x_test[:10]), i + 1)
    ax.axis('off')
    ax.text(0.5, -0.35, 'pred=' + str(pred_data[idx]), fontsize = 10, ha = 'center', transform = ax.transAxes) # ha정렬방식
    ax.text(0.5, -0.7, 'actu=' + str(actual_data[idx]), fontsize = 10, ha = 'center', transform = ax.transAxes)
    ax.imshow(img)
plt.show()

# CNN Layer 추가
from tensorflow.keras.layers import Activation, Dropout, BatchNormalization, LeakyReLU

# 모델구조 2-1 : function API 사용 CNN + Dense
'''
input_layer = Input((32, 32, 3))
conv_layer1 = Conv2D(filters = 10, kernel_size=(4, 4), strides = 2, padding = 'same')(input_layer)
conv_layer2 = Conv2D(filters = 20, kernel_size=(3, 3), strides = 2, padding = 'same')(conv_layer1)

flatten_layer = Flatten()(conv_layer2)
output_layer = Dense(units=10, activation = 'softmax')(flatten_layer)
model = Model(input_layer, output_layer)
print(model.summary())
'''

input_layer = Input((32, 32, 3))

x = Conv2D(filters = 32, kernel_size=3, strides = 1, padding = 'same')(input_layer)
x = MaxPool2D((2,2))(x)
x = BatchNormalization()(x)
x = LeakyReLU()(x)

x = Conv2D(filters = 32, kernel_size=3, strides = 2, padding = 'same')(x)
x = MaxPool2D((2,2))(x)
x = BatchNormalization()(x)
x = LeakyReLU()(x)

x = Conv2D(filters = 64, kernel_size=3, strides = 1, padding = 'same')(x)
x = MaxPool2D((2,2))(x)
x = BatchNormalization()(x)
x = LeakyReLU()(x)

x = Conv2D(filters = 64, kernel_size=3, strides = 2, padding = 'same')(x)
x = MaxPool2D((2,2))(x)
x = BatchNormalization()(x)
x = LeakyReLU()(x)

x = Flatten()(x) # 1차원으로 축소

x = Dense(128)(x)
x = BatchNormalization()(x)
x = LeakyReLU()(x)
x = Dropout(rate = 0.3)(x)

x = Dense(NUM_CLASSES)(x)
output_layer = Activation('softmax')(x)

model = Model(input_layer, output_layer)

opt = Adam(lr = 0.01)
model.compile(optimizer = opt, loss = 'categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, batch_size = 128, epochs = 10, shuffle=True, verbose=2)

print('test acc : %.3f'%(model.evaluate(x_test, y_test, verbose = 0, batch_size = 128)[1]))
print('test loss : %.3f'%(model.evaluate(x_test, y_test, verbose = 0)[0]))

CLASSES = np.array(['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck'])

pred = model.predict(x_test[:10])
pred_data = CLASSES[np.argmax(pred, axis = -1)]
actual_data = CLASSES[np.argmax(y_test[:10], axis = -1)]
print("예측값 : ", pred_data)
print("실제값 : ", actual_data)
print("분류 실패 수 : ", (pred_data != actual_data).sum())

# 시각화
fig = plt.figure(figsize=(15, 3))
fig.subplots_adjust(hspace = 0.4, wspace = 0.5)

for i, idx in enumerate(range(len(x_test[:10]))):
    img = x_test[idx]
    ax = fig.add_subplot(1, len(x_test[:10]), i + 1)
    ax.axis('off')
    ax.text(0.5, -0.35, 'pred=' + str(pred_data[idx]), fontsize = 10, ha = 'center', transform = ax.transAxes) # ha정렬방식
    ax.text(0.5, -0.7, 'actu=' + str(actual_data[idx]), fontsize = 10, ha = 'center', transform = ax.transAxes)
    ax.imshow(img)
plt.show()
