import scipy.stats as stats
import pandas as pd
import numpy as np
import urllib.request
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import statsmodels.api as sm
import matplotlib.pyplot as plt

# [ANOVA 예제 1]
# 빵을 기름에 튀길 때 네 가지 기름의 종류에 따라 빵에 흡수된 기름의 양을 측정하였다.
# 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하는지를 분산분석을 통해 알아보자.
# 조건 : NaN이 들어 있는 행은 해당 칼럼의 평균값으로 대체하여 사용한다.

# 귀무 : 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하지 않는다.
# 대립 : 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재한다.
kind = [1, 2, 3, 4, 2, 1, 3, 4, 2, 1, 2, 3, 4, 1, 2, 1, 1, 3, 4, 2]
quantity = [64, 72, 68, 77, 56, None, 95, 78, 55, 91, 63, 49, 70, 80, 90, 33, 44, 55, 66, 77]

df = pd.DataFrame({'kind' : kind, 'quantity':quantity})
#print(df['quantity'].mean())
df = df.fillna(df['quantity'].mean()) # 결측값 평균으로 채우기
print(df.head(3))
m1 = df[df['kind'] == 1]
m2 = df[df['kind'] == 2]
m3 = df[df['kind'] == 3]
m4 = df[df['kind'] == 4]
q1 = m1['quantity']
q2 = m2['quantity']
q3 = m3['quantity']
q4 = m4['quantity']
# print(np.average(q1))
# print(np.average(q2))
# print(np.average(q3))
# print(np.average(q4))

# 정규성 확인
print(stats.shapiro(q1))
print(stats.shapiro(q2))
print(stats.shapiro(q3))
print(stats.shapiro(q4))
# print(stats.ks_2samp(q1, q2))
# print(stats.ks_2samp(q1, q3))
# print(stats.ks_2samp(q1, q4))
# print(stats.ks_2samp(q2, q3))
# print(stats.ks_2samp(q2, q4))
# print(stats.ks_2samp(q3, q4))
# p-value 전부 0.05 이상 정규성 만족

# 등분산성
print(stats.levene(q1, q2, q3, q4).pvalue) # 등분산 확인 :  0.3268969935062273 등분산도 만족

reg = ols("df['quantity'] ~ C(df['kind'])", data = df).fit()
print(anova_lm(reg, type=1))
# p-value :  0.604199 > 0.05 이므로 귀무가설 채택.  귀무 : 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하지 않는다.

from statsmodels.stats.multicomp import pairwise_tukeyhsd
# 각 그룹 간의 차이를 알고자 한다면 Post Hoc Test를 하게 된다.
turkeyResult = pairwise_tukeyhsd(df.quantity, df.kind)
print(turkeyResult) 

# [ANOVA 예제 2]
# DB에 저장된 buser와 jikwon 테이블을 이용하여 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 있는지 검정하시오.
# 만약에 연봉이 없는 직원이 있다면 작업에서 제외한다.
# 귀무 : 부서간 연봉 평균에 차이가 없다.
# 대립 : 부서간 연봉 평균에 차이가 있다.
import MySQLdb
import ast
with open('mariadb.txt', mode='r') as f:
    config = ast.literal_eval(f.read())
try:
    #print(config)
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    
    sql = '''
        select buser_num, buser_name, jikwon_pay from jikwon inner join buser on jikwon.buser_num = buser.buser_no
    '''
    df1 = pd.read_sql(sql, conn).dropna(subset = ['jikwon_pay']) # 결측값 제거 (연봉 없는 직원)
    print(df1.head(3))
    #print(df1.info())
    
    a1 = df1[df1['buser_name'] == '총무부']
    a2 = df1[df1['buser_name'] == '영업부']
    a3 = df1[df1['buser_name'] == '전산부']
    a4 = df1[df1['buser_name'] == '관리부']
    '''
    a1 = df1[df1['buser_num'] == 10]
    a2 = df1[df1['buser_num'] == 20]
    a3 = df1[df1['buser_num'] == 30]
    a4 = df1[df1['buser_num'] == 40]
    '''
    b1 = a1['jikwon_pay']
    b2 = a2['jikwon_pay']
    b3 = a3['jikwon_pay']
    b4 = a4['jikwon_pay']
#     print(np.average(b1))
#     print(np.average(b2))
#     print(np.average(b3))
#     print(np.average(b4))
    
    #print(b1)
    # 정규성 # 두개는 만족하고 두개는 만족하지 않음.
    print()
    
    print(stats.shapiro(b1).pvalue) # ShapiroResult(statistic=0.7803537845611572, pvalue=0.02604489028453827)
    print(stats.shapiro(b2).pvalue) # ShapiroResult(statistic=0.8372057676315308, pvalue=0.02560843899846077)
    print(stats.shapiro(b3).pvalue) # ShapiroResult(statistic=0.9133293628692627, pvalue=0.4194071292877197)
    print(stats.shapiro(b4).pvalue) # ShapiroResult(statistic=0.9809899926185608, pvalue=0.9078023433685303)
    
    # 등분산성
    print(stats.levene(b1, b2, b3, b4).pvalue) # 만족 LeveneResult(statistic=0.33787559669754447, pvalue=0.7980753526275928)
    
    # 정규성2개는 만족 2개는 만족 못했으므로 kruskal-wallis test 진행
    print(stats.kruskal(b1, b2, b3, b4))
    # KruskalResult(statistic=1.671252253685445, pvalue=0.6433438752252654)
    # p-value : 0.6433438752252654 > 0.05 이므로 귀무가설 채택, 부서간 연봉 평균에 차이가 없다.
    
    f_statistic, p_val = stats.f_oneway(b1, b2, b3, b4)
    print('f_statistic:', f_statistic, ', p_val:', p_val)
    # f_statistic: 0.41244077160708414 , p_val: 0.7454421884076983
    
    # 각 그룹 간의 차이를 알고자 한다면 Post Hoc Test를 하게 된다.
    turkeyResult = pairwise_tukeyhsd(df1.jikwon_pay, df1.buser_num, alpha = 0.05)
    print(turkeyResult)

except Exception as e:
    print("err :", str(e))
finally:
    cursor.close()
    conn.close()
    