# RNN으로 문맥을 반영해서 다음 단어를 예측하기 - many to one
from tensorflow.keras.preprocessing.text import Tokenizer

# text = """경마장에 있는 말이 뛰고 있다
# 그의 말이 법이다
# 가는 말이 고와야 오는 말이 곱다"""

text = '''
오전 7시 40분께 서울 지하철 5호선 서대문역 주변에서는 마스크를 착용한데다 패딩 모자를 깊이 눌러써 얼굴이 거의 보이지 않는 직장인들이 빠른 발걸음으로 출근을 서둘렀다.
서대문역 인근 오피스텔에서 광화문으로 걸어서 출근한다는 최모(37)씨는 "두세 정거장 거리인데 오늘은 너무 추워서 버스를 탈 생각"이라고 말했다.
갑자기 찾아온 추위에 롱패딩에 목도리까지 둘러 두꺼워진 옷차림으로 뒤뚱뒤뚱 걷는 모습도 보였고, 빠른 걸음을 옮기다 그늘 속에 있는 빙판에서 넘어질 뻔한 시민들도 있었다.
올겨울 들어 처음으로 한파주의보가 발령된 이 날 서울의 최저 기온은 영하 9.7도를 기록했다.
살을 에는 듯한 찬바람에 지하철역에서 나와 곧장 카페로 종종걸음치는 사람들도 보였다. 이들은 따뜻한 커피를 핫팩처럼 손에 쥐고 회사로 향했다.
지하철에서 내려 버스 환승을 기다리던 직장인 김모(30)씨는 "위아래로 세 겹씩 껴입어 지하철에서는 살짝 땀이 났는데, 내리니까 잘했다 싶다"며 "코로나도 코로나지만 이렇게 추운 날이면 정말 재택근무가 가능한 사람들이 부럽다"고 말했다.
오전 8시 40분께 독립문역 인근 버스정류장에서는 손이 시려서인지 평소와 달리 스마트폰을 보는 시민이 거의 없었다.
공덕역 근처에서 만난 직장인 이모(32)씨는 "코로나 때문에 주말 내내 집에만 있다가 오늘 처음 나왔는데 이렇게 추워진 줄 몰랐다"며 "안에 패딩 조끼라도 하나 더 껴입고 나올 걸 그랬다"고 말했다.
박모(39)씨는 "오늘 아침 기온이 영하 10도로 떨어질 거라는 예보를 보고 충분히 껴입은 덕분에 특별히 춥다는 느낌은 들지 않는다"며 "이런 추위에는 마스크가 방한용품의 기능까지 하는 것 같다"며 웃었다.
한파와 신종 코로나바이러스 감염증(코로나19) 유행이 겹치며 마스크를 두 겹씩 쓴 사람들도 있다.
동장군이 반가운 사람들도 있다.
선릉역 주변에서 따뜻한 음료와 토스트 등을 파는 노점상 김모(60)씨는 "요즘 손님이 너무 없어 걱정이었는데, 날이 추워지니 그래도 아침에 찾는 사람들이 많아 다행이다"라고 말했다.
'''

tok = Tokenizer()
tok.fit_on_texts([text])
encoded = tok.texts_to_sequences([text])[0]
print(encoded)
print(tok.word_index)

vocab_size = len(tok.word_index)
print('단어 집합의 크기 : ', vocab_size)

sequences = list()
for line in text.split('\n'):
  encoded = tok.texts_to_sequences([line])[0]
  for i in range(1, len(encoded)):
    sequ = encoded[:i + 1]
    #print(sequ)
    sequences.append(sequ)
print(sequences)
print('학습에 참여할 샘플 수 : %d'%len(sequences)) # 전체 학습데이터에 대해서 맨 우측에 있는 단어는 레이블로 처리되도록 분리

print(max(len(i) for i in sequences))

from tensorflow.keras.preprocessing.sequence import pad_sequences
max_len = max(len(i) for i in sequences)
psequences = pad_sequences(sequences, maxlen = max_len, padding = 'pre')
print(psequences)

import numpy as np
psequences = np.array(psequences)
x = psequences[:, :-1] # feature
y = psequences[:, -1] # label
#print(x)
print(y) # one-hot 처리 필요

from tensorflow.keras.utils import to_categorical
y = to_categorical(y, num_classes = vocab_size + 1) # 앞에 0이있어서 +1 해준값을 넣어줌
print(y)

# model
from tensorflow.keras.layers import Embedding, Dense, LSTM, Input
from tensorflow.keras.models import Sequential, Model

# function api
# input = Input(shape = (50, 1))
# lstm_layer = LSTM(20, activation='tanh')(input)
# x = Dense(20, activation = 'relu')(lstm_layer)
# output = Dense(1, activation = 'sigmoid')(x)
# model = Model(input = input, output = output)

# Sequential api
model = Sequential()
model.add(Embedding(vocab_size + 1, 32, input_length = max_len - 1))
# model.add(SimpleRNN(32, activation = 'tanh'))
model.add(LSTM(32, activation = 'tanh'))
model.add(Dense(32, activation = 'relu'))
model.add(Dense(vocab_size + 1, activation = 'softmax'))
#print(model.summary())
model.compile(loss = 'categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x, y, epochs=200, verbose = 2)
print(model.evaluate(x, y))

def sequence_generation(model, t, current_word, n):
    init_word = current_word
    sentence = ''
    for _ in range(n):
        encoded = t.texts_to_sequences([current_word])[0]
        encoded = pad_sequences([encoded], maxlen = max_len - 1, padding = 'pre')
        #print(encoded)
        result = np.argmax(model.predict(encoded))
        #print(result)
        for word, index in t.word_index.items():
            #print('word : ', word, ', index : ', index)
            if index == result:
                break
        current_word = current_word + ' ' + word
        sentence = sentence + ' ' + word
    sentence = init_word + sentence
    return sentence
        
# print(sequence_generation(model, tok, '경마장에', 1))
# print(sequence_generation(model, tok, '경마장에', 2))
# print(sequence_generation(model, tok, '경마장에', 4))
# print(sequence_generation(model, tok, '그의', 1))
# print(sequence_generation(model, tok, '가는', 1))
# print(sequence_generation(model, tok, '그의', 2))
# print(sequence_generation(model, tok, '가는', 2))
# print(sequence_generation(model, tok, '경마', 1))
# print(sequence_generation(model, tok, '말', 1))
# print(sequence_generation(model, tok, '겨울', 1))

print(sequence_generation(model, tok, '코로나', 10))
print(sequence_generation(model, tok, '마스크', 10))
print(sequence_generation(model, tok, '아침', 5))
print(sequence_generation(model, tok, '관악산', 20))