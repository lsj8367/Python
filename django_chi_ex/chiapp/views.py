from django.shortcuts import render
from chiapp.models import Survey
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family = 'malgun gothic') # 한글 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False # 음수 부호 깨짐 방지
#  1) 선택 결과를 DB에 저장하라.
#  2) 성별과 커피브랜드별 인원수를 교차분할표로 출력하시오.
#  3) 이 자료를 근거로 성별에 따라 선호하는 커피브랜드에 차이가 있는지를 검정하고 그 결과를 해석하시오.
#  4) 검정결과를 웹문서로 출력하시오.
#  5) 커피브랜드별 선호 건수에대한 차트(세로막대)를 출력하시오
# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')
def surveyFunc(request):
    return render(request, 'survey.html')
def listFunc(request):
    # 귀무 : 성별에따라 선호하는 커피브랜드에는 차이가 있다
    # 대립 : 성별에따라 선호하는 커피브랜드에는 차이가 없다
    if request.method == "POST":
        #print(request.POST['gender'])
        
        # DB에 값 insert
        Survey(
                    gender = request.POST['gender'],
                    age = request.POST['age'],
                    co_survey = request.POST['co_survey'],
                    ).save()

#         print(df)
#         for data in datas:
#             print(data.gender)
        
        #print(datas, type(datas))
        datas = Survey.objects.all() # 삽입한 후에 결과를  select
        df = pd.DataFrame(list(datas.values())) # 값만 가지고 데이터프레임을 만든다.
        dftab = pd.crosstab(index = df['gender'], columns= df['co_survey']) # 성별과 브랜드에 관한 교차표
        
        #print(dftab)
        result1 = dftab.to_html() # 교차표 html문서화
        chi_result = [dftab.loc['남'], dftab.loc['여']] # 성별에대해 카이제곱분포
        chi2, p, _, _ = stats.chi2_contingency(chi_result)
        #print(chi2, ' ' , p)
        context = {'result' : result1, 'chi2' : chi2, 'p':p} # result.html에 넘겨줄값

        #커피브랜드별 선호 건수에대한 차트(세로막대)를 출력하시오
        #print(dftab.sum())
        box = df['co_survey'].unique()
        #print(box) # 브랜드명
        lists = []
        for i in box:
            lists.append(dftab[i].sum()) # 각 브랜드의 커피선호도 합계
        #print(lists)

            
        #print(box, lists)

        plt.bar(box, lists, width=0.5, color='purple') # 구간, 값 세로막대
        #plt.legend(['판매량'], loc = 1) # loc 시계반대방향 위치주는것
        plt.title('커피브랜드별 선호 건수에대한 차트(세로막대)')
        plt.xlabel('매장 종류')
        plt.ylabel('매장별 판매수')
        fig = plt.gcf() # 저장준비 선언
        fig.savefig('C:/Users/com/python/django_chi_ex/chiapp/static/plot.png')
        
    return render(request, 'result.html', context)
         
    