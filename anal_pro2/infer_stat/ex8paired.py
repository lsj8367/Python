'''
* 서로 대응인 두 집단의 평균 차이 검정(paired samples t-test, 동일표본 t검정, 대을표본t검정, 쌍체 검정)
처리 이전과 처리 이후를 각각의 모집단으로 판단하여, 동일한 관찰 대상으로부터 처리 이전과 처리 이후를 1:1로 대응시킨 두 집단으로 부터
의 표본을 대응표본(paired sample)이라고 한다.
대응인 두 집단의 평균 비교는 동일한 관찰 대상으로부터 처리 이전의 관찰과 이후의 관찰을 비교하여 영향을 미친 정도를 밝히는데 주로 사용
하고 있다. 집단 간 비교가 아니므로 등분산 검정을 할 필요가 없다.
조건 : 정규성을 만족, 
'''
# 실습1) 정규분포를 따르는 난수 데이터 
import numpy as np
import scipy as sp
import scipy.stats as stats

np.random.seed(1)
x1 = np.random.normal(80, 10, 100)
x2 = np.random.normal(77, 10, 100)
print(stats.shapiro(x1).pvalue) # 0.82154381275177
print(stats.shapiro(x2).pvalue) # 0.5715901851654053
# 귀무 : 특강 전후의 시험점수에 차이가 없다
# 대립 : 특강 전후의 시험점수에 차이가 있다
print(stats.ttest_rel(x1, x2)) # 전과후의 데이터 삽입 Ttest_relResult(statistic=1.6866277160835161, pvalue=0.09482383636569139)
# pvalue = 0.09482383 > 0.05이므로 귀무가설 채택

print("----------------------------")
# 실습2) 9명의 환자에 대해 복부 수술 전 몸무게와 복부 수술 후 몸무게에 변화가 있는가를 검증해라.
baseline = [67.2, 67.4, 71.5, 77.6, 86.0, 89.1, 59.5, 81.9, 105.5]
follow_up = [62.4, 64.6, 70.4, 62.6, 80.1, 73.2, 58.2, 71.0, 101.0]
print('수술전 몸무게 평균:', np.mean(baseline)) # 78.41111111111111
print('수술후 몸무게 평균:', np.mean(follow_up)) # 71.5
# 귀무 : 수술 전 몸무게와 복부 수술후 몸무게 변화가 없다
# 대립 : 수술 전 몸무게와 복부 수술후 몸무게 변화가 있다
print(stats.ttest_rel(baseline, follow_up)) # Ttest_relResult(statistic=3.6681166519351103, pvalue=0.006326650855933662)
# pvalue = 0.00632 < 0.05 이므로 귀무가설 기각

print("^^^^^^^^^^^^^^^^^^^^^^^")
# 집단에 따라 t검정 방법은 달라질 수 있다.
# 수면제1 종류를 먹다가 수면제2 종류를 먹었을 때 수면시간 변화에 차이가 있는지 검정하시오.
x1 = np.array([0.7, 0.3, 0.2, 0.1, 0.2]) # 수면제1 복용 시
x2 = np.array([1.3, 1.0, 0.3, 0.1, 0.5]) # 수면제2 복용 시
print(np.mean(x1)) # 0.3
print(np.mean(x2)) # 0.6399999999999999

print()
# 실습 1) 서로 다른 사람이 각 수면제를 먹었을 때 : 독립표본 T검정
result1 = stats.ttest_ind(x1, x2, equal_var = True)
#print(result1.pvalue)
if result1.pvalue >= 0.05:
    print("약의 변경여부에 따른 수면시간에 변화가 없다.")
else:
    print("약의 변경여부에 따른 수면시간에 변화가 있다.")
# 실습 2) 동일한 사람이 시간에 차이를 두고 각 수면제를 먹었을 때 : 대응표본 T검정
result2 = stats.ttest_rel(x1, x2)
if result2.pvalue >= 0.05:
    print("약의 변경여부에 따른 수면시간에 변화가 없다.")
else:
    print("약의 변경여부에 따른 수면시간에 변화가 있다.")












