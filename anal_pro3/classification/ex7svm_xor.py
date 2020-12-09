# SVM으로 XOR 분류 모델 작성
xor_data = [
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0]
]

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import svm, metrics

xor_df = pd.DataFrame(xor_data)
print(xor_df)
feature = np.array(xor_df.iloc[:, 0:2]) # 독립변수
label = np.array(xor_df.iloc[:, 2]) # 종속변수
print(feature) 
print(label)

# LogisticRegression으로 분류
#model = LogisticRegression()
# SVC로 분류 (svm알고리즘 사용)
#model = svm.SVC()
model = svm.SVC(C = 10) # 위와 같음
#model = svm.LinearSVC(C = 1000) # 개량형
model.fit(feature, label)
pred = model.predict(feature)
print("예측값 : ", pred)

print()
acc = metrics.accuracy_score(label, pred) # 실제값, 예측값
print("accuracy(분류정확도)", acc)

ac_report = metrics.classification_report(label, pred)
print(ac_report)