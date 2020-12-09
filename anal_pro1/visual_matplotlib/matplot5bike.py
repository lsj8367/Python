# kaggle dataset 중에서 자전거 공유 데이터로 시각화 연습
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot') #  R의 ggplot 스타일을 사용할것이다.
plt.rc('font', family = 'malgun gothic') # 한글 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False # 음수 부호 깨짐 방지

# 탐색적 분석(EDA)
train = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/data/train.csv",
                    parse_dates = ['datetime']) # object 타입 변경 datetime형식으로 읽기
print(train.shape)
print(train.columns)
print(train.info())
pd.set_option('display.max_columns', 500) # 생략없이 전체보기
print(train.head(3))
print(train.temp.describe()) # temp columns에 대한 요약 통계량
print(train.isnull().sum()) # null이 포함된 칼럼 조회
# null이 포함된 column 확인 시각화
# pip install missingno
# import missingno as msno
# msno.matrix(train, figsize=(12, 5))
# plt.show()

print(train['datetime'][0])
# datetime 칼럼 자료를 분리
train['year'] = train['datetime'].dt.year
train['month'] = train['datetime'].dt.month
train['day'] = train['datetime'].dt.day
train['hour'] = train['datetime'].dt.hour
train['minute'] = train['datetime'].dt.minute
train['second'] = train['datetime'].dt.second
print(train.columns)
print(train.head(2))
print(train.tail(2))
"""
# 대여량 시각화
figure,(ax1, ax2, ax3, ax4) = plt.subplots(nrows = 1, ncols = 4)
figure.set_size_inches(15, 5)  # 크기변경
sns.barplot(data = train, x = 'year', y = 'count', ax = ax1)
sns.barplot(data = train, x = 'month', y = 'count', ax = ax2)
sns.barplot(data = train, x = 'day', y = 'count', ax = ax3)
sns.barplot(data = train, x = 'hour', y = 'count', ax = ax4)
ax1.set(ylabel='Count', title = '연도별 대여량')
ax2.set(ylabel='Count', title = '월별 대여량')
ax3.set(ylabel='Count', title = '일별 대여량')
ax4.set(ylabel='Count', title = '시간별 대여량')
plt.show()
"""

"""
# boxplot 시각화
fig, axes = plt.subplots(nrows = 2, ncols = 2)
fig.set_size_inches(12, 10)
sns.boxplot(data = train, y = 'count', orient = 'v', ax = axes[0][0]) # orient는 방향
sns.boxplot(data = train, y = 'count', x = 'season', orient = 'v', ax = axes[0][1]) # orient는 방향
sns.boxplot(data = train, y = 'count', x = 'hour', orient = 'v', ax = axes[1][0]) # orient는 방향
sns.boxplot(data = train, y = 'count', x = 'workingday', orient = 'v', ax = axes[1][1]) # orient는 방향
axes[0][0].set(ylabel = 'Count', title = '대여량')
axes[0][1].set(ylabel = 'Count', xlabel = 'season', title = '계절별 대여량')
axes[1][0].set(ylabel = 'Count', xlabel = 'hour', title = '시간별 대여량')
axes[1][1].set(ylabel = 'Count', xlabel = 'workingday', title = '근무일에 따른 대여량')
plt.show()
"""
# 요일 칼럼 추가
train['dayofweek'] = train['datetime'].dt.dayofweek
#print(train['dayofweek'])
print(train['dayofweek'].value_counts())

"""
# pointplot
fig, (ax1, ax2) = plt.subplots(ncols = 2)
fig.set_size_inches(15, 20)
sns.pointplot(data = train, x = 'hour', y = 'count', ax = ax1)
sns.pointplot(data = train, x = 'hour', y = 'count', hue = 'dayofweek', ax = ax2)
plt.show()
"""

# 산점도 : regplot
fig, (ax1, ax2, ax3) = plt.subplots(ncols = 3)
fig.set_size_inches(10, 10)
sns.regplot(x = 'temp', y = 'count', data = train, ax = ax1)
sns.regplot(x = 'windspeed', y = 'count', data = train, ax = ax2)
sns.regplot(x = 'humidity', y = 'count', data = train, ax = ax3)
plt.show()


