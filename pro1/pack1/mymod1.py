'''
main module에서 호출될 소스 코드
내가 만든 모듈
'''
tot = 123

def listHap(*ar):
    print(ar)
    if __name__ == '__main__': #시스템명령은 __ 로 사용
        print('최상위 모듈')
    
def kbs():
    print("대한민국 공영방송")
    
def mbc():
    print("mbc 문화방송")