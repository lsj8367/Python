# 밀도기반 클러스터링 : 커브를 그리는 데이터의 경우 일부분은 KMeans로 제대로 군집화 할 수 없다.
# 이런 경우 DBSCAN 사용
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_moons
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN

x, y = make_moons(n_samples = 200, noise = 0.05, random_state = 0)
print(x)
print()
print(y)

plt.scatter(x[:, 0], x[:, 1])
plt.show()

# KMeans 로 군집분석 클러스터링
km = KMeans(n_clusters = 2, random_state = 0) # KMeans 객체 생성
pred1 = km.fit_predict(x)

# KMeans로 클러스터링된 분류 결과를 시각화
def plotKmeansFunc(x, y):
    plt.scatter(x[y == 0, 0], x[y == 0, 1], c = 'blue', marker = 'o', s = 40, label = 'cluster1')
    plt.scatter(x[y == 1, 0], x[y == 1, 1], c = 'red', marker = 's', s = 40, label = 'cluster2')
    plt.title('KMeans - Result')
    plt.legend()
    plt.show()

plotKmeansFunc(x, pred1) # 일부 군집에 문제가 있음을 알 수 있다. 완전분리 실패

print("\nDBSCAN을 사용 -------------")
dmodel = DBSCAN(eps = 0.2, min_samples = 5, metric = 'euclidean') # 반경 최소갯수 min_samples
pred2 = dmodel.fit_predict(x) # 학습과 예측 동시에
plotKmeansFunc(x, pred2)








