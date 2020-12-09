import pandas as pd

'''
pandas 문제 3)  타이타닉 승객 데이터를 사용하여 아래의 물음에 답하시오.
  데이터 : http://cafe.daum.net/flowlife/RUrO/103
        https://github.com/pykwon/python/blob/master/testdata_utf8/titanic_data.csv
        titanic_data.csv 파일을 다운로드 후

 1) 성별, 선실(class or pclass), 나이대(소년, 청년, 장년, 노년)에 의한 생존율을 데이터프레임을 사용해 계산한다.
     행에는 성별 및 나이에 대한 계층적 인덱스(pd.cut())를 사용하고, 열에는 선실 인덱스를 사용한다.

  2) 성별 및 선실에 대한 자료를 이용해서 생존율('survived')을 피봇테이블 형태로 작성한다. 
      df.pivot_table()
'''

titanic = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/titanic_data.csv')
df = pd.DataFrame(titanic)
print(df.head(3))

bins = [1, 20, 35, 60, 150]
labels = ["소년", "청년", "장년", "노년"]
df["age_cat"] = pd.cut(titanic["Age"], bins, labels=labels)  # 칼람 추가

print('\n3-1) 나이대에 대한 생존자수 계산 ---------------------\n')
print(df['age_cat'].value_counts())

print('\n3-2) pivot_table 사용--------------------\n')
print(round(df.pivot_table(values=['Survived'], index = ['Sex'], 
                           columns=['Pclass'], fill_value = 0) * 100, 3))

# df_n = df.pivot_table(values=['Survived'], index = ['Sex'], 
#                             columns=['Pclass'], fill_value = 0)
# print(round(df_n * 100, 2))

print()
print(round(df.pivot_table(values=['Survived'], index = ['Sex', 'Age'], \
                           columns=['Pclass'], fill_value = 0)) * 100, 3)

'''
pandas 문제 4)
 https://github.com/pykwon/python/tree/master/testdata_utf8
 1) human.csv 파일을 읽어 아래와 같이 처리하시오.
 2) tips.csv 파일을 읽어 아래와 같이 처리하시오.
'''
human = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/human.csv',
                     skipinitialspace=True)
df = pd.DataFrame(human)

# human = human.rename(columns=lambda x: x.strip())
# human['Group'] = human['Group'].str.strip()

print(df)
print('4-1)')
print('\n-----Group이 NA인 행은 삭제\n', df.dropna(subset=['Group']))
#human = human[human['Group'] != 'NA']

df2 = pd.DataFrame(df, columns= ['Career', 'Score'])    # df[df.columns[2:4]]
print('\n-----Career, Score 칼럼을 추출하여 데이터프레임을 작성\n', df2)
print('\n-----Career, Score 칼럼의 평균계산\n', df2.mean(axis=0))

print('\n4-2)')
tips = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/tips.csv')
df = pd.DataFrame(tips)
print('\n-----파일 정보 확인\n', df.info())
print('\n-----앞에서 3개의 행만 출력\n',df.iloc[:3, ])  # df.head(3)
print('\n-----요약 통계량 보기\n', df.describe())
print('\n-----흡연자, 비흡연자 수를 계산\n', df['smoker'].value_counts())
print('\n-----요일을 가진 칼럼의 유일한 값 출력\n', df['day'].unique())  # pd.unique(df['day'])
