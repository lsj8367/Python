# 분류모델 평가 : ROC(Receiver Operating Characteristic) Curve
from sklearn.datasets import make_classification # 분류연습하기 좋은 난수 제공
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd

x, y = make_classification(n_samples = 16, n_features = 2, n_informative = 2, n_redundant = 0, random_state = 0) # 독립변수 2개, 표본데이터 수 16개, 종속변수와 상관이있는 수(informative)
print(x)
print(y) # 실제값

# train, test 나누기 생략
model = LogisticRegression().fit(x, y)
y_hat = model.predict(x) # 예측값
print("y_hat: ", y_hat) # 예측값
f_value = model.decision_function(x) # 결정함수 예측값, ROC 커브의 판별 경계선
print()
df = pd.DataFrame(np.vstack([f_value, y_hat, y]).T, columns = ['f' , 'y_hat', 'y'])
print(df.head(3))
df.sort_values("f", ascending = False).reset_index(drop = True)

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y, y_hat, labels = [1, 0]))

# TP / (TP + FN)  # 실제값이 참값인것들 중에서 예측값도 참이라 분류한 값을 실제값 참데이터로 나눈값
recall = 7 / (7 + 1)

# fallout (위양성율)   FP / (FP + TN) : FPR   # 실제값이 참인데 예측값이 거짓인경우 / (실제값이 참인데 예측값이 거짓인경우 + 실제와 예측 둘다 거짓인경우)
fallout = 1 / (1 + 7)
print('recall : ', recall)
print('fallout : ', fallout)

from sklearn.metrics import roc_curve

fpr, tpr, thresholds = roc_curve(y, model.decision_function(x))
print('fpr:',fpr)
print('tpr:',tpr)
print('thresholds:',thresholds)

import matplotlib.pyplot as plt
plt.rc('font', family = 'malgun gothic')
plt.plot(fpr, tpr, 'o-', label = 'Logistic Regression')
plt.plot([0, 1], [0, 1], 'k--', label = 'random guess')
plt.plot([fallout], [recall], 'ro', ms = 10)
plt.xlabel('fallout(fpr)위양성률')
plt.ylabel('recall(tpr)재현률')
plt.title("ROC 커브 연습")
plt.show()

# AUC (Area Under the Curve) : ROC 커브의 면적
# 위양성률이 같을 때 재현률 값이 크거나, 재현률이 같을때 위양성률이 작을 수록  1에 가까운 값이고 이런 형태가 나오면 좋은 모델이라 판정
from sklearn.metrics import auc
print("ROC 커브의 면적 : ", auc(fpr, tpr))
