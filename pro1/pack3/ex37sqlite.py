# sqlite3 : 내장된 개인용 Database
import sqlite3

def dbFunc(dbName):
    try:
        conn = sqlite3.connect(dbName)
        c = conn.cursor()
#         try:
#             c.execute("select * from jikwon")
#         except:
#             c.execute("create table jikwon(id integer primary key, name text)")
        
        
        
        
        c.execute("drop table jikwon")
        c.execute("create table jikwon(id integer primary key, name text)")
        # insert
        c.execute("insert into jikwon values(1, '홍길동')")
        
        tdata = (2, '고길동') # tuple type
        c.execute("insert into jikwon values(?,?)", tdata)
        
        tdata2 = 3, '나길동' # tuple type
        c.execute("insert into jikwon values(?,?)", tdata2)
        
        tdata3 = ((4, '관우'),(5, '장비')) # tuple type
        c.executemany("insert into jikwon values(?,?)", tdata3) # 여러개를 insert 해줄때는 executemany
        
        ldata = [6, '조운'] # list type (가능)
        c.execute("insert into jikwon values(?,?)", ldata)
        
        #sdata = {7, '삼장'} # set type은 안됨 ( X )
        #c.execute("insert into jikwon values(?,?)", sdata)
        
        dicData1 = {'id':7, 'name':'공기밥'} # dict type
        c.execute("insert into jikwon values(:id, :name)", dicData1) # ? 대신에 :키값으로 binding 해줘야함, 칼럼명 X
        
        dicData2 = {'sabun':8, 'irum':'고래밥'} # dict type
        c.execute("insert into jikwon values(:sabun, :irum)", dicData2) # ? 대신에 :키값으로 binding 해줘야함, 칼럼명 안들어가도됨
        
        conn.commit()
        
        # select
        print('출력 1')
        c.execute("select * from jikwon")
        for r in c:
            print(str(r[0]) + ' ' + r[1])
        
        print("출력 2 : 부분자료")
        #c.execute("select * from jikwon where id <= 2")
        # bun = 2
        #c.execute("select * from jikwon where id <= %d"%bun)
        ir = '홍길동'
        c.execute("select * from jikwon where name = '%s'"%ir)
        
        for r in c.fetchall():
            print(str(r[0]) + ' ' + r[1])
        
        
        print("출력 3 : sql 지원 함수사용")
        c.execute("select count(*) from jikwon")
        print('건수 : ' + str(c.fetchone()[0]))
        
        
        
        
    except Exception as e:
        print("err : " + str(e))
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    dbFunc('test.db')
    