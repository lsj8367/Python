# Recurrent Neural Network(RNN, 순환신경망)
# 기존의 Feed Forward Neural Network(은닉층 -> 출력층으로 일방향 처리)와는 달리 입력과 출력을 엮어 시퀀스 단위로 처리
# 사용 예) 글작성, 번역, 품사태깅, 이미지 캡션, 챗봇, 텍스트 분류...
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, LSTM

model = Sequential()
#model.add(SimpleRNN(3, input_length =2 , input_dim = 10))
model.add(SimpleRNN(3, input_shape = (2, 10)))
print(model.summary())
print()
model2 = Sequential()
model2.add(LSTM(3, input_shape=(2, 10)))
print(model2.summary())

model = Sequential()
model.add(SimpleRNN(3, batch_input_shape = (8, 2, 10))) # batch_size -> 뉴럴꾸러미 갯수, sequence수 한 뉴럴의 갯수, 입력수
print(model.summary())
print()
model2 = Sequential()
model2.add(LSTM(3, batch_input_shape=(8, 2, 10)))
print(model2.summary())

model = Sequential()
model.add(SimpleRNN(3, batch_input_shape = (8, 2, 10), return_sequences=True)) # batch_size -> 뉴럴꾸러미 갯수, sequence수 한 뉴럴의 갯수, 입력수
print(model.summary())
print()
model2 = Sequential()
model2.add(LSTM(3, batch_input_shape=(8, 2, 10), return_sequences=True))
print(model2.summary())

# SimpleRNN : sequence를 구성하는 4개의 숫자를 입력받아 다음번 숫자를 예측하는 모델 작성
import tensorflow as tf
import numpy as np

x = []
y = []

for i in range(6):
    lst = list(range(i, i + 4))
    x.append(list(map(lambda c: [c / 10], lst)))
    y.append((i + 4) / 10)

print(x, ' ', len(x))
print(y, ' ', len(y))
for i in range(len(x)):
    print(x[i], y[i])

model = tf.keras.Sequential([
    #tf.keras.layers.SimpleRNN(units=10, activation='tanh', input_shape = [4, 1]), # 순차적방법 tanh   # 120개
    tf.keras.layers.LSTM(units=10, activation='tanh', input_shape = [4, 1]), # 순차적방법 tanh   # 480개
    #tf.keras.layers.GRU(units=10, activation='tanh', input_shape = [4, 1]),   # 390개
    tf.keras.layers.Dense(1) # 예측값이 1개니까 1씀
])
model.compile(optimizer='adam', loss = 'mse') # 숫자니까 mse
print(model.summary())

model.fit(x, y, epochs = 100, verbose = 0)
print('예측값 : ', model.predict(x).flatten())
print("실제값 : ", y)

# 새값으로 예측
print('새 값으로 예측값 : ', model.predict([[[0.6], [0.7], [0.8], [0.9]]]).flatten())
print('새 값으로 예측값 : ', model.predict([[[-0.2], [-0.1], [0.0], [0.1]]]).flatten())