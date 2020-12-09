# 동질성 검정 - 두 집단의 분포가 동일한가? 다른 분포인가? 를 검증하는 방법이다. 
import pandas as pd
import scipy.stats as stats

data = pd.read_csv("testdata/survey_method.csv")
print(data.head())
print(data['method'].unique()) # [ 1 2 3]

# 귀무 : 교육방법에 따른 교육생들의 만족도에 차이가 없다.
ctab = pd.crosstab(index = data['method'], columns = data['survey'])
ctab.columns = ['매우만족', '만족', '보통', '불만족', '매우불만족']
ctab.index = ['방법1','방법2','방법3']
print(ctab)

chi2, p, _, _ = stats.chi2_contingency(ctab)
print('chi2:', chi2, ', p-value:', p)
# 동질성 검정 실습 2 연령대별 sns 이용률의 동질성 검정
# 귀무 : 연령대별 sns서비스들에 대해 이용 현황은 동일하다.
# 대립 : 연령대별 sns서비스들에 대해 이용 현황은 동일하지 않다.

sns_data = pd.read_csv("testdata/snsbyage.csv")
print(sns_data.head(2))
print(sns_data['age'].unique())
print(sns_data['service'].unique())

ctab2 = pd.crosstab(index = sns_data['age'], columns = sns_data['service']) # 나이대별 서비스 선정 인원수
print(ctab2)
chi2, p, df, exp = stats.chi2_contingency(ctab2)
print('chi2:', chi2, ', p-value:', p, 'df : ', df)