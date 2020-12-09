# iris dataset으로 선형회귀분석
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf

iris = sns.load_dataset('iris')
print(iris.head(3))

# sns.pairplot(iris, hue = 'species', height = 1.5)
# plt.show()

# 변수 간 상관관계
print(iris.corr())

print()
# 회귀모델 : 상관관계가 약한 변수를 사용
#result1 = smf.ols(formula = 'sepal_length ~ sepal_width', data = iris).fit()
# 원래는 sepal과 petal을 비교하는것은 옳지 않지만 연습용그냥 진행
result1 = smf.ols(formula = 'sepal_length ~ petal_length', data = iris).fit()

print("result1 요약 결과표\n", result1.summary())
print("result1 R squared : ", result1.rsquared)
print("result1 p-value : ", result1.pvalues)
pred = result1.predict()
print('예측값: ', pred[:5])
print('실제값: ', iris.sepal_length[:5])
# 새로운 data로 예측
new_data = pd.DataFrame({'petal_length' : [1.4, 0.8, 8.0]})
y_pred_new = result1.predict(new_data)
print('새로운 data로 예측한 sepal_length 결과 : \n', y_pred_new)

print('\n다중회귀분석 : 독립변수 복수 -----------') # 'y ~ x1 + x2 + x3 +...'
result2 = smf.ols(formula = 'sepal_length ~ petal_length + petal_width', data = iris).fit()
print("result2 요약 결과표\n", result2.summary())
print("result2 R squared : ", result2.rsquared)
print("result2 p-value : ", result2.pvalues)

# 참고 : 여러 개의 칼럼 지정시 아래와 같은 방법을 사용하면 효과적.
column_select = '+'.join(iris.columns.difference(['sepal_length', 'sepal_width', 'species'])) # + 기준 difference안에 칼럼들 제외시켜  합침 
formula = 'sepal_length ~ ' + column_select
result2 = smf.ols(formula = formula, data = iris).fit()

new_data2 = pd.DataFrame({'petal_length' : [1.4, 0.8, 8.0], 'petal_width' : [0.2, 0.8, 1.5]})
y_pred_new2 = result1.predict(new_data2)
print('새로운 data로 예측한 sepal_length 결과 : \n', y_pred_new2)

# 다중공선성(Multicollinearity)과 VIF(Variance Inflation Factors)
# 다중회귀모형에서 일부 독립변수가 다른 독립변수와 상관관계가 너무 높은 경우 문제 발생.
# VIF 값이 10이 넘는 경우 다중 공선성 발생. 변수 선택에 신중해야 한다.
from statsmodels.stats.outliers_influence import variance_inflation_factor
print(iris.columns)
del iris['species'] # 칼럼 삭제
print(iris.columns)

vifDf = pd.DataFrame()
vifDf['vif factor'] = [variance_inflation_factor(iris.values, i) for i in range(iris.shape[1])] # range(열)만
vifDf['features'] = iris.columns
print(vifDf)
