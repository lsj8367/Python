'''
클래스
'''

kor = 100

def abc():
    print('모듈의 함수')
    
class MyClass:
    kor = 90
    
    def abc(self):
        print('난 메소드야')
    
    def show(self):
        # kor = 80
        print(self.kor)
        print(kor) # 현재 메소드에서 kor변수를 찾고, 없다면 모듈의 멤버를 참조한다.
        self.abc()
        abc() # 모듈의 함수 호출

myclass = MyClass()
myclass.show()

print('~~~' * 10)
class My:
    a = 1
    
print(My.a)


my1 = My()
print(my1.a)

my2 = My()
print(my2.a)
my2.b = 2
print(my2.b)

# print(my1.b) # AttributeError: 'My' object has no attribute 'b'
# print(My.b) # AttributeError: 'My' object has no attribute 'b'

















