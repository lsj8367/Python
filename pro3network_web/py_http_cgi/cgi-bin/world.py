# 웹용
ss1 = '문자열 1'
ss2 = '두번째 문자열 자료'
print('Content-Type:text/html;charset=utf-8\n')
print('''
<html>
<body>
자료 출력 : {0}, {1}
<br>
<img src='../images/logo.png' width='50%'/>
<br>
<a href='../main.html'>메인으로</a>
</body>
</html>
'''.format(ss1, ss2))