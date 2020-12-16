# -*- coding: utf-8 -*-
"""tfrnn9네이버영화분류.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VJpcudxbYgxXQtBCu92vejZEXurNs0Ij
"""

# 네이버 영화 리뷰 감성분류
import pandas as pd
import matplotlib.pyplot as plt
! pip install konlpy
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

train_data = pd.read_table('https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt')
test_data = pd.read_table('https://raw.githubusercontent.com/e9t/nsmc/master/ratings_test.txt')
print(train_data.head(2), len(train_data)) # 150000
print(test_data.head(2), len(test_data))   # 50000

print(train_data['document'].nunique(), train_data['label'].nunique()) # 146182 2 document에 중복자료 있음.
train_data.drop_duplicates(subset = ['document'], inplace = True) # document의 중복 제거

# 급부정 데이터 시각화
train_data['label'].value_counts().plot(kind='bar')
plt.show()

print(train_data.groupby('label').size().reset_index(name = 'count'))

# null 여부
print(train_data.isnull().values.any()) # True 결측값 있음
print(train_data.isnull().sum()) # 결측값 document    1
print(train_data.loc[train_data.document.isnull()]) # 25857  2172111      NaN      1

train_data = train_data.dropna(how = 'any')
print(train_data.isnull().values.any())
print(len(train_data))

# 특수문자 제거 : 정규 표현식
import re
# ss = '한국abcKbs good 123 !@#$%^&'
# print(re.sub(r'[^a-zA-Z]', '', ss)) # 영문빼고 다 지움
# 한글 : 자음 ㄱ ~ ㅎ, 모음 ㅏ ~ ㅣ, 완성형 : 가 ~ 힣
train_data['document'] = train_data['document'].str.replace('[^ㄱ-ㅎㅏ-ㅣ가-힣]', '')
print(train_data[:3])
train_data['document'].replace('', np.nan, inplace = True) # 공백을 nan처리
print(train_data.isnull().sum()) # nan값 생김

train_data = train_data.dropna(how = 'any')
print(len(train_data))

# test data
test_data.drop_duplicates(subset=['document'], inplace = True)
test_data['document'] = test_data['document'].str.replace('[^ㄱ-ㅎㅏ-ㅣ가-힣]', '')
test_data['document'].replace('', np.nan, inplace = True)
test_data = test_data.dropna(how = 'any')
print(len(test_data))

# 불용어(Stop word)는 분석에 큰 의미가 없는 단어
stopwords = ['의', '이', '가', '은', '는', '을','들', '도', '으로', '에', '한', '와', '하다']

# 형태소 분석
okt = Okt()
x_train = []
for sen in train_data['document']:
    temp_x = []
    temp_x = okt.morphs(sen, stem=True)
    temp_x = [word for word in temp_x if not word in stopwords] # 불용어제거
    x_train.append(temp_x)

print(x_train[:3])

x_test = []
for sen in test_data['document']:
    temp_x = []
    temp_x = okt.morphs(sen, stem=True)
    temp_x = [word for word in temp_x if not word in stopwords] # 불용어제거
    x_test.append(temp_x)
    
print(x_test[:3])

# Token 처리
tokenizer = Tokenizer()
tokenizer.fit_on_texts(x_train)
print(tokenizer.word_index)