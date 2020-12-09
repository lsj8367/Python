# BOW -> bag of word : 단어의 빈도수를 부여해 feature vector를 만들어 빈도 수 저장
# 한글 어간 추출 : '봄은', '봄과', '봄이' => '봄' 으로 통일
import numpy as np
from konlpy.tag import Okt

str_data = np.array(['봄은', '봄과', '봄이'])

# 텍스트 정제 - 형태소 추출
my_words = []
okt = Okt()
for i, doc in enumerate(str_data):
    for word in okt.pos(doc, stem = True): # 한글자씩 출력
        #print(word)
        if word[1] in ['Noun']:
            my_words.append(word[0])
print(my_words)

print('\n -----------------------------')
content = ['How to format my hard disk.', 'Hard disk format format problems.']
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
# CountVectorizer : 단어 토큰을 생성해 각 단어의 수를 세어 BOW 벡터를 생성, 띄어쓰기 기준
# TfidfVectorizer : 단어의 가중치를 조정한 BOW 벡터를 생성, 띄어쓰기 기준

# 방법1) CountVectorizer
count_vec = CountVectorizer(analyzer='word', min_df = 1) # analyzer = 'char' 똑같음
print(count_vec)

aa = count_vec.fit_transform(content)
print(aa) # 구두점 빠지고 영어는 전부 소문자로 바뀜.
print(count_vec.get_feature_names())
print(aa.toarray())

print('----------------------------')
# 방법2) CountVectorizer
tfidf_vec = TfidfVectorizer(analyzer='word', min_df = 1)
print(tfidf_vec)
bb = tfidf_vec.fit_transform(content)
print(bb)
print(tfidf_vec.get_feature_names())
print(bb.toarray())

print('\n\n한글 데이터로 CountVectorizer ---------------')
text_data = ['나는 배 고프다 아니 배가 고프다.', '내일 점심 뭐 먹지', '내일 공부 해야겠다']
count_vec = CountVectorizer()
#count_vec = CountVectorizer(analyzer='word', min_df = 1, ngram_range = (1, 1)) # ngram 몇글자씩 묶는지여부
#count_vec = CountVectorizer(analyzer='word', ngram_range = (3, 3))

#count_vec = CountVectorizer(stop_words = ['나는', '해야지']) # 불용어 등록(들어간 단어 빠짐)
#count_vec = CountVectorizer(min_df = 1, max_df = 5) # 빈도수가 최소1번 최대 5번

count_vec.fit(text_data)
print(count_vec.get_feature_names()) # 가나다순 ['고프다', '공부', '나는', '내일'
print(count_vec.vocabulary_) # {'나는': 2, '고프다': 0,  사전순 인덱싱 키 : 문자, 밸류 : 열

print(text_data[0])
sentence = [text_data[0]]
print(count_vec.transform(sentence))
print(count_vec.transform(sentence).toarray())

new_sentence = ['나는 공부 이건 점심 먹고 공부 해야 배가 부르다 라고 느낀다']
print(count_vec.transform(new_sentence).toarray())
print(count_vec.transform(new_sentence).toarray().sum(axis = 1))
# 횟수를 사용해 벡터를 만듦으로 해서 직관적으로 파악.
# 중복이 많은 경우 문제 있음. 위의 경우 의미가 없는 단어가 작업에 참여하므로 어간 추출이 필요함

my_words = []
for i, doc in enumerate(text_data):
    for word in okt.pos(doc, stem = True): # 한글자씩 출력
        #print(word)
        if word[1] in ['Noun', 'Adjective', 'Verb']:
            my_words.append(word[0])
print(my_words)
count_vec.fit(my_words)
print(count_vec.transform(my_words).toarray())

print('\n\n한글 데이터로 CountVectorizer ---------------')
text_data = ['나는 배 고프다 아니 배가 고프다.', '내일 점심 뭐 먹지', '내일 공부 해야겠다', '점심 먹고 공부 해야지.']
tfidf_vectorizer = TfidfVectorizer()
tfidf_vectorizer.fit(text_data)
print(tfidf_vectorizer.get_feature_names())
print(tfidf_vectorizer.vocabulary_)
print()
print(tfidf_vectorizer.transform(text_data).toarray())

sentence = [text_data[3]] # 점심먹고 공부해야지
print(tfidf_vectorizer.transform(sentence))
print(tfidf_vectorizer.transform(sentence).toarray())
# 1(공부), 8(점심)번째 단어가 0.437 정도의 값을 가짐
# 4(먹고), 10(해야지)번째 단어가 0.5552 정도의 값을 가짐