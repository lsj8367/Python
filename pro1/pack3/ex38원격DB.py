# 원격 DBMS와 연동 : MariaDB
import MySQLdb

# 연결하는 기본 방법
# conn = MySQLdb.connect(host = '127.0.0.1', user = 'root', password='123', database='test')
# print(conn) # <_mysql.connection open to '127.0.0.1' at 000001FAEB9DB710> 접속완료
# 
# conn.close

# with.open으로 파일을 열어 연결도 가능하다.
# conn.commit()은 select 문 빼고 다 써준다.

# 연결 정보를 dict type
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
    conn = MySQLdb.connect(**config) # dict type은 **하고 넘겨줌
    cursor = conn.cursor()
    
    # 자료 추가
    #sql = "insert into sangdata(code,sang,su,dan) values(20, '신상1', 5, 50000)"
    #cursor.execute(sql)
    
    '''
    sql = "insert into sangdata(code,sang,su,dan) values(%s,%s,%s,%s)" #sql 자체가 문자열이라서 %s로 넣어줘야함
    #sql_data = (21, '신상2', 10, 2500)
    sql_data = 21, '신상2', 10, 2500 # 위랑 이거랑 둘다 가능
    result = cursor.execute(sql, sql_data) # 문자열 + 매핑
    print('result : ', result)
    
    conn.commit() # 안해주면 데이터 안들어감!!!
    '''
    
    # 자료 수정
    '''
    sql = "update sangdata set sang=%s, su=%s, dan=%s where code=%s"
    sql_data = ('마스크', 100, 70000, 21)
    
    result = cursor.execute(sql, sql_data) # 문자열 + 매핑
    print('수정 result : ', result)
    conn.commit()
    '''
    # 자료 삭제
    code = '21'
    #sql = "delete from sangdata where code=" + code # 써도 되는데 권장 X
    
    #sql = "delete from sangdata where code=%s" # 권장 1!!!!
    #cursor.execute(sql, (code,)) # 한값만 들어갈때는 ,를 꼭 써주자
    
    sql = "delete from sangdata where code='{}'".format(code) # 권장2
    res = cursor.execute(sql)
    print("삭제 res: ", res)
    conn.commit() # 여기는 수동커밋인가봐
    
    
    
    # 자료읽기 : 방법1
    print("자료읽기-----------")
    sql = "select code, sang, su, dan from sangdata"
    cursor.execute(sql)
    
    for data in cursor.fetchall():
        #print(data)
        print("%s %s %s %s"%data)
    
    # print()
    # 자료읽기 : 방법 2
    '''
    for r in cursor:
        print(r[0], r[1], r[2], r[3])
        
    print()
    # 방법 3
    for (code, sang, su, dan) in cursor: # 칼럼매핑이아니고 순서대로 변수매핑 하는것
        print(code, sang, su, dan)
    
    # 방법 3-1
    for (a, b, 수량, 단가) in cursor: # 이렇게 해도 실행이 된다. 변수매핑이기 때문.
        print(a, b, 수량, 단가)
    '''
except Exception as e:
    print('err : ' + str(e))
finally:
    cursor.close()
    conn.close()
