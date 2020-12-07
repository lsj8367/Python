'''
연산자
'''
from builtins import divmod

# print() 문 사용 연습

print(format(1.5678, '10.3f'))
print('나는 나이가 %d 이다.'%23)
print('나는 나이가 %s 이다.'%'스물셋')
print('나는 나이가 %d 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 나이가 %s 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 키가 %f이고, 에너지가 %d%%.'%(177.7, 100))
print('이름은 {0}, 나이는 {1}'.format('한국인', 33))
print('이름은 {}, 나이는 {}'.format('신선해', 33))
print('이름은 {1}, 나이는 {0}'.format(34, '강나루'))

print()
v1 = 3
print(v1)
v1 = v2 = v3 = 5
print(v1, v2, v3)
print('출력1', end=',') #계속 이어서 출력
print('출력2\n출력3') # 기본적으로 \n이 들어가있다

v1 = 1,2,3
print(v1)
v1, v2 = 100, 200
print(v1, v2)
v2, v1 = v1, v2
print(v1, v2)

print('값 할당용 packing')
v1, *v2 = 1,2,3,4,5 # 맨처음 변수만 v1이 가지고 뒤는 리스트형식으로 v2가 가짐
print(v1)
print(v2)

*v1, v2, v3= 1,2,3,4,5 # 마지막 변수만 v2가 가지고 앞은 v1이 전부 다 가져감
print(v1)
print(v2)
print(v3)
print('연산자---')
print(5 + 3, 5 - 3, 5 * 3, 5 / 3, 5 // 3, 5 % 3, 5 ** 3)
print('나누기의 경우 몫과 나머지 얻기 : ', divmod(5,3))
print(1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 123456789123456789)
print('우선순위 : ', 3 + 4 * 5, ((3 + 4) * 5))

print('관계연산자 ----')
print(5 > 3, 5 == 3, 5 != 3)
print("논리 연산자 ------")
print(5 > 3 and 4 > 3, 5 > 3 or 4 < 3, not(5 >= 3))

print('문자열 더하기 --------')
print('한' + '국' + '만세')
print('대한민국' * 10)

print('누적------')
a = 10
a = a + 1
a += 1
# ++a, a-- 자바의 증감연산자 파이썬에서는 사용이 불가
print("a : ", a)

print("부호 변경: ", a, a * -1, -a, --a, +a, ++a)

print("bool 처리: ", bool(True), bool(False))
print("bool 처리: ", bool(0), bool(1.5), bool(None), bool([]), bool({}), bool(set()))
print('bool 처리 : ', bool(1), bool(-12))

print('이스케이프문자-------')
print('aa\tbb')
print('aa\bbb')
print('aa\nbb')
print('c:\abc\nbc\tbc\good.txt')
print(r'c:\abc\nbc\tbc\good.txt') # r을 선행하면 \를 해석하지 않는다.

