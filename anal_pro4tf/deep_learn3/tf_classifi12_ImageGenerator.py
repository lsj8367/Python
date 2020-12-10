import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import matplotlib.pyplot as plt
import numpy as np


from tensorflow.python.client import device_lib
device_lib.list_local_devices()

np.random.seed(0)
tf.random.set_seed(3)
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(-1, 28, 28, 1).astype('float32') / 255 # 면개수 -1(auto) 28행28열     1 = 흑백
x_test = x_test.reshape(-1, 28, 28, 1).astype('float32') / 255 # 면개수 -1(auto) 28행28열     1 = 흑백

print(x_train)
y_train = to_categorical(y_train) # one-hot encoding
print(y_train)
y_test = to_categorical(y_test)

# 이미지 보강 : 기존이미지를 상하 좌우회전, 대칭, 확대, 이동시키며 더 많은 이미지를 생산
'''
# 연습
from tensorflow.keras.preprocessing.image import ImageDataGenerator
img_gen = ImageDataGenerator(
    rotation_range = 10, # 회전범위
    zoom_range = 0.1, # 확대/축소
    shear_range = 0.5,
    width_shift_range=0.5, 
    height_shift_range=0.5, # 평행이동
    horizontal_flip = True, #수직이동
    vertical_flip = False
)

augment_size = 100 # 크기
x_augment = img_gen.flow(np.tile(x_train[0].reshape(28 * 28), 100).reshape(-1, 28, 28, 1),
                         np.zeros(augment_size), batch_size = augment_size, shuffle = False).next()[0]
plt.figure(figsize = (10, 10))
for c in range(100):
    plt.subplot(10, 10, c + 1)
    plt.axis('off') # 축 생략
    plt.imshow(x_augment[c].reshape(28, 28), cmap='gray')
plt.show()
'''
from tensorflow.keras.preprocessing.image import ImageDataGenerator

img_generator = ImageDataGenerator(
    rotation_range = 10, # 회전범위
    zoom_range = 0.1, # 확대/축소
    shear_range = 0.5,
    width_shift_range=0.5, 
    height_shift_range=0.5, # 평행이동
    horizontal_flip = True, #수직이동
    vertical_flip = False
)

augment_size = 30000 # 변형된 이미지 3만개 생성
randidx = np.random.randint(x_train.shape[0], size = augment_size)
x_augment = x_train[randidx].copy() # 복사본 생성
y_augment = y_train[randidx].copy()

x_augment = img_generator.flow(x_augment, np.zeros(augment_size), batch_size = augment_size, shuffle = False).next()[0]

# 원래데이터 x_train에 변형된 이미지 3만개를 추가
x_train = np.concatenate((x_train, x_augment)) # 기존 6만개 + 복사본 3만개 
y_train = np.concatenate((y_train, y_augment)) # 기존 6만개 + 복사본 3만개
print(x_train.shape, ' ', y_train.shape)

# plt.figure(figsize = (10, 10))
# for c in range(100):
#     plt.subplot(10, 10, c + 1)
#     plt.axis('off') # 축 생략
#     plt.imshow(x_augment[c].reshape(28, 28), cmap='gray')
# plt.show()

# 신경망 구성
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(filters=32, kernel_size=(3,3), input_shape = (28, 28, 1), padding = 'same', activation = 'relu'),
    tf.keras.layers.MaxPool2D(pool_size = (2, 2)),
    tf.keras.layers.Dropout(rate = 0.3),
    
    tf.keras.layers.Conv2D(filters=64, kernel_size=(3,3), padding = 'same', activation = 'relu'),
    tf.keras.layers.MaxPool2D(pool_size = (2, 2)),
    tf.keras.layers.Dropout(rate = 0.3),
    
    tf.keras.layers.Flatten(),
    
    tf.keras.layers.Dense(units = 128, activation = 'relu'),
    tf.keras.layers.Dropout(rate = 0.3),
    tf.keras.layers.Dense(units = 64, activation = 'relu'),
    tf.keras.layers.Dropout(rate = 0.3),
    tf.keras.layers.Dense(units = 10, activation = 'softmax'),
    
])

model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
print(model.summary())

chkpoint = ModelCheckpoint(filepath='tf12.hdf5', monitor='val_loss', verbose = 2, save_best_only = True)
earlyStop = EarlyStopping(monitor='val_loss', patience = 3)

history = model.fit(x_train, y_train, validation_split = 0.25, epochs = 10, batch_size = 128, verbose = 2, callbacks = [earlyStop, chkpoint])

print('test evaluate : %.4f'%(model.evaluate(x_test, y_test)[1]))

#시각화
plt.figure(figsize = (12, 4))

plt.subplot(1,2,1)
plt.plot(history.history['accuracy'], marker ='o', c='red', label='acc')
plt.plot(history.history['val_accuracy'], marker ='s', c='blue', label='val_acc')
plt.xlabel('epochs')
plt.ylim(0.5, 1)
plt.legend(loc = 'lower right')

plt.subplot(1,2,2)
plt.plot(history.history['loss'], marker ='o', c='red', label='loss')
plt.plot(history.history['val_loss'], marker ='s', c='blue', label='val_loss')
plt.xlabel('epochs')
plt.legend(loc = 'lower right')
plt.show()
