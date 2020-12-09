# CNN : 이미지의 특징을 뽑아 크기를 줄이고, 이를 일차원 배열로 만들어 완전연결층(여러 층의 Dense)으로 전달해 이미지(텍스트)를 분류
# 분류 정확도가 상당히 높다. 연산량이 많아 시스템의 성능이 좋아야 한다.

# MNIST 손글씨 : 흑백 이미지
import tensorflow as tf
from tensorflow.keras import datasets, layers, models

(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()
print(train_images.shape, type(train_images), train_images.ndim)

# CNN 처리를 위해 3차원 자료를 4차원으로 구조 변경. channel을 추가(흑백:1, 칼라:3)