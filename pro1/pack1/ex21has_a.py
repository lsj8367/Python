'''
로또번호 출력 : 클래스의 포함연습
'''
import random

class LottoBall:
    def __init__(self, num):
        self.num = num

class LottoMachine: # 45개의 공세팅
    def __init__(self):
        self.ballList = []
        for i in range(1, 46):
            self.ballList.append(LottoBall(i)) # 클래스의 포함관계
            
    def selectBalls(self): # 공을 담음
        # 섞기 전 공
        for a in range(45):
            print(self.ballList[a].num, end = " ")
        random.shuffle(self.ballList)
        print()
        # 섞은 후 공
        for a in range(45):
            print(self.ballList[a].num, end = " ")
        print()
        return self.ballList[0:6] # 0 ~ 6번째까지의 공
        

class LottoUi:
    def __init__(self):
        self.machine = LottoMachine() # 클래스의 포함관계
    
    def playLotto(self):
        input("로또를 뽑으려면 엔터키를 누르세요")
        selectBalls = self.machine.selectBalls()
        print("당첨번호 :", end = " ")
        for ball in selectBalls:
            print("%d"%(ball.num), end = " ")

if __name__ == "__main__":
    LottoUi().playLotto()

