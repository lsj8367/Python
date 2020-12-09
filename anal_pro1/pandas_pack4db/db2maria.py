# 원격 DB 연동 후 테이블 자료를 읽어 DataFrame으로 객체화
import MySQLdb
import pandas as pd
import numpy as np
import ast
import csv

try:
    with open('mariadb.txt', mode = 'r') as f: # mode 옵션 r w rb
        config = f.read()
        print(config, type(config)) #  <class 'str'>
except Exception as e:
    print("read err : " + str(e))

config = ast.literal_eval(config) # dict type으로 변환
print(type(config))

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
        select jikwon_no, jikwon_name, buser_name, jikwon_jik, jikwon_gen, jikwon_pay from jikwon
        inner join buser on buser.buser_no = jikwon.buser_num
    """
    cursor.execute(sql)
    for(a,b,c,d,e,f) in cursor:
        print(a,b,c,d,e,f)
    """
    # table의 자료를 csv 파일로 저장
    with open('jik_data.csv', mode = 'w', encoding = 'utf-8') as fw: # 파일쓰기
        writer = csv.writer(fw)
        for row in cursor:
            writer.writerow(row)
        print('저장 완료')
    """
    
    # 읽기1 : csv 파일 -> dataFrame
    df1 = pd.read_csv('jik_data.csv', header = None, names=('번호', '이름', '부서','직급', '성별', '연봉'))
    print(df1.head(3))
    
    print()
    # 읽기 2 : SQL문 -> DataFrame
    df2 = pd.read_sql(sql, conn)
    df2.columns = '번호', '이름', '부서','직급', '성별', '연봉'
    print(df2.head(3))
    
    #print('전체 인원 수 : {}'.format(str(len(df2))))
    print("전체 인원 수 : ", len(df2), df2['이름'].count())
    print("직급별 인원 수 : ", df2['직급'].value_counts()) # 직급은 걍 카운트만 쓰면안 나옴
    print("부서별 인원 수 : ", df2['부서'].value_counts()) # 세부별로 조회안되고 그냥 전체 명수가 나옴
    print("연봉 평균 :", df2.loc[:, '연봉'].sum() / len(df2))
    print("연봉 평균 :", df2.loc[:,'연봉'].mean())
    print("연봉 요약 통계량 : ", df2.loc[:,['연봉']].describe())
    print("연봉이 8000 이상 : ", df2.loc[df2['연봉'] >= 8000])
    print("연봉이 5000 이상인 영업부 : ", df2.loc[(df2['연봉'] >= 5000) & (df2['부서'] == '영업부')])
    print("교차표 : " , pd.crosstab(df2['성별'], df2['직급'], margins = True)) # html로 출력 가능, Series X
    
    print()
    # 그룹화
    print(df2.groupby(['성별'])['이름'].count()) # 성별 인원수
    print(df2.groupby(['성별','직급'])['이름'].count()) # 성별/직급별 인원수
    
    # pivot_table : 성별내의 직급별 연봉 평균
    print(df2.pivot_table(['연봉'], index=['성별', '직급'], aggfunc=np.mean)) 
    
    # 시각화
    import matplotlib.pyplot as plt
    plt.rc('font', family = 'malgun gothic')
    
    jik_ypay = df2.groupby(['직급'])['연봉'].mean() # 직급에 대한 연봉
    print(jik_ypay.index)
    print(jik_ypay.values)    
    
    plt.pie(jik_ypay, labels = jik_ypay.index,
            labeldistance=0.5, # 글자 차트 안으로 넣기
            counterclock = False, # 시계반대 방향
            explode=(0.2, 0, 0, 0.3, 0), # 조각떼내기
            shadow = True # 음영주기
            )
    plt.show()
        
except Exception as e2:
    print("sql err : " + e2)
finally:
    cursor.close()
    conn.close()