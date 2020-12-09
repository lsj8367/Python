# 주요 차트의 종류
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn
plt.rc('font', family = 'malgun gothic') # 한글 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False # 음수 부호 깨짐 방지
"""
fig = plt.figure() # 명시적으로 차트 영역 선언
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

# 히스토그램
ax1.hist(np.random.rand(10), bins = 15, alpha = 0.9) # 히스토그램 alpha는 투명도, bins은 구간
ax2.plot(np.random.rand(10))
plt.show()
"""

data = [50, 80, 100, 70, 90]
print(type(data))
"""
# 막대그래프
plt.bar(range(len(data)), data) # 구간, 값 세로막대
plt.show()

error = np.random.randn((len(data)))
plt.barh(range(len(data)), data, alpha = 0.5, xerr = error) # 가로막대 , xerr = error 에러막대(오차막대) 표시가능
plt.show()
"""

"""
plt.pie(data, explode=(0, 0.1, 0, 0, 0), colors = ['yellow', 'red', 'blue'])
plt.title('원형 차트')
plt.show()

plt.boxplot(data)
plt.show()
"""
"""
# 버블차트 : 산점도 차트에 점의 크기를 동적으로 표시
n = 30
np.random.seed(0) # 난수값 고정
x = np.random.randn(n) # 정규 분포를 따르는 난수
y = np.random.randn(n)
color = np.random.randn(n)
scale = np.pi * (15 * np.random.rand(n)) ** 2
plt.scatter(x, y, c = color, s = scale)
plt.show()
"""

"""
# Series 자료로 차트
from pandas import Series
sdata = Series(np.random.randn(10).cumsum(), index = np.arange(0, 100, 10))
plt.plot(sdata)
plt.show()
"""
"""
# 시계열 자료 차트로 출력
import pandas as pd
fdata = pd.DataFrame(np.random.randn(1000, 4), index = pd.date_range('1/1/2000', periods = 1000), columns = list('abcd')) # abcd 구간으로 나눔, 1000행 4열
#print(fdata)
fdata = fdata.cumsum()
print(fdata.head())
plt.plot(fdata)
plt.show()
"""

print('matplotlib의 기능 보강용 모듈중 seaborn모듈=====')
import seaborn as sns
titanic = sns.load_dataset('titanic') # seaborn이 제공하는 dataset 중 일종
print(titanic.info())

#sns.distplot(titanic['age']) # hist는 distplot
#sns.boxplot(y='age', data = titanic, palette = 'Paired')
#sns.relplot(x = 'who', y = 'age', data = titanic)
#sns.countplot(x = 'class', data = titanic, hue = 'who') # hue는 카테고리변수
titanic_pivot = titanic.pivot_table(index = 'class', columns = 'sex', aggfunc = 'size')
print(titanic_pivot)
sns.heatmap(titanic_pivot, cmap = sns.light_palette('gray', as_cmap = True), annot = True, fmt = 'd') # fmt 데시말
plt.show()
