'''
웹용 파이썬
'''
py_var = '파이썬 변수 값 출력'
py_var2 = 123

print('Content-Type:text/html;charset=utf-8\n')
print('<html><body>')
print('<h2>반가워요. 파이썬 웹 만세!</h2>')
print('<b>파이썬모듈</b>로 만든 문서입니다<br>')
print('변수 값 1 : %s'%(py_var))
print('<br>변수 값 2 : %d'%(py_var2))
print('</body></html>')


