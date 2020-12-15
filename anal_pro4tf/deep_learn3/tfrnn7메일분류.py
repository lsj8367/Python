# !sudo apt-get install -y fonts-nanum
# !sudo fc-cache -fv
# !rm ~/.cache/matplotlib -rf

# RNN으로 스팸메일 분류
import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/spam.csv', encoding = 'latin1')
print(data.head())
print('샘플 수 : ', len(data))
print(data[:2])
print(data.info())
del data['Unnamed: 2']
del data['Unnamed: 3']
del data['Unnamed: 4']
print(data[:3])
data['v1'] = data['v1'].replace(['ham', 'spam'],[0, 1]) # ham은 0 spam은 1로 바꿈
print(data[:3])
print(data.info())
print(data.isnull().values.any()) # False

print(data['v2'].nunique(), data['v1'].nunique()) # nunique 는 중복되지 않는 갯수
# 총 5572 중 중복 제외 갯수 5169개
data.drop_duplicates(subset = ['v2'], inplace = True) # 중복은 제거됨
print('샘플 갯수 : ', len(data)) # 5169

# 데이터 분포 시각화
import matplotlib.pyplot as plt
# data['v1'].value_counts().plot(kind = 'bar')
# plt.show()

print(data.groupby('v1').size().reset_index(name = 'count'))
#    v1  count
# 0   0   4516
# 1   1    653

# feature와 label 얻기
x_data = data['v2']
y_data = data['v1']
print('메일 수 : {}'.format(len(x_data)))

# token 처리
from tensorflow.keras.preprocessing.text import Tokenizer
tokenizer = Tokenizer()
tokenizer.fit_on_texts(x_data)
sequences = tokenizer.texts_to_sequences(x_data)
print(sequences[:3])

# 단어에 부여된 인덱스 값 확인
word_to_index = tokenizer.word_index
print(word_to_index)

vocab_size = len(word_to_index) + 1
print('단어 집합 크기 : {}'.format(vocab_size))

# train / test    8 : 2
n_of_train = int(len(sequences) * 0.8)
n_of_test = int(len(sequences) - n_of_train)
print('train : ', n_of_train) # 4135
print('test : ', n_of_test) # 1034

# x_data에 대해 정수 인코딩된 결과인 sequences를 x_data로 변경하고 분포 확인
x_data = sequences
print('메일의 최대 길이 %d'%max(len(i) for i in x_data)) # 189
print('메일의 평균 길이 %f'%(sum(map(len, x_data)) / len(x_data))) # 15.610370

from tensorflow.keras.preprocessing.sequence import pad_sequences
max_len = 189
data = pad_sequences(x_data, maxlen = max_len)
print(data.shape)
#print(data[0])

# train/test 분리작업 실행
import numpy as np
x_train = data[:n_of_train]
y_train = np.array(y_data[:n_of_train])
x_test = data[n_of_train:]
y_test = np.array(y_data[n_of_train:])
print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)
#print(x_train[:2])
#print(y_train[:2])

# model
from tensorflow.keras.layers import LSTM, Embedding, Dense
from tensorflow.keras.models import Sequential
model = Sequential()
model.add(Embedding(vocab_size, 32))
model.add(LSTM(32, activation = 'tanh'))
model.add(Dense(1, activation = 'sigmoid')) # 이항분류

model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['acc'])
history = model.fit(x_train, y_train, epochs = 10, batch_size = 64, validation_split = 0.2, verbose = 2)
print('model 평가 : ', model.evaluate(x_test, y_test))

# Commented out IPython magic to ensure Python compatibility.
# !sudo apt-get install -y fonts-nanum
# !sudo fc-cache -fv
# !rm ~/.cache/matplotlib -rf

import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic') 
history_dict = history.history
loss = history_dict['loss']
val_loss = history_dict['val_loss']
print(val_loss)

plt.title('이승재')
plt.plot(loss, 'bo-', label = 'loss')
plt.plot(val_loss, 'ro-', label = 'val_loss')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()
print('추천 epoch 수 : 4')
plt.show()