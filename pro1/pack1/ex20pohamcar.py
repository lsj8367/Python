# 클래스의 포함관계 - 핸들 클래스를 별도 작성 후 호출
from pack1.ex20handle import PohamHandle

class PohamCar:
    turnShow = '정지'
    
    def __init__(self, ownerName):
        self.ownerName = ownerName
        self.handle = PohamHandle() # 클래스의 포함
        
        
    def TurnHandle(self, q):
        if q > 0:
            self.turnShow = self.handle.RightTurn(q)
        elif q < 0:
            self.turnShow = self.handle.LeftTurn(q)
        elif q == 0:
            self.turnShow = "직진"

# 응용 프로그램의 시작점 : 가독성          
if __name__ == "__main__": # 메인모듈인지 여부 확인
    tom = PohamCar('tom')
    tom.TurnHandle(10)
    print(tom.ownerName + '의 회전량은 ' + tom.turnShow + str(tom.handle.quantity))

    tom.TurnHandle(-20)
    print(tom.ownerName + '의 회전량은 ' + tom.turnShow + str(tom.handle.quantity))
    
    print()
    john = PohamCar('john')
    john.TurnHandle(0)
    print(john.ownerName + '의 회전량은 ' + john.turnShow + str(john.handle.quantity))