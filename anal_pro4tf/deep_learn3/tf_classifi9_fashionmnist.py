# 패션 MNIST : 70,000개의 흑백이미지 (28 * 28 pixel), 10개의 범주로 분리
# Labels
# Each training and test example is assigned to one of the following labels:
# 0 T-shirt/top, 1 Trouser, 2 Pullover, 3 Dress, 4 Coat, 5 Sandal, 6 Shirt, 7 Sneaker, 8 Bag, 9 Ankle boot 

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
print(train_images.shape, train_labels.shape) # (60000, 28, 28) (60000,)
print(set(train_labels)) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# plt.imshow(train_images[0])
# plt.colorbar()
# plt.show()

# train data 25개 출력 (5 by 5)
# plt.figure(figsize = (10, 10))
# for i in range(25):
#     plt.subplot(5, 5, i + 1)
#     plt.xticks([])
#     plt.yticks([])
#     plt.imshow(train_images[i])
#     plt.xlabel(class_names[train_labels[i]])
#     
# plt.show()

# 이미지 데이터 정규화
train_images = train_images / 255.0
test_images = test_images / 255.0

# model
model = tf.keras.Sequential([
    #tf.keras.layers.Dense(512, input_shape = (784, )),
    tf.keras.layers.Flatten(input_shape=(28, 28)), # Flatten 차원축소
    tf.keras.layers.Dense(128, activation = tf.nn.relu),
    tf.keras.layers.Dense(64, activation = tf.nn.relu),
    tf.keras.layers.Dense(10, activation = tf.nn.softmax)
])
# loss = 'sparse_categorical_crossentropy' 내부적으로 one-hot encoding 해줌
model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

model.fit(train_images, train_labels, batch_size = 128, epochs = 10, verbose=2)
test_loss, test_acc = model.evaluate(test_images, test_labels, batch_size = 128)
print('평가  loss: ', test_loss)
print('평가  acc: ', test_acc)

pred = model.predict(test_images)
#print(pred[0])
print('예측값 : ', np.argmax(pred[0]))
print('실제값 : ', test_labels[0])

# 시각화 : 예측 이미지와 실제 레이블 비교
def plot_image(i, pred_arr, real_label, img):
    pred_arr, real_label, img = pred_arr[i], real_label[i], img[i]
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img, cmap = 'Greys')
    pred_label = np.argmax(pred_arr)
    if pred_label == real_label: # 예측값과 실제값이 같을때
        color = 'blue'
    else:
        color = 'red'\
        
    plt.xlabel('{} {:2.0f}% ({})'.format(class_names[pred_label], 100 * np.max(pred_arr), class_names[real_label]), color = color)
    
i = 1
plot_image(i, pred, test_labels, test_images)
plt.show()
