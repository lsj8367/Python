# 추상클래스 : 추상메소드를 하나 이상 가진 경우 대체적으로 이를 추상클래스라 한다.
from abc import *

class AbstactClass(metaclass = ABCMeta): # 추상 클래스
    name = "난 AbstactClass"
    @abstractmethod # 추상메소드를 만드는 decorator
    def abcMethod(self): # 추상 메소드
        pass
    
    def normalMethod(self): # 일반 메소드
        print("추상 클래스 내의 일반 메소드")
        
# parent = AbstactClass() # err : Can't instantiate abstract class AbstactClass with abstract methods abcMethod
# 추상클래스는 인스턴스 할수 없다.

class Child1(AbstactClass): # 추상클래스를 상속 받았기때문에 추상 메소드를 반드시 override 하지 않으면 에러가 난다.
    name = "Child1"
    
    def abcMethod(self): # 반드시 override 해야하는 함수
        print('추상 메소드를 일반메소드로 오버라이딩 함')

class Child2(AbstactClass):
    def abcMethod(self):
        print("추상메소드를 Child2에서 오버라이딩")
    
    def normalMethod(self): # 오버라이딩이 선택적
        print("추상 클래스의 일반 메소드를 재정의함")
    
c1 = Child1()
print(c1.name)
c1.abcMethod()

print()
c2 = Child2()
print(c2.name)

c2.abcMethod() # BoundMethod Call
c2.normalMethod()


# 추상 클래스 타입의 변수 선언은 가능
parent = AbstactClass # 주소를 넘기는것은 가능하다
print(type(parent))


print() 
parent = c1 
parent.abcMethod()
print()
parent = c2 
parent.abcMethod()

print("\n\n추상연습 2")
class Friend(metaclass = ABCMeta):
    def __init__(self, name):
        self.name = name
            
    @abstractmethod
    def hobby(self):
        pass
    
    def printName(self):
        print("이름은" + self.name)

class John(Friend):
    def __init__(self, name, addr):
        Friend.__init__(self, name)
        self.addr = addr
        
    def hobby(self):
        print(self.addr + " 거리를 걸어다님")
        
    def printAddr(self):
        print("주소는 " + self.addr)

class Chris(Friend):
    def __init__(self, name, addr, age):
        Friend.__init__(self, name)
        self.addr = addr
        self.age = age
    
    def hobby(self):
        print(self.addr + " 동네를 뛰어다님")
        print(self.addr + " 살고  나이는 " + str(self.age) + "살임을 참고로 알림")
    

john = John('존', '역삼동')
john.printName()
john.hobby()
john.printAddr()

print("-------")
chris = Chris('크리스','신사동', 23) # 양 많을때는 \사용
chris.printName()
chris.hobby()










