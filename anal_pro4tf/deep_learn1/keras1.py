# Keras를 이용해 OR게이트 논리 모델을 생성한 후 분류 결과 확인
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation   # Dense 완전연결체
from tensorflow.keras.optimizers import SGD, Adam, RMSprop

# 순서 1: 데이터  수집 및 가공
x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0,1,1,1])

print(x)

# 순서 2 : 모델 생성
# model = Sequential([
#     Dense(input_dim = 2, units = 1), # 두개가 들어와서 한개 출력
#     Activation('sigmoid') # 이항분류:sigmoid,  다향분류:softmax
# ])

model = Sequential() # 컨테이너 느낌
model.add(Dense(units= 1, input_dim = 2)) # 이런식으로 추가+++ 해도 되는것
model.add(Activation('sigmoid'))

# 순서 3 : 모델 학습과정 설정(컴파일)
# model.compile(optimizer = 'sgd', loss = 'binary_crossentropy', metrics = ['accuracy'])
# model.compile(optimizer = 'rmsprop', loss = 'binary_crossentropy', metrics = ['accuracy'])
# model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
# model.compile(optimizer = SGD(lr=0.1), loss = 'binary_crossentropy', metrics = ['accuracy'])
# model.compile(optimizer = SGD(lr=0.1, momentum = 0.9), loss = 'binary_crossentropy', metrics = ['accuracy'])
# model.compile(optimizer = RMSprop(lr=0.1), loss = 'binary_crossentropy', metrics = ['accuracy'])
model.compile(optimizer = Adam(lr=0.01), loss = 'binary_crossentropy', metrics = ['acc']) # lr = 학습비율
# optimizer: 모델을 update cost(loss)가 최소화될수 있도록 해줌 'sgd'는 확률적 경사 하강법
# loss 모델오차 최소화 binary -> 이항, crossentropy -> 불순물
# metrics 훈련 검정 모니터링 분류기 때문에 'accuracy'

# 순서4 : 모델 학습(train data)
model.fit(x, y, epochs = 1000, batch_size = 1, verbose = 1) # verbose = 학습진행과정 1은 자세하게 보여주고, 2는 간략하게 보여주고, 0은 안보여줌(대신 속도가 빠름)
# epochs = epochs 1은 전체 데이터를 한 차례 훑고 지나갔음을 의미함. 정수값 기재 필요.총 훈련 횟수를 정의.
# batch_size = 기본값은 32. 미니 배치 경사 하강법을 사용하고 싶지 않을 경우에는 batch_size=None을 통해 선택 가능.

# 순서 5 : 모델 평가(test data)
loss_metrics = model.evaluate(x, y) # test data가 없어서 뒷부분 생략
print('loss_metrics', loss_metrics)

"""
# 참고 : 모델 학습의 결과가 만족스러운 경우  모델을 저장 후 읽어서 예측을 한다.
model.save('test.hdf5') # 모델 저장
# hdf5는 대용량 데이터 처리를 할때 사용하는 구조

# 모델을 읽을때.
from tensorflow.keras.models import load_model
model = load_model('test.hdf5') # 저장된 모델 읽기
"""
# 순서 6 : 학습결과 확인 ----
pred = model.predict(x)
print('예측결과 : \n', pred) # 0.5보다작으면 0, 크면 1 잘 예측했다.
print('예측결과 : \n', pred.flatten()) # 차원 축소

pred = (model.predict(x) > 0.5).astype('int32') # 0.5 기준으로 0과 1 나누기
print('예측결과 : \n', pred.flatten()) # 차원축소


