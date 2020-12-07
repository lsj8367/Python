'''
사용자 정의 모듈 연습
'''
print('뭔가를 하다가... 사용자 정의 모듈 호출 시도')

import pack1.mymod1

list1 = [1, 3]
list2 = [2, 4]

pack1.mymod1.listHap(list1, list2)

def good():
    if __name__ == '__main__': #시스템명령은 __ 로 사용
        print('최상위 메인 모듈')

good()

print('tot 는', pack1.mymod1.tot)
pack1.mymod1.kbs()
from pack1.mymod1 import mbc
mbc()

print()
from pack1etc.mymod2 import Hap, Cha
print('Hap : ', Hap(5, 2))
print('Cha : ', Cha(5, 2))

print('mymod3.py는 파이썬 PythonPath 폴더 중 어딘가에  저장한 상태')
from mymod3 import Gop
print('Gop : ', Gop(5, 2))

# 참고 : colab에서 실습할 경우
# 순서1) mymod1.ipynb 파일을 작성 한 후 메뉴에서 '파일' -> .py 로 다운로드한후
# 순서2) from google.colab import files
# 순서3) files.upload() 해서 파일 선택하는 화면 나오면 mymod1.py선택
# 순서4) from mymod1 import 







