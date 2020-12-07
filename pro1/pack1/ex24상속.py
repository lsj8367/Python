# 상속
class Person:
    say = '난 사람이야 ~'
    nai = 20
    __kbs = 'good' # 변수앞에 __를 주게되면 private 멤버변수가 된다. = 현재클래스에서만 호출이 가능하다.
    
    def __init__(self, nai):
        print('Person 생성자')
        self.nai = nai
    
    def PrintInfo(self):
        print('나이 :{}, 이야기:{}'.format(self.nai, self.say))
        
    def Hello(self):
        print('안녕')
        print('Hello에서 kbs 출력 ', self.__kbs)
    
    @staticmethod
    def sbs(tel): # static method
        print('sbs - static method : ', tel)
        # print(self.say) # 클래스 멤버 호출불가능 , 해당 클래스 멤버에 상관없는 독립적 처리에 사용
    
    @classmethod
    def ytn(cls):
        print('Person이 가진 ytn 메소드', cls.say, cls.nai) # cls로 멤버에 접근이 가능
    
    
    
p = Person('22')
p.PrintInfo()
p.Hello()

print('---' * 20)

class Employee(Person):
    subject = '근로자'
    say = '일하는 동물'
    
    def __init__(self):
        print('Employee 생성자')
        
    def PrintInfo(self): # method override
        print('Employee 메소드')
        
    def EprintInfo(self):
        self.PrintInfo()
        super().PrintInfo() # 부모에게 가는것
        print(self.say, super().say)
        self.Hello()
        super().Hello()
        
e = Employee()
print(e.say, e.nai, e.subject)
e.PrintInfo()
e.EprintInfo()

print('------------')
class Worker(Person):
    def __init__(self, nai):
        # super().__init__(nai)
        print('Worker 생성자')
        super().__init__(nai) # BoundMethod Call 부모 생성자 호출 시 순서는 상관이 없다.
    def WprintInfo(self):
        self.PrintInfo()
        super().PrintInfo()
        
        
w = Worker('25')
print(w.say, w.nai)

w.PrintInfo()

w.WprintInfo()

print('***' * 20)

class Programmer(Worker):
    def __init__(self, nai):
        print('Programmer 생성자')
        # super().__init__(nai)
        Worker.__init__(self, nai) # UnBound Method Call
    
    def WprintInfo(self):
        print("Programmer클래스 에서 Worker의 메소드를 오버라이딩")
        
    def abc(self):
        print('Programmer Hello에서 kbs 출력 ', self.__kbs)
        
pr = Programmer(33)
print(pr.say, pr.nai)
pr.PrintInfo()
pr.WprintInfo()

print('클래스 타입 확인')
a = 10
print(type(a))
print(Person.__bases__) # __bases__ -> 현재클래스의 부모클래스 확인
print(Employee.__bases__)
print(Programmer.__bases__)

print()
# pr.abc() # AttributeError: 'Programmer' object has no attribute '_Programmer__kbs'
# 변수가있던 유효한 클래스에서만 사용이 가능함.

pr.sbs('010-1234-5678')
Person.sbs('010-2222-2222') # 권장 : 클래스 이름으로 호출

Person.ytn()

