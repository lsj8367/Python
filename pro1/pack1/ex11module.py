'''
Module : 소스 코드의 재사용을 가능하게 하며, 소스코드를 하나의 이름공간으로 구분하고 관리하는 단위
하나의 파일은 모듈단위로 저장되고 관리한다.
표준모듈, 사용자 작성 모듈, third party 모듈
'''
# 내장된 모듈 경험하기
print('뭔가를 하다가...')
import sys
print(sys.path)
# sys.exit() # 프로그램의 강제 종료

import math
print(math.pi)

print('뭔가를 하다가...')
import calendar
calendar.setfirstweekday(6) # 일요일을 첫요일로
calendar.prmonth(2020, 10)

print()
import random # module을 로딩
print(random.random())
print(random.randint(1, 10))

from random import random # from 모듈명 import 멤버 모듈의 멤버 로딩
# from random import * # 랜덤멤버 모두로딩
print(random())




print('프로그램 종료')
