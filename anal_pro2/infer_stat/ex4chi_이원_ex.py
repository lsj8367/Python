import MySQLdb
import numpy as np
import pandas as pd
import ast
import csv
import scipy.stats as stats
# 카이제곱 문제1) 부모학력 수준이 자녀의 진학여부와 관련이 있는가?를 가설검정하시오
#   예제파일 : cleanDescriptive.csv
#   칼럼 중 level - 부모의 학력수준(대학원1,대졸:2,고졸:3), pass - 자녀의 대학 진학여부(성공:1, 실패:2)
#   조건 : NA가 있는 행은 제외한다
# 귀무 : 부모학력 수준이 자녀의 진학여부와 관련이 없다
# 대립 : 부모학력 수준이 자녀의 진학여부와 관련이 있다
data = pd.read_csv("testdata/cleanDescriptive.csv").dropna(subset=['level','pass'])
print(data)
#print(data.dropna(axis = 0))
#data = data.dropna(axis = 0)
print(data.columns)
df1 = data.loc[:, ['level', 'pass', 'level2', 'pass2']]
print(df1)
df_tab = pd.crosstab(index = df1['level'], columns = df1['pass'])
df_tab.index = ['고졸', '대졸', '대학원졸']
df_tab.columns = ['합격', '불합격']
print(df_tab)
chi_result = [df_tab.loc['고졸'], df_tab.loc['대졸'], df_tab.loc['대학원졸']]
chi2, p, ddof, expected = stats.chi2_contingency(chi_result)
print('chi2:', chi2,'p-value:', p, 'df:', ddof)
# chi2: 7.794459691049416 p-value: 0.25070568406521365 df: 2
# 유의수준 0.05 > 0.02 이므로 귀무가설 기각    부모학력 수준이 자녀의 진학여부와 관련이 없다

print("===========================================================")
# 카이제곱 문제2) jikwon_jik과 jikwon_pay 간의 관련성 분석. 가설검정하시오.
#   예제파일 : MariaDB의 jikwon table 
#   jikwon_jik   (이사:1, 부장:2, 과장:3, 대리:4, 사원:5)
#   jikwon_pay (1000 ~2999 :1, 3000 ~4999 :2, 5000 ~6999 :3, 7000 ~ :4)
#    귀무 : 직급과 급여는 관련이 없다.
#    대립 : 직급과 급여는 관련이 있다.
#   조건 : NA가 있는 행은 제외한다.
with open('mariadb.txt', mode = 'r') as f:
    config = ast.literal_eval(f.read())

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = 'select jikwon_jik, jikwon_pay from jikwon'
    
    df = pd.read_sql(sql, conn)
    print(df)
        
    df.loc[df['jikwon_jik'] == '이사', '직급'] = '1이사'
    df.loc[df['jikwon_jik'] == '부장', '직급'] = '2부장'
    df.loc[df['jikwon_jik'] == '과장', '직급'] = '3과장'
    df.loc[df['jikwon_jik'] == '대리', '직급'] = '4대리'
    df.loc[df['jikwon_jik'] == '사원', '직급'] = '5사원'
    
    #df['jikwon_pay'] = pd.to_numeric(df['jikwon_pay'])
    df.loc[(df['jikwon_pay'] >= 1000) & (df['jikwon_pay'] < 3000), '급여'] = '1000 ~2999'
    df.loc[(df['jikwon_pay'] >= 3000) & (df['jikwon_pay'] < 4999), '급여'] = '3000 ~4999'
    df.loc[(df['jikwon_pay'] >= 5000) & (df['jikwon_pay'] < 6999), '급여'] = '5000 ~6999'
    df.loc[df['jikwon_pay'] >= 7000, '급여'] = '7000 ~'
    print(df)
    
    df2_tab = pd.crosstab(index = df['직급'], columns = df['급여'])
    print(df2_tab)
    
    chi2_result = [df2_tab.loc['1이사'], df2_tab.loc['2부장'], df2_tab.loc['3과장'], df2_tab.loc['4대리'], df2_tab.loc['5사원']]
    chi2, p, ddof, expected = stats.chi2_contingency(chi2_result)
    print('chi2:', chi2,'p-value:', p, 'df:', ddof)
    # chi2: 37.40349394195548 p-value: 0.00019211533885350577 df: 12
    # p-value: 0.0001 이므로 유의수준 0.05보다 작음 귀무가설 기각 
    
except Exception as e:
    print("error : ", str(e))
finally:
    cursor.close()
    conn.close()