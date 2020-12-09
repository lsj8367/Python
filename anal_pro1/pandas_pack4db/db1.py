# DB 자료(RDBMS) 연동 후 DataFrame으로 객체화
# sqllite3
import sqlite3
import pandas as pd
sql = "create table if not exists test(product varchar(10), maker varchar(10), weight real, price integer)"

conn = sqlite3.connect(':memory:') # Ram에다가 DB생성

conn.execute(sql)
conn.commit()

data = [('mouse','samsung', 12.5, 15000), ("keyboard", "lg", 500.5, 55000)]
stmt = "insert into test values(?,?,?,?)"
conn.executemany(stmt, data)
data1 = ('book', 'hanbit', 1000, 35000)
conn.execute(stmt, data1)
data2 = 'pen', 'monami', 100, 1000
conn.execute(stmt, data2)
conn.commit()

cursor = conn.execute("select * from test")
rows = cursor.fetchall()
for a in rows:
    print(a)

print('\ntest 테이블 자료를 DataFrame으로 저장')
#df1 = pd.DataFrame(rows, columns = ['상품명', '제조사', '무게', '가격'])
df1 = pd.DataFrame(rows, columns = list(zip(*cursor.description))[0])
print(df1)
print(*cursor.description) # [0]번째로 칼럼명 사용도 가능함
# ('product', None, None, None, None, None, None) ('maker', None, None, None, None, None, None) ('weight', None, None, None, None, None, None) ('price', None, None, None, None, None, None)

print()
df2 = pd.read_sql("select * from test", conn)
print(df2)
#print(df2.to_html())
cursor.close()
conn.close()


# DataFrame을 DB로 저장하기
# data = {
#     'irum' : ['신기해','홍길동', '강나루'],
#     'nai' : [22, 25, 32],
#     }
# frame = pd.DataFrame(data)
conn = sqlite3.connect('test.db')
# frame.to_sql('mytable', conn, if_exists = "append", index = False)


# 읽기
df3 = pd.read_sql("select * from mytable", conn)
print(df3)





