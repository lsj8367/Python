import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import roc_curve, auc
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
from tensorflow.keras.utils import to_categorical
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/bmi.csv')
print(df.head(5))
print(df.info())
label = {'thin' : 0, 'normal' : 1, 'fat' : 2}
df = df.replace({'label' : label})
print(df)
data = df.values
x = np.array(data[:, 0:-1], dtype= np.float64) # int는 tensor에 없음
y = data[:, -1]
#print(x)
#print(y)

onehot = OneHotEncoder(categories = 'auto')
y = onehot.fit_transform(y[:, np.newaxis]).toarray()
print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 1)

print(x_train.shape)
n_features = x_train.shape[1]
n_classes = y_train.shape[1]
print(n_features)
print(n_classes)

def create_newModel(input_dim, output_dim, out_nodes, n, model_name = 'model'):
    def create_model():
        model = Sequential(name = model_name)
        for _ in range(n):
            model.add(Dense(out_nodes, input_dim = input_dim, activation = 'relu'))
            
        model.add(Dense(output_dim, activation = 'softmax'))
        model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
        return model
    return create_model
'''
models = [create_newModel(n_features, n_classes, 10, n, 'model_{}'.format(n)) for n in range(1, 4)]

history_dict = {}

for create_model in models:
    create_model().summary()
    model = create_model()
    
    print(type(x_train))
    print(type(y_train))
    print(x_train.dtype, ' ', y_train.dtype)
    
    historys = model.fit(x_train, y_train, batch_size = 10, epochs = 50, verbose = 2, validation_split = 0.3)
    score = model.evaluate(x_test, y_test, verbose = 2)
    print('test accuracy : ', score[1])
    history_dict[model.name] = [historys, model]
    
print(history_dict)

# 시각화
fig, (ax1, ax2) = plt.subplots(2, 1, figsize = (8, 6))
#print(fig, ax1, ax2)

for model_name in history_dict:
    print('h_d : ', history_dict[model_name][0].history['acc']) # model 별로 historys의 history의 정확도 보기
    val_acc = history_dict[model_name][0].history['val_acc']
    val_loss = history_dict[model_name][0].history['val_loss']
    ax1.plot(val_acc, label = model_name)
    ax2.plot(val_loss, label = model_name)
    ax1.set_ylabel('validation acc')
    ax2.set_ylabel('validation loss')
    ax2.set_xlabel('epochs')
    ax1.legend()
    ax2.legend()
plt.show()

print('\nROC curve - 분류 모델 성능 평가 기법중 하나 ====')
# AUC 값은 1에 가까울수록 우수한 모델
plt.figure()
plt.plot([0, 1],[0, 1],'k--')

for model_name in history_dict:
    model = history_dict[model_name][1]
    y_pred = model.predict(x_test)
    fpr, tpr, _ = roc_curve(y_test.ravel(), y_pred.ravel())
    print('fpr : ', fpr)
    print('tpr : ', tpr)
    plt.plot(fpr, tpr, label = '{}, AUC value:{:.3f}'.format(model_name, auc(fpr, tpr)))

plt.xlabel('False Positive rate')
plt.ylabel('True Positive rate')
plt.title('ROC Curve')
plt.legend()
plt.show()
'''
# 가장 마지막것의 정확도가 좋아서 채택
create_model = create_newModel(n_features, n_classes, 10, 3)

estimator = KerasClassifier(build_fn = create_model, epochs = 50, batch_size = 20, verbose = 2)
scores = cross_val_score(estimator, x, y, cv = 2)
print('Accuracy : {:0.2f} (±{:0.2f})'.format(scores.mean(), scores.std()))

model = Sequential()
model.add(Dense(10, input_dim = n_features, activation = 'relu'))
model.add(Dense(10, activation = 'relu'))
model.add(Dense(10, activation = 'relu'))
model.add(Dense(3, activation = 'softmax'))

model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics=['acc'])
print(model.summary())

model.fit(x_train, y_train, epochs = 50, batch_size = 20, verbose = 2)
print('모델 검증 : ', model.evaluate(x_test, y_test))

print()
y_pred = np.argmax(model.predict(x_test), axis = 1)
print('pred : ', y_pred)
real_y = np.argmax(y_test, axis = 1).reshape(-1, 1)
print("실제 값 : ", real_y.ravel())
print("분류 실패 수 : ", (y_pred != real_y.ravel()).sum())

print()
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
print('confusion_matrix : ', confusion_matrix(real_y, y_pred))
print('accuracy : ', accuracy_score(real_y, y_pred))
print('classification_report : \n', classification_report(real_y, y_pred))

# 새로운 값으로 예측하기
height = float(input('키 입력 : '))
weight = float(input('몸무게 입력 : '))
#print(height, weight)
new_data = [[height, weight]]
new_pred = model.predict(new_data)
# print('new_pred : ', new_pred)
print('new_pred  ', np.argmax(new_pred, axis = 1).flatten()) # 0: thin 1: normal 2: fat

