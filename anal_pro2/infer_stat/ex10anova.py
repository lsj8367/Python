# 일원분산 분석으로 집단 간의 평균차이 검정
import scipy.stats as stats
import pandas as pd
import numpy as np
import urllib.request
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/group3.txt"
data = np.genfromtxt(urllib.request.urlopen(url), delimiter = ',')
print(data)

# 강남구 소재 GS 편의점 알바생의 3개 지역 급여에 대한 평균차이를 검정하시오
# 귀무 : 3개 지역 급여에 대한 평균차이가 없다.
# 대립 : 3개 지역 급여에 대한 평균차이가 있다.


gr1 = data[data[:, 1] == 1, 0]
gr2 = data[data[:, 1] == 2, 0]
gr3 = data[data[:, 1] == 3, 0]
print(gr1)
print(gr2)
print(gr3)
print(np.average(gr1), ' ', np.average(gr2), ' ', np.average(gr3)) # 평균값 : 316.625   256.44444444444446   278.0

# 정규성 검정
print(stats.shapiro(gr1)) # 정규성 만족
print(stats.shapiro(gr2))
print(stats.shapiro(gr3))

# 등분산성 검정....

# 시각화
# plot_data = [gr1, gr2, gr3]
# plt.boxplot(plot_data)
# plt.show()

# 일원분산분석 1
f_statistic, p_val = stats.f_oneway(gr1, gr2, gr3)
print('f_statistic:', f_statistic, ', p_val:', p_val)
# p_val: 0.0435893 < 0.05이므로 귀무가설 기각. 3개 지역 급여에 대한 평균에 차이가 있다.

print()
# 일원분산분석 2 : linear model을 이용
df = pd.DataFrame(data, columns = ['value', 'group'])
#print(df)

model = ols('value ~ C(group)', df).fit() # 종속변수 ~ 독립변수 # 학습시키는것 fit
print(anova_lm(model))
# 0.043589 --> p_value
# 방법1과 방법2의 p-value는 같다.
