# Perceptron : 단층신경망으로 input_data * 가중치의 합에 대해 임계값(활성화함수)을 기준으로 이항분류가 가능.
# 단층신경망으로 논리회로 분류
import numpy as np
from sklearn.linear_model import Perceptron

feature = np.array([[0, 0], [0, 1], [1,0], [1, 1]])
print(feature)
#label = np.array([0, 0, 0, 1]) # and
#label = np.array([0, 1, 1, 1]) # or
label = np.array([0, 1, 1, 0]) # xor : 단층신경망으로 분류 X

ml = Perceptron(max_iter = 1000).fit(feature, label) # max_iter 학습횟수
print(ml)
print(ml.predict(feature))

print("\n다층신경망으로 xor 문제 해결")
from sklearn.neural_network import MLPClassifier
#ml2 = MLPClassifier(hidden_layer_sizes = 30).fit(feature, label)
ml2 = MLPClassifier(hidden_layer_sizes = (10,10,10), max_iter = 100, verbose = 1, learning_rate_init = 0.01).fit(feature, label) # learning_rate_init 학습률 얼마씩 할것인지
# max_iter 학습횟수
print(ml2)
print(ml2.predict(feature))