import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

data = pd.read_csv('test.csv', encoding='utf8')
data.columns = ['문장']
data = data.dropna()
print(data.head(5))

count_vec = CountVectorizer(analyzer='word', min_df = 1) # analyzer = 'char' 똑같음
print(count_vec)
aa = count_vec.fit_transform(data['문장'])
print(aa) # 구두점 빠지고 영어는 전부 소문자로 바뀜.
print(count_vec.get_feature_names())
print(aa.toarray())
