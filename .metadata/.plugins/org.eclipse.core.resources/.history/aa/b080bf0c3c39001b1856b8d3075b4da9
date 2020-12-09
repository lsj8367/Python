# 뉴스문서를 읽어 형태소 분석 후 파일로 저장. 단어별 유사도 출력
import pandas as pd
from konlpy.tag import Okt

okt = Okt()

with open('daumnews.txt', mode = 'r', encoding = 'utf-8') as f:
    #print(f.read())
    lines = f.read().split('\n') #줄바꿈 기준
    #print(len(lines)) # 34

wordDic = {}

for line in lines:
    datas = okt.pos(line) # 단어의 품사 태깅
    #print(datas)
    for word in datas:
        if word[1] == 'Noun': # 명사만 작업에 참여
            #print(word[0])
            #print(word[0] in wordDic)
            if not(word[0] in wordDic): # dict안에 word 단어가 없다면 0
                wordDic[word[0]] = 0
            wordDic[word[0]] += 1 # 있으면 1씩 누적

#print(wordDic) # {'오늘': 7, '대중교통': 6, '음식점': 1, '등': 15, '다중': 11, '이용': 12, '시설': 11, '마스크': 59, '안': 2, '최대': 1, '원': 1...
# 건수별 내림차순 정렬
keys = sorted(wordDic.items(), key = lambda x:x[1], reverse=True)
print(keys)

# DataFrame에 단어와 건수 담기
wordList = []
countList = []

for word, count in keys[:20]: # 건수 상위 20개
    wordList.append(word)
    countList.append(count)
    
df = pd.DataFrame()
df['word'] = wordList
df['count'] = countList
print(df)

print('---' * 20)
results = []

with open('daumnews.txt', mode = 'r', encoding = 'utf-8') as f:
    lines = f.read().split('\n') #줄바꿈 기준
    
    for line in lines:
        datas = okt.pos(line, stem = True)
        print(datas)
        imsi = []
        for word in datas:
            if not word[1] in ['Verb','Conjunction', 'Josa', 'Number', 'Suffix', 'Punctuation', 'Adjective', 'Modifier', 'Alpha', 'Determiner']: # 제외할 항목
                imsi.append(word[0])
        imsi2 = (" ".join(imsi)).strip() # strip 앞뒤공백 제거
        results.append(imsi2)
        
print(results)
fileName = 'daumnews2.txt'
with open(fileName, mode = 'w', encoding = 'utf-8') as fw:
    fw.write('\n'.join(results))
    print("저장 성공")


print('\n워드임베딩 -단어를 수치화하여 벡터로 기억 - 단어/문장 간 관련성(유사도) 계산, 전이학습...')
# One-hot encoding : 단어를 인덱싱하여 희소벡터화시킴
# Word2vec : 문맥이 유사한 단어를 비슷한 벡터로 표현
# pip install gemsim

from gensim.models import word2vec
import pandas as pd
import numpy as np

# 간단한 예
one_sentence = ['python', 'lan', 'program', 'computer', 'say']
print(one_sentence)

# One-hot encoding

values = []
for x in range(len(one_sentence)):
    values.append(x)
print(values) # [0, 1, 2, 3, 4]
values_len = len(values)

one_encoding = np.eye(values_len)[values]
print(one_encoding)

# Word2Vec 처리
sentence = [['python', 'lan', 'program', 'computer', 'say']]
model = word2vec.Word2Vec(sentence, min_count = 1, size = 50) #min_count : 단어 최소빈도수, size 배열크기,
print(model.wv) # <gensim.models.keyedvectors.Word2VecKeyedVectors object at 0x0000016AC93152E0>
word_vectors = model.wv
print('model.wv.vocab : ', word_vectors.vocab) # Vocab object
vocabs = word_vectors.vocab.keys()
print('vocabs :', vocabs)
vocab_val = word_vectors.vocab.values()
print('vocab_val :', vocab_val)
 
word_vectors_list = [word_vectors[v] for v in vocabs]
print(word_vectors_list)
print(word_vectors_list[0], ' ', len(word_vectors_list[0])) # 절대값이 1에 가까우면 단어끼리의 연관성이 짙음
print(len(word_vectors_list))
print(word_vectors.similarity(w1='lan', w2 = 'program')) # 유사도 0.09404077 계속 바뀜

print(model.wv.most_similar('lan')) # lan과 나머지단어들간의 유사도
print(model.wv.most_similar('python'))

print()
# daumnews.txt 파일 자료를 읽어 단어간 유사도 파악
getObj = word2vec.LineSentence(fileName)
print(getObj)  # <gensim.models.word2vec.LineSentence object at 0x00000230A833DB50>

#분석 방법론 - 단어의 빈도수 이용
# CBOW : 주변단어로 중심단어를 예측하는 법   ex) 나는 ~ 간다 앞뒤로 가운데를 예측, 주변단어를 몇개 하느냐가 window값 mincount로 1글자짜리는 제외함 2글자부터
# Skip-Gram : 중심단어로 주면단어를 예측하는 법   ex) ~ 외나무 다리 ~ 가운데 로 앞뒤를 예측
model = word2vec.Word2Vec(getObj, size=100, window=10, min_count=2, sg=1) # sg1 = Skip-Gram sg0 = CBOW
print(model) # Word2Vec(vocab=95, size=100, alpha=0.025)

model.init_sims(replace=True) # 필요없는 메모리 해제

# 학습된 모델을 저장 후 재 사용
# 학습이 완료되서 아래를 진행하게되면 위의 과정은 필요가 없게된다 왜? 이미 학습시켰으니까
try:
    model.save('news.model')
except Exception as e:
    print("err : ", str(e))

# 모델 읽기
model = word2vec.Word2Vec.load('news.model')
print(model.wv.most_similar(positive = ['마스크'])) # positive : 단어사전에 단어가 있을 확률
print(model.wv.most_similar(positive = ['마스크'], topn=3))
print(model.wv.most_similar(positive = ['마스크', '흡연'], negative=['물']))





