'''
원격 DB와 연동 후 테이블 자료를 읽어 브라우저로 출력
'''
import MySQLdb
import ast

with open('mariadb.txt', mode='r') as f:
    config = ast.literal_eval(f.read())

print('Content-Type:text/html;charset=utf-8\n')
print('<html><body><h2>상품 자료(파이썬)</h2>')
print('<table>')
print('<tr><th>코드</th><th>상품명</th><th>수량</th><th>단가</th></tr>')
try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    cursor.execute("select * from sangdata")
    datas = cursor.fetchall()
    
    for code,sang,su,dan in datas:
        print('''
            <tr>
                <td>{0}</td>
                <td>{1}</td>
                <td>{2}</td>
                <td>{3}</td>
            </tr>
        '''.format(str(code), sang, su, dan))

except Exception as e:
    print('err : ' + str(e))
finally:
    cursor.close()
    conn.close()
    
print('</table></body></html>')