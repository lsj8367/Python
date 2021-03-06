# zoo dataset 으로 동물 분류 : type 7가지
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
import numpy as np

xy = np.loadtxt('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/zoo.csv', delimiter = ',')
print(xy[0], xy.shape)

x_data = xy[:, 0:-1] # feature
y_data = xy[:, -1] # label
print(x_data[:2], x_data.shape)
print(y_data[:2], y_data.shape, ' ', set(y_data))

nb_classes = 7 # 0 ~ 6
y_one_hot = to_categorical(y_data, nb_classes)  # one-hot encoding
print(y_one_hot[:3])

# model
model = Sequential()
model.add(Dense(32, input_shape = (16, ), activation = 'relu'))
model.add(Dense(32, activation = 'relu'))
model.add(Dense(nb_classes, activation = 'softmax'))
print(model.summary())

model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics=['acc'])
# loss = 'sparse_categorical_crossentropy' 내부적으로 one-hot encoding 해줌

history = model.fit(x_data, y_one_hot, epochs = 100, batch_size = 10, validation_split = 0.3, verbose = 2)
print(model.evaluate(x_data, y_one_hot))

history_dict = history.history
loss = history_dict['loss']
val_loss = history_dict['val_loss']
acc = history_dict['acc']
val_acc = history_dict['val_acc']

"""
# 시각화
import matplotlib.pyplot as plt
plt.plot(loss, 'b-', label = 'train loss')
plt.plot(val_loss, 'r--', label = 'train val_loss')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()
plt.show()

plt.plot(acc, 'b-', label = 'train acc')
plt.plot(val_acc, 'r--', label = 'train val_acc')
plt.xlabel('epoch')
plt.ylabel('acc')
plt.legend(loc = 'best')
plt.show()
"""
# predict
pred_data = x_data[:1]
pred = model.predict(pred_data)
print(pred, ' ', np.sum(pred))
print(np.argmax(pred))

# 여러개를 예측
pred_datas = x_data[:15]
preds = [np.argmax(i) for i in model.predict(pred_datas)]
print('예측값들 : ', preds)
print('실제값들 : ', y_data[:15].flatten())

# 새로운 값 예측
print(x_data[:1])
new_data = [[0., 1., 1., 1., 1., 1., 1., 0., 1., 1., 1., 1., 2., 1., 1., 0.]]
print(np.argmax(model.predict(new_data)))









