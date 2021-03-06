# -*- coding: utf-8 -*-
"""tf13GAN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xAtviywjodHGgHFobi-MqzhXT4a6QI_5
"""

# GAN(생성적 적대 신경망)
# DCGAN(Deep Convolutinal GAN)

# GAN(생성적 적대 신경망)
# DCGAN(Deep Convolutional GAN)
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Input, Dense, Flatten, Dropout, Reshape, BatchNormalization, Activation, LeakyReLU, UpSampling2D, Conv2D
from tensorflow.keras.models import Sequential,Model
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

import os

if not os.path.exists("./ganimages"):
  os.makedirs("./ganimages")

np.random.seed(3)
tf.random.set_seed(3)

generator = Sequential()

# 가짜 이미지 생성자
generator.add(Dense(128 * 7 * 7, input_dim = 100, activation = LeakyReLU(0.2)))
generator.add(BatchNormalization()) # 안정적 학습유도
generator.add(Reshape((7, 7, 128)))
generator.add(UpSampling2D()) # 2배 차원 확대
generator.add(Conv2D(64, kernel_size = 5, padding = 'same'))
generator.add(BatchNormalization())
generator.add(Activation(LeakyReLU(0.2)))
generator.add(UpSampling2D())
generator.add(Conv2D(1, kernel_size=5, padding = 'same', activation = 'tanh'))
generator.summary()

# 가짜 이미지 판별자
discriminator = Sequential()
discriminator.add(Conv2D(64, kernel_size=5, strides=2, input_shape=(28, 28, 1), padding = 'same')) # strides 를 1주면 차원이 줄어들지 않음. 2라면 차원이 줄어들게됨
discriminator.add(Activation(LeakyReLU(0.2)))
discriminator.add(Conv2D(128, kernel_size = 5, strides = 2, input_shape=(28, 28, 1), padding = 'same'))
discriminator.add(Activation(LeakyReLU(0.2)))
discriminator.add(Flatten())
discriminator.add(Dense(1, activation = 'sigmoid'))
discriminator.summary()

discriminator.compile(loss = 'binary_crossentropy', optimizer = 'adam')

discriminator.trainable = False # 판별자는 진품/가품 구분만 필요하므로 학습기능을 꺼줌.

print("***" * 20)
print()
# 생성자와 판별자를 연결시키는 GAN 모델을 생성
ginput = Input(shape = (100, ))
dis_output = discriminator(generator(ginput))
gan = Model(ginput, dis_output)
gan.compile(loss = 'binary_crossentropy', optimizer = 'adam')
gan.summary()

# 신경망을 실행시키는 함수를 만든다.
def gan_train(epoch, batch_size, saving_interval):
    (X_train, _), (_, _) = mnist.load_data()  # MNIST 데이터 불러오기
    # 앞서 불러온 적 있는 MNIST를 다시 이용. 
    # 단, 테스트과정은 필요없고 이미지만 사용할 것이기 때문에 X_train만 불러왔다.
    X_train = X_train.reshape(X_train.shape[0], 28, 28, 1).astype('float32')
    X_train = (X_train - 127.5) / 127.5  
    print('X_train : -----------------', X_train)   
    # 픽셀값은 0에서 255사이의 값이다. 이전에 255로 나누어 줄때는 이를 0~1사이의 값으로 바꾸었던 것인데, 여기서는 127.5를 빼준 뒤 127.5로 나누어 줌으로 인해 -1에서 1사이의 값으로 바뀌게 된다.
    #X_train.shape, Y_train.shape, X_test.shape, Y_test.shape
    
    true = np.ones((batch_size, 1))
    fake = np.zeros((batch_size, 1))
    
    for i in range(epoch):
        # 실제 데이터를 판별자에 입력하는 부분.
        idx = np.random.randint(0, X_train.shape[0], batch_size)
        imgs = X_train[idx]
        d_loss_real = discriminator.train_on_batch(imgs, true) # batch_size 길이 만큼 판별을 시작
        
        # 가상 이미지를 판별자에 입력하는 부분.
        noise = np.random.normal(0, 1, (batch_size, 100))
        gen_imgs = generator.predict(noise)
        d_loss_fake = discriminator.train_on_batch(gen_imgs, fake)
        
        # 판별자와 생성자의 오차를 계산.
        d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)
        g_loss = gan.train_on_batch(noise, true)
        
        print('epoch:%d' % i, ' d_loss:%.4f' % d_loss, ' g_loss:%.4f' % g_loss)
        # 이부분은 중간 과정을 이미지로 저장해 주는 부분. 본 장의 주요 내용과 관련이 없어
        # 소스코드만 첨부. 만들어진 이미지들은 gan_images 폴더에 저장.
        if i % saving_interval == 0:
            #r, c = 5, 5
            noise = np.random.normal(0, 1, (25, 100))
            gen_imgs = generator.predict(noise)
        
            # Rescale images 0 - 1
            gen_imgs = 0.5 * gen_imgs + 0.5
        
            fig, axs = plt.subplots(5, 5)
            count = 0
            for j in range(5):
                for k in range(5):
                    axs[j, k].imshow(gen_imgs[count, :, :, 0], cmap='gray')
                    axs[j, k].axis('off')
                    count += 1
            fig.savefig("ganimages/gan_mnist_%d.png"%i)
            plt.show()

gan_train(2001, 32, 500)

