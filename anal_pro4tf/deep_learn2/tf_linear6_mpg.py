# 자동차 연비 예측 - 선형회귀분석

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow.keras import layers

dataset = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/auto-mpg.csv')
print(dataset.head(2))
print(dataset.columns)
del dataset['car name'] # 필요없는 칼럼 제거
dataset.drop(['cylinders', 'acceleration', 'model year', 'origin'], axis = 'columns', inplace = True)
print(dataset.head(2))
print(dataset.corr()) # 상관계수
print(dataset.info())

# 강제 형변환 시 ValueError를 무시하기 errors = 'coerce', 해당 행은 NaN이 됨
dataset['horsepower'] = dataset['horsepower'].apply(pd.to_numeric, errors = 'coerce') 
print(dataset.info())
print(dataset.isna().sum()) # ?가 NaN으로 바뀜
dataset = dataset.dropna() # NaN 지우기
print(dataset.isna().sum())

# 시각화
# sns.pairplot(dataset[['mpg', 'weight', 'horsepower', 'displacement']], diag_kind='kde') # 밀도분포 보여주는것 kde
# plt.show()

# train / test 분리
print(dataset.shape)
train_dataset = dataset.sample(frac = 0.7, random_state=123)
# print(train_dataset.index)
test_dataset = dataset.drop(train_dataset.index)
print(train_dataset.shape) # (274, 8)
print(test_dataset.shape) # (118, 8)

train_stat = train_dataset.describe()
#print(train_stat)
train_stat.pop('mpg') # 'mpg' : label
train_stat = train_stat.transpose()
print(train_stat)

train_labels = train_dataset.pop('mpg')
print(train_labels[:2])
test_labels = test_dataset.pop('mpg')
print(test_labels[:2])

def st_func(x): # 표준화 처리함수 (요소값 - 평균) / 표준편차
    return ((x - train_stat['mean']) / train_stat['std'])

#print('st_func(10) : ', st_func(10))
#print('st_func(train_dataset[:3]) : ', train_dataset[:3])
st_train_data = st_func(train_dataset) # 표준화된 train feature
st_test_data = st_func(test_dataset) # 표준화된 test feature

# print(train_dataset[:3])
# print(st_train_data[:3])

# 모델 작성
def build_model():
    # layer 생성
    network = tf.keras.Sequential([
            layers.Dense(units=64, activation = 'linear', input_shape = [3]),
            layers.Dense(units=64, activation = 'linear'),
            layers.Dense(1, activation = 'linear')
        ])
    
    # 컴파일
    opti = tf.keras.optimizers.Adam(0.01)
    network.compile(optimizer = opti, loss = 'mean_squared_error', metrics = ['mean_absolute_error', 'mean_squared_error']) # mae, mse 순서 full-name
    
    return network

model = build_model()
print(model.summary())

# fit() 전에 모델을 predict() 할 수 있다.
print(model.predict(st_train_data[:1])) # 결과에 관심 X

EPOCHS = 5000

# 학습 조기종료 (EarlyStopping)
#early_stop = tf.keras.callbacks.EarlyStopping(monitor = 'loss') 
early_stop = tf.keras.callbacks.EarlyStopping(monitor = 'val_loss', patience=5)

history = model.fit(st_train_data, train_labels, epochs=EPOCHS, batch_size = 32, \
                    validation_split = 0.2, verbose=1, callbacks=[early_stop])

df = pd.DataFrame(history.history)
print(df.head(3), df.columns) # ['loss', 'mean_squared_error', 'mean_absolute_error', 'val_loss', 'val_mean_squared_error', 'val_mean_absolute_error']

# 시각화
def plot_history(history):
    hist = pd.DataFrame(history.history)
    hist['epoch'] = history.epoch
    plt.figure(figsize=(8, 12))
    
    plt.subplot(2, 1, 1)
    plt.xlabel('epoch')
    plt.ylabel('mean_absolute_error[mpg]')
    plt.plot(hist['epoch'], hist['mean_absolute_error'], label = 'train error')
    plt.plot(hist['epoch'], hist['val_mean_absolute_error'], label = 'val error')
    plt.legend()
    
    plt.subplot(2, 1, 2)
    plt.xlabel('epoch')
    plt.ylabel('mean_squared_error[mpg]')
    plt.plot(hist['epoch'], hist['mean_squared_error'], label = 'train error')
    plt.plot(hist['epoch'], hist['val_mean_squared_error'], label = 'val error')
    plt.legend()
    
    plt.show()
    
plot_history(history)
    
# 모델 평가
loss, mae, mse = model.evaluate(st_test_data, test_labels)
print('loss : ', loss)
print('mse : ', mse)
print('mae : ', mae)

# 새로운 데이터로 예측 시 표준화 후 참여
print(test_dataset[:2])
new_data = pd.DataFrame({'displacement' : [300, 400], 'horsepower' : [120, 180], 'weight' : [2000, 5000]})
print(new_data)
new_st_test_data = st_func(new_data) # 표준화하기
new_pred = model.predict(new_st_test_data).flatten() # 차원축소
print("예측 결과 : ", new_pred)
