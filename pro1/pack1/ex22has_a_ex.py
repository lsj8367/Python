'''
연습문제
'''
class CoinIn:
    # coin = 0
    # cupcount = 0
    
    def __init__(self, coin):
        self.coin = coin
    
    def culc(self, cupcount):
        self.cupcount = cupcount
        
        
class Machine:
    cupcount = 1
    
    def showData(self, coin, cupcount):
        if coin < 200:
            print('요금이 부족합니다')
        elif coin - (200 * cupcount) < 0:
            print('원금 보다 많습니다.')
        elif coin >= 200:
            change = coin - (200 * cupcount)
            print('커피 ' + str(cupcount) + '잔 과 잔돈  ' + str(change) + '원')
    
gogo = CoinIn(input("넣는 금액 : "))
gogo.culc(input('몇잔 원하세요 : '))
m = Machine()
m.showData(int(gogo.coin), int(gogo.cupcount))

