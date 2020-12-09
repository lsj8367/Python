# pandas 문제 5)
#  MariaDB에 저장된 jikwon, buser, gogek 테이블을 이용하여 아래의 문제에 답하시오.

import MySQLdb
import numpy as np
import pandas as pd
import ast
import csv

pd.set_option('display.max_columns', 500) # 생략없이 전체보기
with open('mariadb.txt', mode = 'r') as f:
    config = ast.literal_eval(f.read())
    #print(config, type(config))

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
        select jikwon_name, buser_name, jikwon_pay, jikwon_jik from jikwon
        inner join buser on buser.buser_no = jikwon.buser_num
        """
#    cursor.execute(sql)
    
#     for data in cursor.fetchall():
#         print(data)
        
#      - 사번 이름, 부서명, 연봉, 직급을 읽어 DataFrame을 작성    
    df = pd.read_sql(sql, conn)
    df.columns = '이름', '부서명', '연봉', '직급'
    df.index = range(1, 31)
    print(df, type(df))
    print()
    
#      - 부서명별 연봉의 합, 평균을 출력
    print("부서별 연봉의 합 : ", df.groupby(['부서명'])['연봉'].sum())
    print("부서별 연봉의 합 : ", df.groupby(['부서명'])['연봉'].mean())
    print()
    
#      - 부서명, 직급으로 교차테이블을 작성(crosstab)
    print("부서명, 직급으로 교차테이블을 작성(crosstab) :\n", pd.crosstab(df['부서명'], df['직급'], margins = True))

#      - 직원별 담당 고객자료를 출력
    #print(df.index[0]) # 1
    #print(len(df.index))
    #print(df['이름'][1])
    
    
    df1 = pd.DataFrame(columns=['고객번호', '고객명', '전화번호', '주민번호', '담당사원 번호'])
    df1.set_index('고객번호', inplace=True)
    
    for i in range(len(df.index)):
        sql2 = """
            select gogek_no, gogek_name, gogek_tel, gogek_jumin, gogek_damsano
            from gogek inner join jikwon on gogek.gogek_damsano = jikwon.jikwon_no
            where jikwon_no = {}
        """.format(str(df.index[i]))
        #print(sql)
        cursor.execute(sql2)
        
        
        result = cursor.fetchone()
            
        if result == None:
            print(df['이름'][i + 1],"직원의 담당 고객  X")
            print()
        else:
            print(df['이름'][i + 1], '직원의 담당 고객 정보')
            df2 = pd.read_sql(sql2, conn)
            df2.columns = ['고객번호', '고객명', '전화번호', '주민번호', '담당사원 번호']
            df2.set_index('고객번호', inplace=True)
            print(df2)
            print()
            df1 = df1.append(df2)
            
            #df = df.append(pd.DataFrame(df2[[i + 1], :]], columns=['고객번호', '고객명', '전화번호', '주민번호', '담당사원 번호']), ignore_index=True)
    
    #      - DataFrame의 자료를 파일로 저장
    print(df1)
    df.to_csv('ex_data.csv', index = False)

    df_re = pd.read_csv('ex_data.csv')
    print(df_re.head(3))


    
except Exception as e:
    print("err : ", str(e))
finally:
    cursor.close()
    conn.close()