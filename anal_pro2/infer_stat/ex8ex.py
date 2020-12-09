import scipy.stats as stats
import pandas as pd
import numpy as np

'''
[two-sample t 검정 : 문제1]
다음 데이터는 동일한 상품의 포장지 색상에 따른 매출액에 대한 자료이다. 
포장지 색상에 따른 제품의 매출액에 차이가 존재하는지 검정하시오.
   blue : 70 68 82 78 72 68 67 68 88 60 80
   red : 60 65 55 58 67 59 61 68 77 66 66
'''
blue = [70, 68, 82, 78, 72, 68, 67, 68, 88, 60, 80]
red = [60, 65, 55, 58, 67, 59, 61, 68, 77, 66, 66]
# 귀무 : 포장지 색상에 따른 제품의 매출액에 차이가 존재하지 않는다.
# 대립 : 포장지 색상에 따른 제품의 매출액에 차이가 존재한다.
print(stats.ttest_ind(blue, red, equal_var=True))
#Ttest_indResult(statistic=2.9280203225212174, pvalue=0.008316545714784403)
# pvalue=0.0083 < 0.05 귀무가설 기각 대립 : 포장지 색상에 따른 제품의 매출액에 차이가 존재한다.

if stats.ttest_ind(blue, red, equal_var=True).pvalue > 0.05:
    print("귀무 : 포장지 색상에 따른 제품의 매출액에 차이가 존재하지 않는다.")
else:
    print("대립 : 포장지 색상에 따른 제품의 매출액에 차이가 존재한다.")

print()
'''
[two-sample t 검정 : 문제2]  
아래와 같은 자료 중에서 남자와 여자를 각각 15명씩 무작위로 비복원 추출하여 혈관 내의 콜레스테롤 양에 차이가 있는지를 검정하시오.
  남자 : 0.9 2.2 1.6 2.8 4.2 3.7 2.6 2.9 3.3 1.2 3.2 2.7 3.8 4.5 4 2.2 0.8 0.5 0.3 5.3 5.7 2.3 9.8
  여자 : 1.4 2.7 2.1 1.8 3.3 3.2 1.6 1.9 2.3 2.5 2.3 1.4 2.6 3.5 2.1 6.6 7.7 8.8 6.6 6.4
'''
man = [0.9, 2.2, 1.6, 2.8, 4.2, 3.7, 2.6, 2.9, 3.3, 1.2, 3.2, 2.7, 3.8, 4.5, 4, 2.2, 0.8, 0.5, 0.3, 5.3, 5.7, 2.3, 9.8]
woman = [1.4, 2.7, 2.1, 1.8, 3.3, 3.2, 1.6, 1.9, 2.3, 2.5, 2.3, 1.4, 2.6, 3.5, 2.1, 6.6, 7.7, 8.8, 6.6, 6.4]
man = pd.Series(man)
woman = pd.Series(woman)
#print(man)
#print(np.average(man)) # 3.0652173913043472
#print(np.average(woman)) # 3.54
#mdata = man.sample(n=15)  # 15명 남자 무작위 비복원
#wdata = woman.sample(n=15) # 15명 여자 무작위 비복원
#print(mdata)
#print(stats.shapiro(mdata)) # ShapiroResult(statistic=0.955064058303833, pvalue=0.607390820980072)
#print(stats.shapiro(wdata)) # ShapiroResult(statistic=0.7995377779006958, pvalue=0.0036264313384890556) # 정규 만족 X
# ttest_ind를 사용하지않고 wilcoxon검정 시행
#print(stats.wilcoxon(mdata, wdata)) # 정규성 X # WilcoxonResult(statistic=57.0, pvalue=0.890380859375)
result = stats.mannwhitneyu(man, woman)
print(result)
if result.pvalue >= 0.05:
    print("귀무 : 두성별 혈관내의 콜레스테롤 양에 차이가 없다.")
else:
    print("대립 : 두성별 혈관내의 콜레스테롤 양에 차이가 있다.")
# 귀무 : 두성별 혈관내의 콜레스테롤 양에 차이가 있다.
# 대립 : 두성별 혈관내의 콜레스테롤 양에 차이가 없다.

print()

'''
[two-sample t 검정 : 문제3]
DB에 저장된 jikwon 테이블에서 총무부, 영업부 직원의 연봉의 평균에 차이가 존재하는지 검정하시오.
연봉이 없는 직원은 해당 부서의 평균연봉으로 채워준다.
'''
import MySQLdb
import ast
with open('mariadb.txt', mode='r') as f:
    config = ast.literal_eval(f.read())
#print(config)
try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = '''
        select buser_name, jikwon_pay from jikwon inner join buser on jikwon.buser_num = buser.buser_no
        '''
    cursor.execute(sql)
    
    df = pd.read_sql(sql, conn)
    #print(df)
    
    b1 = df[df['buser_name'] == '총무부']
    b2 = df[df['buser_name'] == '영업부']
    #print(b1) # 총무부만 추려냄
    #print(b2) # 영업부만 추려냄
    b1 = b1.fillna(b1['jikwon_pay'].mean()) # 결측값 평균값으로 채워넣음
    b2 = b2.fillna(b1['jikwon_pay'].mean())
    #b2 = b2.sample(n=7) # 길이를 안맞추면 에러가 떠서 7개로 총무부랑 맞춰줌

    x1 = b1.iloc[:,1]
    x2 = b2.iloc[:,1]
    # 귀무 : 총무부, 영업부 직원의 연봉의 평균에 차이가 있다
    # 대립 : 총무부, 영업부 직원의 연봉의 평균에 차이가 없다
    #print(x1.mean())
    #print(x2.mean())
    print(stats.shapiro(x1)) # ShapiroResult(statistic=0.7803537845611572, pvalue=0.02604489028453827)
    print(stats.shapiro(x2)) # ShapiroResult(statistic=0.8463208675384521, pvalue=0.11370489001274109) 계속 변함
    # 정규성을 만족하지 않음 wilcoxon사용
    #print(stats.wilcoxon(x1, x2)) # WilcoxonResult(statistic=13.0, pvalue=0.9375)
    print(stats.ttest_ind(x1,x2))
    if stats.ttest_ind(x1, x2).pvalue >= 0.05:
        print("귀무 : 총무부,영업부(샘플 7개)직원의 연봉의 평균에 차이가 없다")
    else:
        print("대립 : 총무부,영업부(샘플 7개)직원의 연봉의 평균에 차이가 있다")

except Exception as e:
    print("err : ", str(e))
finally:
    cursor.close()
    conn.close()

print()
'''
[대응표본 t 검정 : 문제4]
어느 학급의 교사는 매년 학기 내 치뤄지는 시험성적의 결과가 실력의 차이없이 비슷하게 유지되고 있다고 말하고 있다. 이 때, 올해의 해당 학급의 중간고사 성적과 기말고사 성적은 다음과 같다. 점수는 학생 번호 순으로 배열되어 있다.
   중간 : 80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80
   기말 : 90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95
그렇다면 이 학급의 학업능력이 변화했다고 이야기 할 수 있는가?
'''
mid = [80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80]
final = [90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95]

#print(np.mean(mid)) # 평균 : 74.16666666666667
#print(np.mean(final)) # 평균 : 81.66666666666667
# 중간,기말 점수는 전후관계 이므로 ttest_rel 사용
print(stats.ttest_rel(mid, final)) # Ttest_relResult(statistic=-2.6281127723493993, pvalue=0.023486192540203194)
if stats.ttest_rel(mid, final).pvalue > 0.05:
    print("귀무 : 이 학급의 학업능력이 변화하지 않았다.")
else:
    print("대립 : 이 학급의 학업능력이 변화했다.")
