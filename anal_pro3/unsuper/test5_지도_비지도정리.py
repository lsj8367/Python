# iris 데이터로 지도 / 비지도 학습 간단 정리
from sklearn.datasets import load_iris

iris_dataset = load_iris()

print(iris_dataset['data'][:3]) # [[5.1 3.5 1.4 0.2] ...
print(iris_dataset['feature_names']) # ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
print(iris_dataset['target'][:3]) # 0 1 2
print(iris_dataset['target_names']) # ['setosa' 'versicolor' 'virginica']

from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(iris_dataset['data'], iris_dataset['target'], test_size = 0.25, random_state = 42)
print(train_x.shape, test_x.shape) # (112, 4) (38, 4)

print('-지도학습 : K-NN----------')
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
knnModel = KNeighborsClassifier(n_neighbors = 3)
knnModel.fit(train_x, train_y) # feature, label
predict_label = knnModel.predict(test_x)
print(predict_label)
print("분류 정확도 : ", np.mean(predict_label == test_y))

new_input = np.array([[6.6, 2.8, 4.7, 1.2]])
print(knnModel.predict(new_input)) # [1] ===> versicolor
print(knnModel.predict_proba(new_input)) # [[0. 1. 0.]] 셋중의 가운데가 1이므로 versicolor

print()
dist, index = knnModel.kneighbors(new_input)
print('dist :', dist)
print('index : ', index)

print('\n비지도학습 : KMeans==========')
from sklearn.cluster import KMeans
kmeansModel = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
kmeansModel.fit(train_x) # label은 주어지지 않음
print(kmeansModel)

print(kmeansModel.labels_) # 0이면 0번째 군집에 속함

print('0 cluster:', train_y[kmeansModel.labels_ == 0]) # 0번째 군집은 라벨 1인 데이터가 많이 분포
print('1 cluster:', train_y[kmeansModel.labels_ == 1]) # 1번째 군집은 라벨 0(setosa)인 데이터가 주로 분포
print('2 cluster:', train_y[kmeansModel.labels_ == 2]) # 2번째 군집은 라벨 2인 데이터가 주로 분포
new_input = np.array([[6.6, 2.8, 4.7, 1.2]])
clu_pred = kmeansModel.predict(new_input)
print(clu_pred)

print()
predict_cluster = kmeansModel.predict(test_x)
print(predict_cluster)

np_arr = np.array(predict_cluster)
print(np_arr)
np_arr[np_arr == 0], np_arr[np_arr == 1], np_arr[np_arr == 2] = 3, 4, 5 # 0,1,2 값을 각각 3,4,5로 치환
print(np_arr)
np_arr[np_arr == 3] = 1 # 군집3을 1(versicolor)로 변경
np_arr[np_arr == 4] = 0 # 군집3을 1(setosa)로 변경
np_arr[np_arr == 5] = 2 # 군집3을 1(verginica)로 변경

print(np_arr)

predict_label = np_arr.tolist()
print(predict_label)

print('test accuracy: {:.2f}'.format(np.mean(predict_label == test_y))) # 0.95
