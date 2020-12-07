# 키보드로 부서번호를 입력받아 해당 부서의 직원 출력
import MySQLdb
import sys

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    
    buser = input('부서번호 입력 : ')
    sql = '''
        select jikwon_no, jikwon_name, buser_num, jikwon_jik
        from jikwon
        where buser_num={0}
    '''.format(buser)
    
    # print(sql)
    
    cursor.execute(sql)
    datas = cursor.fetchall()
    
    if len(datas) == 0:
        print(buser + '번 부서는 없는 번호입니다.')
        sys.exit() # 프로그램 강제 종료
    for d in datas:
        print(d[0], d[1], d[2], d[3])
    
    print("인원 수 : " + str(len(datas)))

except Exception as e:
    print('err : ' + str(e))
finally:
    conn.close()
    