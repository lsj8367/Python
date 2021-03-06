# 모델의 정확도가 높을수록 비용함수 값은 낮아지며, 모델의 정확도가 낮으면 비용함수는 높아진다.
import math
import numpy as np
real = [10, 9, 3, 2, 11]
#pred = np.array([11, 5, 2, 4, 3]) # 모델이 예측한 값
pred = np.array([10, 8, 4, 3, 11]) # 모델이 예측한 값
print(np.corrcoef(pred, real)) # 0.456

print()
cost = 0
for i in range(5):
    cost += math.pow(pred[i] - real[i], 2)
    print(cost)
    
print(cost / len(pred))

print('----------------------')
# 비용함수(cost)와 가중치(W)의 변화값을 시각화
import tensorflow as tf
import matplotlib.pyplot as plt

x = [1,2,3,4,5] # feature
#y = [1,2,3,4,5] # label
y = [2,4,6,8,10] # label
b = 0 # 절편

w_val = []
cost_val = []

for i in range(-30, 50):
    feed_w = i * 0.1 # 0.1 <== learning rate
    #print(feed_w)
    hypothesis = tf.multiply(feed_w, x) + b
    cost = tf.reduce_mean(tf.square(hypothesis - y)) # 예측값(hypothesis) - 실제값(y)
    cost_val.append(cost)
    w_val.append(feed_w)
    print((str(i) + ': cost: ' + str(cost.numpy()) + ', weight:' + str(feed_w)))

plt.plot(w_val, cost_val, 'o')
plt.xlabel('weight')
plt.ylabel('cost')
plt.show()
