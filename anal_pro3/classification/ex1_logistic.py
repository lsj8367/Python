# 로지스틱 회귀분석 (Logistic Regression) : 선형회귀 분석 확장 개념 - 이항분류가 목적
# 독립변수 : 연속형, 종속변수 : 범주형
# odds -> odds ratio -> logic function -> sigmoid function

# sigmoid function test
import math
def sigmoidFunc(x):
    return 1 / (1 + math.exp(-x))

print(sigmoidFunc(3))
print(sigmoidFunc(1))
print(sigmoidFunc(-3))
print(sigmoidFunc(-5))

print('------------------')
import statsmodels.formula.api as smf
import numpy as np
import statsmodels.api as sm

mtcars = sm.datasets.get_rdataset('mtcars').data
print(mtcars.head(2))
print()
mtcar = mtcars.loc[:, ['mpg', 'hp', 'am']]
print(mtcar.head(2), ' ', mtcar['am'].unique()) # [1 0]

# 방법1 logit()
formula = 'am ~ hp + mpg' # 범주형~ 연속형
result = smf.logit(formula = formula, data = mtcar).fit()
print(result)
print(result.summary())
#print("예측 값:", result.predict())
pred = result.predict(mtcar[:5])
print("예측 값:", np.around(pred))
print("실제 값:", mtcar.am[:5])

print()
#confusion matrix
conf_tab = result.pred_table()
print("confusion matrix:\n", conf_tab) # 맞춘수 틀린수를 행렬로 나타내줌 1행1열 참           2열 거짓     2행 1열 참          2열 거짓
# 분류정확도
print('분류정확도:', (16 + 10) / len(mtcar)) # 0.8125
print('분류정확도:', (conf_tab[0][0] + conf_tab[1][1]) / len(mtcar)) # 0.8125
from sklearn.metrics import accuracy_score # 정확도 알려주는 라이브러리
pred2 = result.predict(mtcar)
print('분류정확도:', accuracy_score(mtcar['am'], np.around(pred2))) # 실제값, 예측값을 넣어줌

print('***' * 10)
# 방법2 glm()
result2 = smf.glm(formula = formula, data = mtcar, family = sm.families.Binomial()).fit() # 이항분포라서 binomial로 변환함 default : Gausian()
print(result2)
print(result2.summary())
glm_pred = result2.predict(mtcar[:5])
print("glm_pred: ", np.around(glm_pred))

glm_pred2 = result2.predict(mtcar)
print('분류정확도2:', accuracy_score(mtcar['am'], np.around(glm_pred2)))

print("\n새로운 값으로 예측 결과를 얻기")
newdf = mtcar.iloc[:2]
print(newdf)
newdf['mpg'] = [10, 35]
newdf['hp'] = [80, 150]
print(newdf)
glm_pred_new = result2.predict(newdf)
print('glm_pred_new:', np.around(glm_pred_new))
print('glm_pred_new:', np.rint(glm_pred_new)) # 위와 같음

print()
import pandas as pd
newdf2 = pd.DataFrame({'mpg': [10, 100], 'hp':[200, 100]})
glm_pred_new2 = result2.predict(newdf2)
print('glm_pred_new2:', np.around(glm_pred_new2))
print('glm_pred_new2:', np.rint(glm_pred_new2))
