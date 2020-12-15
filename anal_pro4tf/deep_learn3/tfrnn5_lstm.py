# 뉴욕타임즈 기사 자료로 텍스트 생성 연습
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/articlesapril.csv')
print(df.head(5))

# print(df.count()) 1324행 x 15열
# print(df.columns)
# ['articleID', 'articleWordCount', 'byline', 'documentType', 'headline',
#        'keywords', 'multimedia', 'newDesk', 'printPage', 'pubDate',
#        'sectionName', 'snippet', 'source', 'typeOfMaterial', 'webURL']

# print(df['headline'].head(5))
print(df['headline'].isnull().values.any()) # False

# headline 열에서 기사제목을 추출
headline = []
headline.extend(list(df.headline.values))
print(headline[:10]) # 'Unknown' 발견 - 제거대상
print(len(headline)) # 1324
headline = [n for n in headline if n != 'Unknown'] # unknown이 아닌것만 추출
print(len(headline)) # 1214
print(headline[:10])

print("He하이ello 가a나다".encode("ascii", errors = 'ignore').decode())
from string import punctuation
print(", Python".strip(punctuation)) # ,와. 제거 공백제거 안됨
print(", Python".strip(punctuation + ' ')) # 공백까지 제거됨

def repre_func(ss):
    ss = ss.encode("utf8").decode('ascii', errors = 'ignore')
    #print(ss)
    return ''.join(c for c in ss if c not in punctuation).lower() # 구두점 제거 + 소문자화

#print(repre_func('Former 대한민국N.F.L. Cheerleaders')) # former nfl cheerleaders
text = [repre_func(hd) for hd in headline]
print(text) #  ['former nfl cheerleaders settlement offer 1 and a meeting with goodell', ...

# 단어 집합(vocabulary) 생성
from keras_preprocessing.text import Tokenizer
tok = Tokenizer()
tok.fit_on_texts(text)

print(tok.word_index)
vocab_size = len(tok.word_index) + 1
print('단어 집합의 크기 : %d'%vocab_size) # 3494

# train data의 형태
sequences = list()
for line in text:
    enc = tok.texts_to_sequences([line])[0] # 각샘플에 대한 정수 인코딩
    for i in range(1, len(enc)):
        se = enc[:i + 1]
        sequences.append(se) # [[99, 269], [99, 269, 371], ...]
print(sequences[:11])
# former = 99, nfl = 269, cheerleaders = 371 ...

print('dict items : ', tok.word_index.items()) #  dict_items([('the', 1), ('a', 2) ...
index_to_word = {}
for key, value in tok.word_index.items():
    index_to_word[value] = key # 키와 밸류를 바꿈
print(index_to_word)
print(index_to_word[1]) # the
print(index_to_word[600]) # panel

max_len = max(len(i) for i in sequences)
print(max_len)

from tensorflow.keras.preprocessing.sequence import pad_sequences
sequences = pad_sequences(sequences, maxlen = max_len, padding = 'pre')
print(sequences[:3])

import numpy as np
sequences = np.array(sequences)
x = sequences[:, :-1] # feature
y = sequences[:, -1] # label

print(x[:3])
print(y[:3])