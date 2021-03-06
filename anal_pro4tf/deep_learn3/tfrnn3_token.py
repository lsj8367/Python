# 텍스트의 토큰화 : 컴퓨터는 텍스트를 수치화하는 전처리 과정을 필요로함
# text를 자소별, 단어별, 형태소별, 문장별 분리
from tensorflow.keras.preprocessing.text import Tokenizer

# corpus : 연구 목적으로 수집된 자연어 집합 txt, csv, xml, ...등 다양한 종류로 구성되어있다.
sampleText = ['The cat say on the mat.', 'The dog ate my homework.'] # list type

# token 처리 : 방법1
token_index ={} # dict type의 token 기억용 변수
for sam in sampleText:
  for word in sam.split(sep = ' '):
    if word not in token_index:
      token_index[word] = len(token_index)

print(token_index)

print()
# token 처리 : 방법2 - keras 가 제공하는 클래스 사용
tokenizer = Tokenizer() # numwords를 빼면 자동처리
tokenizer.fit_on_texts(sampleText) # token 처리
print(tokenizer.word_index) # 중복제거
token_seq = tokenizer.texts_to_sequences(sampleText)
print(token_seq) # [[1, 2, 3, 4, 1, 5], [1, 6, 7, 8, 9]]
# ['The cat say on the mat.', 'The dog ate my homework.']

token_mat = tokenizer.texts_to_matrix(sampleText, mode = 'binary') # count, freq, tfidf, binary(one-hot encoding)
print(token_mat)
print(tokenizer.word_counts)  # 각 단어의 갯수
print(tokenizer.document_count) # 총 문장 수
print(tokenizer.word_docs)

from tensorflow.keras.utils import to_categorical
token_seq = to_categorical(token_seq[0], num_classes = 6)
print(token_seq)

import numpy as np
docs = ['너무 재밌어요', '최고에요','참 잘 만든 영화에요', '추천하고 싶은 영화입니다', '한번 더 보고 싶네요', '글쎄요', '별로에요', '생각보다 지루하네요', '연기가 어색하네요', '재미없어요']
classes = np.array([1,1,1,1,1,0,0,0,0,0]) # 1 : 긍정, 2 : 부정
token = Tokenizer()
token.fit_on_texts(docs)
print(token.word_index)
x = token.texts_to_sequences(docs) # 텍스트를 정수 인덱싱해서 리스트 형으로 반환
print('토큰화 결과 : ', x)

from tensorflow.keras.preprocessing.sequence import pad_sequences
padded_x = pad_sequences(x, 4)
print('패딩 결과 : ', padded_x)  #4칸으로 맞춰줌

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Flatten, Embedding

word_size = len(token.word_index) + 1 # 임베딩 단어수 지정
model = Sequential()
model.add(Embedding(word_size, 8, input_length = 4))
model.add(LSTM(32))
model.add(Dense(32, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))

model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
model.fit(padded_x, classes, epochs = 20, verbose = 1)

print('accuracy : %.4f'%(model.evaluate(padded_x, classes)[1]))