'''
회귀분석 문제 2) 
github.com/pykwon/python에 저장된 student.csv 파일을 이용하여 세 과목 점수에 대한 회귀분석 모델을 만든다. 
이 회귀문제 모델을 이용하여 아래의 문제를 해결하시오.
  - 국어 점수를 입력하면 수학 점수 예측
  - 국어, 영어 점수를 입력하면 수학 점수 예측
'''
import pandas as pd
import statsmodels.formula.api as smf

ex1 = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/student.csv")
print(ex1.head(5))
print(ex1.corr()) # 0.766263
model = smf.ols(formula = '수학 ~ 국어', data = ex1).fit()
print(model)
pred = model.predict()
print("실제값 : ", ex1.국어[:5])
print("예측값 : ", pred[:5])

kor = float(input('국어 점수를 입력하세요.'))
x_new = pd.DataFrame({'국어' : [kor]})
print("국어 점수로 예측된 수학 점수 :", model.predict(x_new))

model2 = smf.ols(formula = '수학 ~ 국어 + 영어', data = ex1).fit()
#print(model2.summary()) # Durbin-Watson:  2.163
# 국어, 영어 점수 입력하여 수학점수 예측하기
#print(model2.predict())
kor, eng = input("국어 영어 점수를 입력하세요.").split()
new_data = pd.DataFrame({'국어' : [float(kor)], '영어' : [float(eng)]})
pred2 = model2.predict(new_data)
print('국어,영어 점수로 예측된 수학 점수 결과 : ', pred2)

'''
회귀분석 문제 3) 
원격 DB의 jikwon 테이블에서 근무년수에 대한 연봉을 이용하여 회귀분석 모델을 작성하시오.
장고로 작성한 웹에서 근무년수를 입력하면 예상연봉이 나올 수 있도록 프로그래밍 하시오.
'''
import MySQLdb
import ast
with open('mariadb.txt', mode = 'r') as f:
    config = ast.literal_eval(f.read())

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = '''
        select jikwon_pay, (date_format(NOW(),'%Y') - date_format(jikwon_ibsail, '%Y')) as jikwon_ibsail from jikwon
    '''
    df = pd.read_sql(sql, conn)
    df['jikwon_ibsail'] = df['jikwon_ibsail'].astype(int)
    #print(df)
    print(df.corr()) # 0.919673
    
    model3 = smf.ols(formula = 'jikwon_pay ~ jikwon_ibsail', data = df).fit()
    #print(model3.summary())
    pred3 = model3.predict()
    
    print("실제값 : ", df[:5])
    print("예측값 : ", pred3[:5])
    
    year = int(input('근무년수를 입력하세요.'))
    newdf = pd.DataFrame({'jikwon_ibsail' : [year]})
    print('근무년수를 통한 예상연봉 :', model3.predict(newdf).values)
    
    # 차원확대, 축소로 맞춰주는것을 좀 해야한다.
    # x = df.jikwon_ibsail
    # y = df.jikwon_pay
    # model = stats.linregress(x, y)
    # np.ravel(np.polyval([model.slope, model.intercept], newdf)) # 예측값 ravel은 차원축소
    
except Exception as e:
    print("err : ", str(e))
finally:
    cursor.close()
    conn.close()