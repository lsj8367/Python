# 연산자 및 내장 함수 오버라이드(재정의)
a = 10
b = 5
print(a + b, a - b)

class AddClass:
    def __init__(self, s):
        self.s = s
    
    def __add__(self, arg): # +에 대한 연산자 중복
        return "더하기 결과는 " + str(self.s + arg)

c1 = AddClass("kbs")
print(c1 + "mbc")        

c2 = AddClass("당신의 이름은 ")
print(c2 + "홍길동")

print("---------------")

class StrClass:
    def __init__(self, initdata):
        self.str = initdata
    
    def __sub__(self, other): # -에 대한 연산자 중복
        for i in other:
            self.str = self.str.replace(i, '')
            return StrClass(self.str)
        
    def __abs__(self): # abc() 내장함수를 재정의
        return StrClass(self.str.upper()) # 모든 문자를 대문자화하는 기능으로 변경
        
    
    def print_data(self):
        print(self.str)
        
c3 = StrClass('aBcdEfgHi Korea')
c3 = c3 - "aB"
c3.print_data()

c3 -= 'cdi'
c3.print_data()
print()
print(abs(-5), abs(5))
c3 = abs(c3)
c3.print_data()

print("\nSingleton-----")
class SingletonClass:
    inst = None
    def __new__(cls): # init 메소드에 의해 new가 호출됨
        if cls.inst is None:
            cls.inst = object.__new__(cls)
        return cls.inst
    def aa(self):
        print("aa 메소드")
    
class MySub(SingletonClass):
    pass

s1 = MySub()
s2 = MySub()
    
print(id(s1), id(s2)) # 주소가 같다 3081502011344 3081502011344

s1.aa()
s2.aa()

print("\n사용 가능한 멤버 고정 - 속성을 고정")
class Animal:
    # name = "a"
    # age = 22
    __slots__ = ['name', 'age']
    
    def printData(self):
        print(self.name, self.age)

m = Animal()
m.name = 'tiger'
m.age = 32
# m.eat = "동물"
m.printData()
# print(m.eat)







