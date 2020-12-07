# sqlite3 : 내장된 개인용 Database
import sqlite3

# print(sqlite3.sqlite_version_info)
# print()
#conn = sqlite3.connect('kbs.db') # db가 별도의 파일로 만들어짐
conn = sqlite3.connect(':memory:') # db자료가 램에만 존재하여 휘발성임, 연습용

try:
    cur = conn.cursor() # sql문 처리가 가능해짐
    
    # 테이블 작성
    cur.execute('create table if not exists friends(name text, phone text, addr text)')
    
    #자료 입력
    cur.execute("insert into friends(name, phone, addr) values('한국인', '111-1111', '서울')")
    cur.execute("insert into friends values('지구인', '222-2222', '서울')")
    cur.execute("insert into friends(name, phone, addr) values(?,?,?)", ('홍길동', '222-3333', '김포'))
    inputdata = ('손오공', '232-4444', '마포')
    cur.execute("insert into friends(name,phone,addr) values(?,?,?)", inputdata)
    conn.commit()
    print("입력 성공!")
    
    # 자료 읽기
    cur.execute("select * from friends")
    #print(cur.fetchone()) # 순서대로 1개씩 출력 ('한국인', '111-1111', '서울')
    #print(cur.fetchall()) # 전체읽기  [('한국인', '111-1111', '서울'), ('지구인', '222-2222', '서울'), ('홍길동', '222-3333', '김포'), ('손오공', '232-4444', '마포')]
    
    for r in cur:
        print(r[0] + ' ' + r[1] + ' ' + r[2])
    
except Exception as e:
    print('err : ' + str(e))
    conn.rollback()
finally:
    conn.close()
