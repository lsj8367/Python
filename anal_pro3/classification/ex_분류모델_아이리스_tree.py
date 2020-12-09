# 로지스틱 회귀 분류 모델 : iris dataset - 다항형 분류
from sklearn import datasets
from sklearn.linear_model import LogisticRegression # softmax 함수를 사용해서 다항 분류 가능
import numpy as np

from sklearn.model_selection._split import train_test_split
from sklearn.metrics import accuracy_score # 정확성
import pandas as pd
import pydotplus

iris = datasets.load_iris()
#print(iris.DESCR)
#print(iris.data)
#print(iris.target)
x = iris.data[:, [2, 3]] # 이것으로 진행해도 무방 #petal만 참여시킴
#x = iris.data # 전체데이터 전부 참여
y = iris.target
print(x[:3])
print(y[:3], set(y)) # 0:setosa, 1:versicolor, 2:verginica
# set으로 자료확인 왜 ? 중복 제거되니까

# train, test로 자료 분리 (7 : 3)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0) #random_state 난수 시드생성해서 난수 고정값
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) # (105, 4) (45, 4) (105,) (45,)

"""
# 스케일링 - 데이터 단위,크기를 일정하게 분포. 정규화(0 ~ 1 사이로 데이터를 분포), 표준화
print(x_train[:3])
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(x_train)
sc.fit(x_test)
x_train = sc.transform(x_train)
x_test = sc.transform(x_test)
print(x_train[:3]) # iris의 경우 데이터의 크기가 모두 일정하므로 스케일링할 필요없다.
"""

# LogisticRegression 분류 모델 사용
#ml = LogisticRegression(C = 1.0, random_state = 0) # C속성 : L2정규화에 의한 패널티 적용 - 오버피팅 방지

# SVC 분류모델 사용
# from sklearn import svm
# ml = svm.SVC(C = 1)

# GaussianNB 분류 모델 사용
# from sklearn.naive_bayes import GaussianNB
# ml = GaussianNB()

from sklearn.tree import DecisionTreeClassifier
ml = DecisionTreeClassifier(criterion = 'entropy', max_depth=5, random_state=0)

result = ml.fit(x_train, y_train) # 학습 진행
#print(result) # 학습 후

"""
# 모델을 학습시킨 후 모델 객체를 저장 후 불러다 사용----------------
import pickle
fileName = 'ex4model.sav'
# pickle.dump(ml, open(fileName, 'wb'))
ml = pickle.load(open(fileName, 'rb'))
# 학습내용을 저장해서 pickle로 불러옴 계속 모델을 작성해줄 필요가 없다.
# ------------------------------------------------
"""

# 분류 예측을 통한 모델 정확도 평가
y_pred = ml.predict(x_test)
print("예측 값 : ", y_pred)
print("실제 값 : ", y_test)

print("총 갯수:%d, 오류수:%d"%(len(y_test), (y_test != y_pred).sum()))
print("정확도1: %.3f"%accuracy_score(y_test, y_pred))

conf_mat = pd.crosstab(y_test, y_pred, rownames=['예측값'], colnames=['실제값'])
print(conf_mat)
print("정확도2: ", (conf_mat[0][0] + conf_mat[1][1] + conf_mat[2][2]) / len(y_test))
print("정확도3: ", ml.score(x_test, y_test))

# 사용자가 알고싶은 새로운 값으로 예측
#new_data = np.array([[1.1, 1.1, 1.1, 1.1], [6.1, 5.1, 4.1, 3.1]])
new_data = np.array([[1.1, 1.1], [6.1, 5.1]])
new_pred = ml.predict(new_data)
print("사용자가 알고 싶은 새로운 값으로의 예측 결과 : ", new_pred)   # [0 2] 전자는 setosa 후자는 verginica

# 시각화
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

plt.rc('font', family = 'malgun gothic')  #그래프에서 한글깨짐 방지용
plt.rcParams['axes.unicode_minus'] = False

def plot_decision_region(X, y, classifier, test_idx=None, resolution=0.02, title=''):
    markers = ('s', 'x', 'o', '^', 'v')  # 점표시 모양 5개 정의
    colors = ('r', 'b', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    #print('cmap : ', cmap.colors[0], cmap.colors[1], cmap.colors[2])

    # decision surface 그리기
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    xx, yy = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))
    # xx, yy를 ravel()를 이용해 1차원 배열로 만든 후 전치행렬로 변환하여 퍼셉트론 분류기의 

    # predict()의 안자로 입력하여 계산된 예측값을 Z로 둔다.
    Z = classifier.predict(np.array([xx.ravel(), yy.ravel()]).T)
    Z = Z.reshape(xx.shape) #Z를 reshape()을 이용해 원래 배열 모양으로 복원한다.

    # X를 xx, yy가 축인 그래프상에 cmap을 이용해 등고선을 그림
    plt.contourf(xx, yy, Z, alpha=0.5, cmap=cmap)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())

    X_test = X[test_idx, :]
    
    import itertools
    colors = itertools.cycle(["r", "b", "g"])
    
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y==cl, 0], y=X[y==cl, 1], c=next(colors), marker=markers[idx], label=cl)
        
    if test_idx:
        X_test = X[test_idx, :]
        plt.scatter(X_test[:, 0], X_test[:, 1], c=[], linewidth=1, marker='o', s=80, label='testset')

    plt.xlabel('표준화된 꽃잎 길이')
    plt.ylabel('표준화된 꽃잎 너비')
    plt.legend(loc=2)
    plt.title(title)
    plt.show()

x_combined_std = np.vstack((x_train, x_test))
y_combined = np.hstack((y_train, y_test))
plot_decision_region(X=x_combined_std, y=y_combined, classifier=ml, test_idx=range(105, 150), title='scikit-learn제공')

# GraphViz로 시각화
# import os
# os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
# from sklearn import tree
# from io import StringIO
# dot_data = StringIO() # 파일 흉내를 내는 역할
# tree.export_graphviz(ml, out_file = dot_data, feature_names = iris.feature_names[2:4])
# graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
# graph.write_png('iris_tree.png')

# 이미지 읽기
from matplotlib.pyplot import imread
img = imread('iris_tree.png')
plt.imshow(img)
plt.show()


