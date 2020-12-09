# 단일 집단 평균 검정(일표본 t검정, one-sample t-test) : 독립(범주형), 종속(연속형)
# 모수(평균)를 알고 있는 경우 sample의 평균과 차이가 있는지 검정

# 실습1 : 어느 남성 집단의 평균 키 검정
# 귀무 : 어느 남성 집단의 평균 키는 177이다 (모수)
# 대립 : 어느 남성 집단의 평균 키는 177이 아니다 (모수)

import numpy as np
import scipy.stats as stats
import matplotlib.pylab as plt
import seaborn as sns
import pandas as pd

# 이미 알려진 평균에 대한 비교 집단이 하나
one_sample = [177.0, 182.7, 169.6, 176.8, 180.0]
print(np.array(one_sample).mean()) # 177.22
result = stats.ttest_1samp(one_sample, popmean = 177) # popmean에 평균값을 지정
print(result) # Ttest_1sampResult(statistic=0.10039070766877535, pvalue=0.9248646407498543)
# 해석 : pvalue=0.9248 > 0.05 이므로 귀무가설 채택

print()
# 귀무 : 어느 남성 집단의 평균 키는 167이다 (모수)
# 대립 : 어느 남성 집단의 평균 키는 167이 아니다 (모수)
result2 = stats.ttest_1samp(one_sample, popmean = 167)
print(result2)
# 해석 : pvalue = 0.0095 < 0.05 귀무가설 채택

print('*****' * 10)
# 실습 2 : 난수를 발생시켜 평균 검정
# 귀무 : 자료들의 평균은 0이다.
# 대립 : 자료들의 평균은 0이아니다.
np.random.seed(123)
mu = 0
n = 10
x = stats.norm(mu).rvs(n)  # 랜덤한 샘플데이터 10개 정규분포 ---- 샘플이 많으면 많아질수록 중심극한의 원리에 의해 0에 가까워짐
print(x, np.average(x))
# sns.distplot(x, kde=False, rug=True, fit=stats.norm)
# plt.show()

result3 = stats.ttest_1samp(x, popmean=0)
print(result3) # Ttest_1sampResult(statistic=-0.6540040368674593, pvalue=0.5294637946339893)
# 해석 : pvalue=0.5294 > 0.05 귀무가설 채택

result4 = stats.ttest_1samp(x, popmean=0.7)
print(result4) #Ttest_1sampResult(statistic=-2.3526142804366375, pvalue=0.043120011586159794)
# 해석 : pvalue=0.043 < 0.05 귀무가설 기각

print('~~~' * 10)
# 실습 예제 3)A중학교 1학년 1반 학생들의 시험결과가 담긴 파일을 읽어 처리 (국어 점수 평균검정) student.csv
data = pd.read_csv('testdata/student.csv')
print(data.head(2))
print(data.describe())
print(np.mean(data.국어)) # 72.9
# 귀무 : 학생들의 국어점수의 평균은 80이다.
# 대립 : 학생들의 국어점수의 평균은 80이 아니다.
result5 = stats.ttest_1samp(data['국어'], popmean = 80)
print(result5) # Ttest_1sampResult(statistic=-1.3321801667713213, pvalue=0.19856051824785262)
# 해석 : pvalue=0.19 > 0.05 귀무가설 채택

result6 = stats.ttest_1samp(data['국어'], popmean = 60)
print(result6) # Ttest_1sampResult(statistic=2.420440021316911, pvalue=0.025687810312950816)
# 해석 : pvalue=0.0256 < 0.05 귀무가설 기각

'''
실습 예제 4)
여아 신생아 몸무게의 평균 검정 수행 babyboom.csv
여아 신생아의 몸무게는 평균이 2800(g)으로 알려져 왔으나 이보다 더 크다는 주장이 나왔다.
표본으로 여아 18명을 뽑아 체중을 측정하였다고 할 때 새로운 주장이 맞는지 검정해 보자.
'''
# 귀무 : 여아 신생아의 몸무게는 평균이 2800(g)이다.
# 대립 : 여아 신생아의 몸무게는 평균이 2800(g)보다 크다.
babydata = pd.read_csv('testdata/babyboom.csv')
print(babydata.head(3))
print()
#print(babydata.columns)
fdata = babydata[babydata.gender == 1] # 여아만 추출 gender값이 1인것
print(fdata.head(3), len(fdata)) # 18명
print(np.mean(fdata.weight)) # 3132.4444444444443

result7 = stats.ttest_1samp(fdata['weight'], popmean = 2800)
print(result7) # Ttest_1sampResult(statistic=2.233187669387536, pvalue=0.03926844173060218)
# 해석 : pvalue=0.0392 < 0.05 귀무가설 기각 == 여아 신생아의 몸무게는 평균이 2800(g)보다 크다.

# 참고 : t분포를 구성하는데 정규분포와  모양이 유사, t-test의 선행조건으로 데이터는 정규성을 따르는지 확인
print(stats.shapiro(fdata.weight))
print(stats.shapiro(fdata.iloc[:,2])) # p-value : 0.05보다 크면 정규성을 만족
# ShapiroResult(statistic=0.8702831864356995, pvalue=0.017984945327043533) : 정규성 만족하지 못함

# 정규성을 따르는지 확인
# sns.distplot(fdata.iloc[:,2], fit = stats.norm)
# plt.show()
stats.probplot(fdata.iloc[:,2], plot = plt) # qqplot
plt.show()
