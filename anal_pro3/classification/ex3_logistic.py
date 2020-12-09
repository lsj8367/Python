# softmax 활성화 함수
# Softmax(소프트맥스)는 입력받은 값을 출력으로 0~1사이의 값으로 모두 정규화하며 출력 값들의 총합은 항상 1이 되는 특성을 가진 함수이다.
import numpy as np
import matplotlib.pyplot as plt
"""
def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()
 
x = np.array([3.4,2.0,1.8])
 
y = softmax(x)
print(y)
print(np.sum(y))

ratio = y
labels = y
 
plt.pie(ratio, labels=labels, shadow=True, startangle=90)
plt.show()
"""
from sklearn import datasets
from sklearn.linear_model import LogisticRegression # softmax 함수를 사용해서 다항 분류 가능

iris = datasets.load_iris()
#print(iris.DESCR)
print(iris.keys())
print(iris.target)
x = iris['data'][:, [3]] # 꽃잎너비 칼럼만 사용
print(x[:10])
y = (iris['target'] == 2).astype(np.int) # 값이 2인것만 True여서 1로 바꾸고 나머지는 0 # setosa + versicolor
print(y)

log_reg = LogisticRegression()
print(log_reg)

log_reg.fit(x, y) # 학습

x_new = np.linspace(0, 3, 1000).reshape(-1, 1) # 난수발생 0부터3까지 1000개  reshape -1은 행의갯수 자동결정, 1열
print(x_new.shape) # (1000, 1)
y_proba = log_reg.predict_proba(x_new) # x에대한 예측 확률 값을 출력
#print(y_proba) # [[9.99250016e-01 7.49984089e-04] ...

plt.plot(x_new, y_proba[:, 1], 'r-', label = 'virginica') # 빨간실선
plt.plot(x_new, y_proba[:, 0], 'b--', label = 'not virginica') # 파란점선
plt.xlabel("Petal_Width")
plt.legend()
plt.show()

print()
print(log_reg.predict([[1.5], [1.7]])) # [0 1] not virginica / virginica
print(log_reg.predict([[2.5], [0.7]])) # [1 0] virginica / not virginica
print(log_reg.predict_proba([[2.5], [0.7]])) # 확률값으로 확인

