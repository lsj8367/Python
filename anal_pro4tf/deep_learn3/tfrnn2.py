# RNN의 기본 구조 연습
import numpy as np
import tensorflow as tf

# many to one
x = np.array([ [[1],[2],[3]], [[2],[3],[4]], [[3],[4],[5]] ], dtype=np.float32)
y = np.array([[4],[5],[6]], dtype=np.float32)
print('shape : x:{}, y:{}'.format(x.shape, y.shape))

# function api 사용
# many to one
layer_input = tf.keras.Input(shape = (3, 1))
#layer_rnn = tf.keras.layers.SimpleRNN(100)(layer_input) # total 10301개
layer_rnn = tf.keras.layers.LSTM(100)(layer_input) # total 40901
#layer_rnn = tf.keras.layers.GRU(100)(layer_input) # total 31001
layer_output = tf.keras.layers.Dense(1)(layer_rnn)

model = tf.keras.Model(layer_input, layer_output)
model.compile(loss = 'mse', optimizer = 'adam')
model._name = 'many-to-one'
print(model.summary())

model.fit(x, y, epochs = 100, batch_size=1, verbose=0)
print('pred: ', model.predict(x).flatten())
new_data = np.array([[[4],[5],[6]]], dtype=np.float32)
print('new pred : ', model.predict(new_data).flatten())

# many to many
layer_input = tf.keras.Input(shape = (3, 1))
# layer_rnn = tf.keras.layers.LSTM(100, return_sequences=True)(layer_input) # total 40901
# layer_output = tf.keras.layers.TimeDistributed(tf.keras.layers.Dense(1))(layer_rnn)


# stacked many to one
layer_input = tf.keras.Input(shape = (3, 1))
layer_rnn1 = tf.keras.layers.LSTM(100, return_sequences=True)(layer_input)
layer_rnn2 = tf.keras.layers.LSTM(100)(layer_rnn1)
layer_output = tf.keras.layers.Dense(1)(layer_rnn2)


model = tf.keras.Model(layer_input, layer_output)
model.compile(loss = 'mse', optimizer = 'adam')
model._name = 'many-to-many'
print(model.summary())

model.fit(x, y, epochs = 100, batch_size=1, verbose=0)
print('pred: ', model.predict(x))
new_data = np.array([[[4],[5],[6]]], dtype=np.float32)
print('new pred : ', model.predict(new_data))