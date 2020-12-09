# 비지도학습 중 변수 얻기 - 요인분석과 주성분분석
# 선택(selection) ex : 국, 영, 수 중에서 국,영만 선택
# 추출(extraction) ex : 국어,영어를 합쳐 어학이라는 새로운 변수를 생성
# 통한 차원축소(변수의 개수를 줄이는 작업)

# 주성분분석 연습 - iris dataset
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_iris
plt.rc('font', family = 'malgun gothic')

iris = load_iris()
n = 10
x = iris.data[:n, :2] # sepal:length, width 
print('차원 축소 전:', x, x.shape, type(x))
print(x.T)

# 시각화
'''
plt.plot(x.T, 'o:')
plt.xticks(range(4), ['꽃받침 길이', '꽃받침 폭'])
plt.xlim(-0.5, 2)
plt.ylim(2.5, 6)
plt.title('iris 크기 특성')
plt.legend(['표본{}'.format(i + 1) for i in range(n)])
plt.show()
'''
# 산점도
ax = sns.scatterplot(0, 1, data = pd.DataFrame(x), s = 100, color='.2', marker='s') # s = scale
for i in range(n):
    ax.text(x[i, 0] - 0.05, x[i, 1] + 0.03, '표본{}'.format(i + 1))

plt.xlabel('꽃받침 길이')
plt.ylabel('꽃받침 폭')
plt.title('붓꽃 칼럼 특성')
plt.axis('equal')
plt.show() # 꽃받침의 길이와 폭이 일정하게 공통적으로 변화하고 있어, 차원축소의 근거가 있다고 볼 수 있다.

# PCA 기능 구현
pca1 = PCA(n_components = 1)
x_low = pca1.fit_transform(x)
print('x_low: ', x_low, ' ', x_low.shape) # (10, 1) 두개의 요소가 1개의 요소값으로 근사된 데이터의 집합 (길이~폭)
# [[ 0.30270263] ...
x2 = pca1.inverse_transform(x_low) # 1개의 요소값으로 근사된 데이터를 원래대로 복구
print('차원복귀 후 :',x2, x2.shape, type(x2))
# [[5.06676112 3.53108532] ...
print(x_low[0], ' ', x2[0])

# 시각화
sns.scatterplot(0, 1, data = pd.DataFrame(x), s = 100, color = '.2', marker = 's')
for i in range(n):
    d = 0.03 if x[i, 1] > x2[i, 1] else -0.04
    ax.text(x[i, 0] - 0.065, x[i, 1] + d, '표본{}'.format(i + 1))
    plt.plot([x[i, 0], x2[i, 0]], [x[i, 1], x2[i, 1]], 'k--')

plt.plot(x2[:,0], x2[:, 1], 'o-', color='b', markersize = 10)
plt.plot(x[:, 0].mean(), x[:, 1].mean(), markersize = 10, marker = 'D')
plt.axvline(x[:, 0].mean(), c = 'r') # 세로선 긋기
plt.axhline(x[:, 1].mean(), c = 'r') # 가로선 긋기
plt.xlabel('꽃받침 길이')
plt.ylabel('꽃받침 폭')
plt.title('붓꽃 데이터 차원 축소')
plt.axis('equal')
plt.show()
    
print('***' * 10) # sepal, petal 모두 참여
x = iris.data
pca2 = PCA(n_components = 2)
x_low2 = pca2.fit_transform(x) # feature만 있음. 
print('x_low2: ', x_low2, ' ', x_low2.shape)

x4 = pca2.inverse_transform(x_low2)
print()
print("최초 자료 : ", x[0])
print("차원 축소 : ", x_low2[0])
print("차원 복귀 : ", x4[0, :])

print()
iris2 = pd.DataFrame(x_low2, columns = ['sepal', 'petal'])
iris1 = pd.DataFrame(x, columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])

print(iris2.head(5)) # 차원축소 데이터
print()
print(iris1.head(5)) # 최초데이터
