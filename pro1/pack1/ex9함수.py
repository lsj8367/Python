# 변수의 생존범위 Local > Enclosing function > Global

player = '국가대표' # 전역변수 : 현재 모듈의 어디서든 참조가 가능함.

def funcSoccer():
    name = '손흥민'
    player = '동네대표' # 지역변수 함수 내에서만 한정
    print(name, player)

funcSoccer()

print('-------------')
a = 10; b = 20; c = 30
print('1. a:{}, b:{}, c:{}'.format(a,b,c))

def kbs():
    a = 40 # 지역변수
    b = 50
    def mbc(): # 내부함수
         
        global c # 전역변수 c
        nonlocal b # 한단계 상위 함수 수준
        
        #c = 60 # 지역
        print('2. a:{}, b:{}, c:{}'.format(a,b,c))
        c = 60 # 지역변수인데 null값을 준거와 같음 UnboundLocalError: local variable 'c' referenced before assignment
        b = 70
    mbc()
    a = 80
    b = 90
    c = 100
    
kbs()
print('3. a:{}, b:{}, c:{}'.format(a,b,c))

print()
v1 = 1
def varTest(v1):
    v1 = v1 + 1
    print(v1)
    
varTest(v1)

print()
g = 1

def func1():
    global g # 주의
    a = g
    g = 2 # 이렇게 주면 지역변수처럼 알음
    return a

print(func1())

print("go" * 5)
# 인수(argument) 키워드로 매핑

def ShowGugu(start = 1, end = 5):
    for dan in range(start, end + 1):
        print(str(dan) + '단 출력')
        
ShowGugu(2, 7)
print()
ShowGugu(3) # 기본 end값은 5로 되어있어서 3,4,5 출력됨
print()
ShowGugu()
print()
ShowGugu(start = 2, end = 3)
print()
ShowGugu(end = 3, start = 2) #파라미터 인자를 따라가기 때문에 바꾸어 써도 상관없다.
print()
ShowGugu(2, end = 3)
print()
# ShowGugu(start = 2, 3) # err : SyntaxError: positional argument follows keyword argument
# ShowGugu(end = 4, 3) # err : SyntaxError: positional argument follows keyword argument

print('가변 인수 처리')
def fu1(*ar): #pass시킬거면 pass
    # print(ar)
    for i in ar:
        print('국없이 먹는 밥 : ' + i)
fu1()
print()
fu1('김밥')
print()
fu1('김밥', '비빔밥')
print()
fu1('김밥', '비빔밥', '주먹밥')

print()
def fu2(a, *ar):
    print(a)
    print(ar)
fu2('김밥', '비빔밥', '주먹밥')

print()

# def fu3(*ar, a): # TypeError: fu3() missing 1 required keyword-only argument: 'a'
#     print(ar)
#     print(a)
# fu3('김밥', '비빔밥', '주먹밥')

def selProcess(choice, *ar):
    if choice == '+':
        re = 0
        for i in ar:
            re += i
    elif choice == '*':
        re = 1
        for i in ar:
            re *= i 
    return re
print(selProcess('+', 1, 2, 3, 4, 5))
print(selProcess('*', 1, 2, 3, 4, 5))

print()
def fu4(w, *h, **other): # **은 하위 키밸류를 dict화 한다.
    print('몸무게{}'.format(w))
    print('키:',h)
    print(other)

#fu4(66, 160, {'irum':'지구인', 'nai':22})
fu4(66, 160, 170, irum='지구인', nai=22)
# 몸무게66
# 키: (160, 170)
# {'irum': '지구인', 'nai': 22}

print('\n-----------------closure------------------')
def abc(a, b):
    cc = a * b
    #print(c)
    return cc

print(abc(2, 3))
# print(cc) # NameError: name 'cc' is not defined
ytn = abc # 주소를 치환받음
print(ytn(2, 3))

del abc # 함수명을 삭제 : 참조 객체는 메모리에 남아있다

# print(abc(2, 3)) # NameError: name 'abc' is not defined
print(ytn(2, 3)) # 함수명을 지운거지 참조객체는 살아있기때문에 ytn은 동작
tvn = ytn

print(tvn(2, 3))

print("-----------------")
def out():
    count = 0
    def inn(): # 내부함수
        nonlocal count
        count += 1
        return count
    print(inn())
#print(count)
out()
out()

print()

def outer():
    count = 0
    def inner(): # 내부함수
        nonlocal count
        count += 1
        return count
    return inner # <== 이것을 클로저라고 한다(내부 함수를 반환)

inner_func_addr = outer() # inner의 주소를 가졌음
print(inner_func_addr)
print(inner_func_addr())
print(inner_func_addr())
print(inner_func_addr())
print()
inner_func_addr2 = outer() # 새로운 주소라서  inner_func_addr 과 다르기 때문에 새로 누적한다
print(inner_func_addr2())
print(inner_func_addr2())

print('수량 * 단가 * 세금 결과 출력하기')
def outer2(tax):
    def inner2(su, dan):
        amount = su * dan * tax
        return amount
    return inner2

r = outer2(0.1) # 세금 : 10%
result1 = r(5, 10000)
print(result1)
result2 = r(10, 20000)
print(result2)

print()
r2 = outer2(0.05) # 세금 : 10%
result3 = r2(5, 10000)
print(result3)








