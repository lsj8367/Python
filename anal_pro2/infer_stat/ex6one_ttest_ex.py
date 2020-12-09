import numpy as np
import pandas as pd
import scipy.stats as stats
'''
[one-sample t 검정 : 문제1]  
영사기에 사용되는 구형 백열전구의 수명은 250시간이라고 알려졌다. 
한국연구소에서 수명이 50시간 더 긴 새로운 백열전구를 개발하였다고 발표하였다. 
연구소의 발표결과가 맞는지 새로 개발된 백열전구를 임의로 수집하여 수명시간을 수집하여 다음의 자료를 얻었다. 
한국연구소의 발표가 맞는지 새로운 백열전구의 수명을 분석하라.
'''
print('===================문제 1====================')
# 귀무 : 한국연구소가 수명이 50시간 더 긴 새로운 백열전구를 개발 했다.
# 대립 : 한국연구소가 수명이 50시간 더 긴 새로운 백열전구를 개발 하지 못했다.
ex1 = [305, 280, 296, 313, 287, 240, 259, 266, 318, 280, 325, 295, 315, 278] # 영사기에 사용되는 백열전구의 수명
print(np.mean(ex1)) # 평균값 289.785
result = stats.ttest_1samp(ex1, popmean = 300)
print(result) # Ttest_1sampResult(statistic=-1.556435658177089, pvalue=0.143606254517609)
# pvalue=0.143 > 0.05 귀무가설 채택
# 결론 : 한국연구소가 수명이 50시간 더 긴 새로운 백열전구를 개발 했다.

print('\n===================문제 2====================')

'''
[one-sample t 검정 : 문제2] 
국내에서 생산된 대다수의 노트북 평균 사용 시간이 5.2 시간으로 파악되었다. A회사에서 생산된 노트북 평균시간과 차이가 있는지를 검정하기 위해서 A회사 노트북 150대를 랜덤하게 선정하여 검정을 실시한다.
실습 파일 : one_sample.csv
'''
# 귀무 : A사 노트북 평균 사용 시간이 국내 노트북 평균사용시간 5.2시간과 차이가 있다.
# 대립 : A사 노트북 평균 사용 시간이 국내 노트북 평균사용시간 5.2시간과 차이가 없다.
ex2 = pd.read_csv('testdata/one_sample.csv')
ex2 = ex2.replace("     ", np.nan).dropna()
print(ex2)
data = ex2.sample(n=len(ex2))
#print(pd.to_numeric(data['time'].values))
print(np.mean(pd.to_numeric(ex2['time'].values)))
result2 = stats.ttest_1samp(pd.to_numeric(data['time'].values), popmean = 5.2)
print(result2)
# Ttest_1sampResult(statistic=3.9460595666462432, pvalue=0.00014166691390197087)
# pvalue=0.00014 < 0.05 귀무가설 기각 A사 노트북 평균 사용 시간이 국내 노트북 평균사용시간 5.2시간과 차이가 없다.


print('\n===================문제 3====================')
'''
[one-sample t 검정 : 문제3] 
http://www.price.go.kr에서 메뉴 중  가격동향 -> 개인서비스요금 -> 조회유형:지역별, 품목:미용 자료를 파일로 받아 미용요금을 얻도록 하자. 
정부에서는 전국평균 미용요금이 15000원이라고 발표하였다. 이 발표가 맞는지 검정하시오.
'''
ex3 = pd.read_csv('ex3.csv')
#print(ex3.iloc[:,3:])
ex3 = ex3.iloc[:,3:].T # 서울~ 제주 미용요금 추출
# 귀무 : 전국 평균 미용요금이 15000이다.
# 대립 : 전국 평균 미용요금이 15000이 아니다.
print(ex3.head(5))
print(np.array(ex3).mean()) # 평균값 16008.5625
result3 = stats.ttest_1samp(ex3[0].values, popmean = 15000)
print(result3) # Ttest_1sampResult(statistic=2.258262434849591, pvalue=0.03925959042018307)
# pvalue=0.0392 < 0.05 귀무가설 기각 전국 평균 미용요금이 15000이 아니다.
