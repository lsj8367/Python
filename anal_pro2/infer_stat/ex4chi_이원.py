# 실습 : 교육수준과 흡연율 간의 관련성 분석 : smoke.csv
import pandas as pd
import scipy.stats as stats
data = pd.read_csv("testdata/smoke.csv")
#data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/smoke.csv')

print(data.head(3))
print(data['education'].unique())  # [1 2 3]
print(data['smoking'].unique()) # [1 2 3]

# 귀무 : 교육수준과 흡연율 간에 관련이 없다.
# 대립 : 교육수준과 흡연율 간에 관련이 있다.
# 독립 : 범주형, 종속 : 범주형 <= 카이제곱 검정

# 학력 수준별 흡연에 대한 교차표 작성
#ctab = pd.crosstab(index = data['education'], columns = data['smoking']) # 빈도수
ctab = pd.crosstab(index = data['education'], columns = data['smoking'])  # 빈도비율
ctab.index = ['대학원졸', '대졸', '고졸']
ctab.columns = ['과흡연', '보통', '비흡연']
print(ctab)

# 수식을 사용할 수 있으나, 제공되는 메소드를 이용
chi_result = [ctab.loc['대학원졸'], ctab.loc['대졸'], ctab.loc['고졸']]
#chi2, p, ddof, expected = stats.chi2_contingency(chi_result)
chi2, p, ddof, expected = stats.chi2_contingency(ctab) # 다른칼럼이 작업에 참여하지 않는경우 바로 사용이 가능
msg = 'chi2:{}, p-value:{}, df:{}'
print(msg.format(chi2, p, ddof))
print('expected : ', expected)
# 해석  : p-value:0.0008182572832162924 < 알파 0.05 귀무가설 기각. 교육수준과 흡영ㄴ율간에 관계가 없다.
# Yates 보정 : 분할표의 자유도가 1인 경우에는 x^2값이 약간 높게 계산된다.
# 그래서 아래의식과 같이 절대값 |O-E|에서 0.5를 뺀 다음 제곱하며, 이 방법을 야트보정이라 한다.

print("-----------------------------")
# 실습) 국가전체와 지역에 대한 인종 간 인원수로 독립성 검정 실습
# 두 집단(국가전체 - national, 특정지역 ~ la) 의 인종간 인원수의 분포가 관련이 있는가?
# 귀무 : 국가전체와 특정지역의 인종 간 인원수의 분포가 관련이 없다.
# 대립 : 국가전체와 특정지역의 인종 간 인원수의 분포가 관련이 있다.
national = pd.DataFrame(['white'] * 100000 + ['hispanic'] * 60000 + \
                        ['black'] * 50000 + ['asian'] * 15000 + ['ohter'] * 35000)
la = pd.DataFrame(['white'] * 600 + ['hispanic'] * 300 + ['black'] * 250 + \
                  ['asian'] * 75 + ['ohter'] * 150)

print(national)
print(la)
na_table = pd.crosstab(index = national[0], columns = 'count')
la_table = pd.crosstab(index = la[0], columns = 'count')
#print(na_table)
na_table['count_la'] = la_table["count"]
print(na_table)

chi2, p, df, _ = stats.chi2_contingency(na_table)
print('chi2:', chi2,'p-value:', p, 'df:', df)
# p-value : 0.0011 < 0.05 이므로 귀무가설 기각

