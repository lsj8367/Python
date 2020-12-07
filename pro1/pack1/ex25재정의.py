# 메소드 오버라이드 : 다형성 구사

class Parent:
    def printData(self):
        pass

class Child1(Parent):
    def printData(self):
        print('Child1에서 오버라이드')

class Child2(Parent):
    def printData(self):
        print('Child2에서 재정의')
        print('부모 메소드와 이름은 동일하나 다른 기능을 갖는다')
    def abc(self):
        print('Child2의 고유메소드')


c1 = Child1()
c1.printData()
print()
c2 = Child2()
c2.printData()
c2.abc()

print('다형성 =========')
par = Parent()
par = c1
par.printData()

print()
kbs = c1 # 입력자료에 의해 변수타입이 결정된다.
kbs.printData()
print()
kbs = c2
kbs.printData()
kbs.abc()

print()
plist = [c1, c2]
for i in plist:
    i.printData()



