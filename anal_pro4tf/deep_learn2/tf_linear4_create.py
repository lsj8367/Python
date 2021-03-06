# 3 ways to create a Keras model with TensorFlow 2.0
# (Sequential, Functional, and Model Subclassing)

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers
import numpy as np

x_data = np.array([1,2,3,4,5], dtype = np.float32) # 공부시간 int형 float으로 변환
y_data = np.array([11,32,53,58,65], dtype = np.float32) # 공부시간에 따른 취득 점수

print(np.corrcoef(x_data, y_data)) # 상관관계  0.95939715

# 선형회귀분석 방법1 : Sequential api 사용
print('Sequential api 사용')
model = Sequential()
model.add(Dense(units=1, input_dim = 1, activation='linear'))
#model.add(Dense(1, activation='linear')) # layer추가

opti = optimizers.SGD(lr=0.001)
model.compile(optimizer = opti, loss = 'mse', metrics=['mse', 'mae']) # mae가 mse보다 이상치에 덜 민감하다.
model.fit(x = x_data, y = y_data, batch_size = 1, epochs = 100, verbose=0)
loss_metrics = model.evaluate(x_data, y_data)
print('loss_metrics : ', loss_metrics)

# 결정계수
from sklearn.metrics import r2_score
print('설명력 : ', r2_score(y_data, model.predict(x_data)))

print('실제 값 : ', y_data)
print('예측 값 : ', model.predict(x_data).flatten()) # 차원축소
print('새로운 공부 시간에 대한 예상 점수 : ', model.predict([2.3, 6.8, 7.0]).flatten())

# 시각화
import matplotlib.pyplot as plt
'''
plt.rc('font', family = 'malgun gothic')
plt.plot(x_data, model.predict(x_data), 'b', x_data, y_data, 'ko')
plt.xlabel('공부시간')
plt.ylabel('시험점수')
plt.show()
'''

# 선형회귀방법 2 : Functional api 사용 - 방법1 보다 다소 복잡해보이나 유연한 모델 작성이 가능. 여러 층의 자원을 공유 가능
print('Functional api 사용')
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model

inputs = Input(shape = (1,)) # input layer를 생성
outputs = Dense(1, activation = 'linear')(inputs) # 입력객체를 뒤에 붙여줌

# 여러개일 경우
#outputs1 = Dense(5, activation = 'linear')(inputs)
#outputs2 = Dense(1, activation = 'linear')(outputs1) # 첫번째 output인자를 뒤에 붙여줌

model2 = Model(inputs, outputs)

opti = optimizers.SGD(lr=0.001)
model2.compile(optimizer = opti, loss = 'mse', metrics=['mse', 'mae']) # mae가 mse보다 이상치에 덜 민감하다.
model2.fit(x = x_data, y = y_data, batch_size = 1, epochs = 100, verbose=0)
loss_metrics = model2.evaluate(x_data, y_data)
print('loss_metrics : ', loss_metrics)

# 결정계수
print('설명력 : ', r2_score(y_data, model2.predict(x_data)))
print('실제 값 : ', y_data)
print('예측 값 : ', model2.predict(x_data).flatten()) # 차원축소
print('새로운 공부 시간에 대한 예상 점수 : ', model2.predict([2.3, 6.8, 7.0]).flatten())

# 선형회귀분석 방법3 : Subclassing api 사용 - 방법1, 2는 선언적인 방법이나, Subclassing은 동적인 구조가 필요할 때 사용

print('\nSubclassing api 사용 1===================')
class MyModel(Model):
    def __init__(self):
        super(MyModel, self).__init__()
        self.d1 = Dense(2, activation='linear')
        self.d2 = Dense(1, activation='linear')
        
    def call(self, x): # 모델.fit() , 모델.evaluate(), 모델.predict()
        # python 작업가능 ,계산, for, if, tensor 처리...
        x = self.d1(x)
        return self.d2(x)
    
model3 = MyModel()

opti = optimizers.SGD(lr=0.001)
model3.compile(optimizer = opti, loss = 'mse', metrics=['mse', 'mae']) # mae가 mse보다 이상치에 덜 민감하다.
model3.fit(x = x_data, y = y_data, batch_size = 1, epochs = 50, verbose=0)
print('실제 값 : ', y_data)
print('예측 값 : ', model3.predict(x_data).flatten()) # 차원축소
print('새로운 공부 시간에 대한 예상 점수 : ', model3.predict([2.3, 6.8, 7.0]).flatten())

print('\nSubclassing api 사용2======')
from tensorflow.keras.layers import Layer

class Linear(Layer):
    def __init__(self, units = 1):
        super(Linear, self).__init__()
        self.units = units
        
    def build(self, input_shape): # 이 함수안에있는 call을 호출
        self.w = self.add_weight(shape = (input_shape[-1], self.units), \
                                 initializer = 'random_normal', trainable = True) # trainable = True <<<< 역전파 사용 유무
        self.b = self.add_weight(shape = (self.units), initializer = 'zeros', trainable = True)
        # 역전파 : 역전파, 오차 역전파법 또는 오류 역전파 알고리즘은 다층 퍼셉트론 학습에 사용되는 통계적 기법을 의미한다.
        
    def call(self, inputs): # wx + b 형식을 만드는것?????
        return tf.matmul(inputs, self.w) + self.b
    
    
class MyMlp(Model):
    def __init__(self):
        super(MyMlp, self).__init__()
        self.linear_1 = Linear(1) # layer가 한개일 경우
        
        # layer가 복수일 경우
        # self.linear_1 = Linear(2)
        # self.linear_2 = Linear(1)
    
    def call(self, inputs): # Linear의 build를 호출
        return self.linear_1(inputs)
    
model4 = MyMlp() # 이것을 불러서 위의 Linear클래스도 부름

opti = optimizers.SGD(lr=0.001)
model4.compile(optimizer = opti, loss = 'mse', metrics=['mse', 'mae']) # mae가 mse보다 이상치에 덜 민감하다.
model4.fit(x = x_data, y = y_data, batch_size = 1, epochs = 50, verbose=0)
print('실제 값 : ', y_data)
print('예측 값 : ', model4.predict(x_data).flatten()) # 차원축소
print('새로운 공부 시간에 대한 예상 점수 : ', model4.predict([2.3, 6.8, 7.0]).flatten())
