import pandas as pd
import numpy as np
# pandas 문제 3)  타이타닉 승객 데이터를 사용하여 아래의 물음에 답하시오.
#   데이터 : http://cafe.daum.net/flowlife/RUrO/103
#         https://github.com/pykwon/python/blob/master/testdata_utf8/titanic_data.csv
#     titanic_data.csv 파일을 다운로드 후
#    df = pd.read_csv('파일명',  header=None,,,)  
data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/titanic_data.csv')
print(data.iloc[:, 2:6])

# 1) 데이터프레임의 자료로 나이대(소년, 청년, 장년, 노년)에 대한 생존자수를 계산한다.
#       cut() 함수 사용
#      bins = [1, 20, 35, 60, 150]
#       labels = ["소년", "청년", "장년", "노년"]
#       df["age_cat"] = pd.cut(titanic["age"], bins, labels=labels)

bins = [1, 20, 35, 60, 150]
labels = ["소년", "청년", "장년", "노년"]
print(data.iloc[:,4:6])

data["bins"] = pd.cut(data["Age"], bins, labels=labels)
print(data['Age'].head(10))
a = data.groupby(['bins','Survived'])['Survived'].count()
#print(a)
print()
print(data['bins'].value_counts())
    
# 생존율======================================================================
  
#   2) 성별 및 선실에 대한 자료를 이용해서 생존여부(Survived)에 대한 생존율을 피봇테이블 형태로 작성한다. 
'''
df.pivot_table()
출력 결과 샘플 :       
pclass    1    2    3
sex            
female    0.968085    0.921053    0.500000
male    0.368852    0.157407    0.135447
'''
print(data.pivot_table(values=['Survived'],index=['Sex'], columns=['Pclass']))

print()

# index에는 성별(Sex) 및 나이(Age)를 사용하고, column에는 선실(Pclass) 인덱스를 사용한다.
#  출력 결과 샘플2 :   
#  위 결과물에 
#  Age 만 추가. 백분율로 표시. 소수 둘째자리까지.    예: 92.86
# .dropna(how = 'any')
redata = data.pivot_table(values=['Survived'], index=['Sex', 'bins'], columns=['Pclass'], fill_value= 0 * 100)
#print(round(redata * 100, 2))
pd.options.display.float_format = '{:.2f}'.format
redata = redata * 100
print(redata)
print()

pd.set_option('display.float_format', None) # 원래대로 소수점 되돌리기

# pandas 문제 4)
#  https://github.com/pykwon/python/tree/master/testdata_utf8
#  1) human.csv 파일을 읽어 아래와 같이 처리하시오.
#      - Group이 NA인 행은 삭제
#      - Career, Score 칼럼을 추출하여 데이터프레임을 작성
#      - Career, Score 칼럼의 평균계산

data2 = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/human.csv')
data2 = data2.rename(columns = lambda x: x.strip())
data2['Group'] = data2['Group'].str.strip()
print(data2.columns) # skipinitialspace = True 공백있으면 이것을 read_csv에 추가할것.
print()
data2['Group'] = data2['Group'].replace('NA', np.nan) # NA를 nan으로 바꾸기
data2 = data2.dropna(how = 'any')
print(data2)
print()
newlist = data2.iloc[:,[2,3]]
print(newlist)
print(newlist.mean())
print()

#  2) tips.csv 파일을 읽어 아래와 같이 처리하시오.
#      - 파일 정보 확인
#      - 앞에서 3개의 행만 출력
#      - 요약 통계량 보기
#      - 흡연자, 비흡연자 수를 계산  : value_counts()
#      - 요일을 가진 칼럼의 유일한 값 출력  : unique()

data3 = pd.read_csv('testdata/tips.csv')
print(data3.info())

print(data3.head(3))
print(data3.describe())
print()

print(data3['smoker'].value_counts())
print(data3['day'].unique())