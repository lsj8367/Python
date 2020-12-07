'''
Module의 멤버 중 class의 이해 (객체 운영)
클래스의 멤버로 메소드와 변수
접근지정자 없다.
메소드 오버로딩 없다
다중 상속이 가능하다 자바의 interface X
'''
print('어떤것을 수행 후 oop를 사용하고 싶다면')

a = 123
print(type(a))

class TestClass:
    aa = 1 # 클래스의 멤버변수(전역) - prototype
    
    def __init__(self): # 오버로딩 기능은 지원하지 않는다.
        print('생성자')
        
#     def __del__(self):
#         print('소멸자')
        
    def myMethod(self):
        name = '한국인'
        print(name)
        print(self.aa)
        
print('class의 멤버변수 aa : ' , TestClass.aa) # 자바처럼 TestClass ### = new TestClass(); 안하고 그냥 바로 클래스 하위 멤버변수를 부를수있다.
# TestClass.myMethod(a)

test = TestClass() # 생성자를 호출. TestClass type의 객체가 생성 ()안써주면 class의 주소를 치환한것
print(test.aa)
test.myMethod()

print('\n메소드 호출 방법')
TestClass.myMethod(test) # 방법 1 : UnBound Method Call
test.myMethod() # 방법 2 : Bound Method Call

print('클래스 타입 : ', isinstance(test, TestClass)) # True

print()
print(type(1))
print(type(test))
print(id(test), id(TestClass))

print('\n\n클래스 연습 2')
class Car:
    handle = 0
    speed = 0
    
    def __init__(self, name, speed):
        self.name = name # this.name = name; 과 같음
        self.speed = speed
        
    def showData(self):
        km = '킬로미터' # 지역변수 메소드 내에서만 쓰임
        msg = '속도 : ' + str(self.speed) + km
        return msg

print(Car.handle, Car.speed)

car1 = Car('Paul', 10)
print(car1.handle, car1.name, car1.speed) # 핸들값은 car1에서 없을때 원래 정의된 클래스의 값을 쓴다
car1.color = '검정' # car1 객체에 color 변수 추가
print(car1.color) # car1 객체에만 color가 있는거라서 아래의  Car.color는 에러가 나게된다.

# print(Car.color) # AttributeError: type object 'Car' has no attribute 'color'

print()
car2 = Car('james', 20)
print(car2.handle, car2.name, car2.speed)
# print(car2.color) # AttributeError: type object 'Car' has no attribute 'color'

print('주소 출력 : ', Car, car1, car2)
print('주소 출력 : ', id(Car), id(car1), id(car2))

print(car1.__dict__) # 각 객체의 멤버 확인
print(car2.__dict__)

print('메소드 호출')
print('car1 => ', car1.showData())
print('car2 => ', car2.showData())
car1.speed = 50
car2.speed = 100
print('car1 => ', car1.showData())
print('car2 => ', car2.showData())
print('car1 => ', car1.speed)
print('car2 => ', car2.speed)







