'''
client가 입력한 데이터를 접수
'''
import cgi

form = cgi.FieldStorage()  # 자료를 키, 밸류의 dict타입으로 받음

name = form['name'].value # java : request.getParameter("name") 와 같은기능을 함
phone = form['phone'].value
gender = form['gen'].value

print('Content-Type:text/html;charset=utf-8\n')
print('''
<html>
<body>
이름은 {0}, 전화는 {1}<br>
성별은 {2}
<hr>
<a href='../main.html'>메인으로</a>
</body>
</html>
'''.format(name, phone, gender))