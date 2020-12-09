import numpy as np
from pandas import Series, DataFrame
'''
pandas 문제 1)
  a) 표준정규분포를 따르는 9 X 4 형태의 DataFrame을 생성하시오
  b) a에서 생성한 DataFrame의 칼럼 이름을 - No1, No2, No2, No4로 지정하시오
  c) 각 컬럼의 평균을 구하시오
'''

data = DataFrame(np.random.randn(9, 4), columns = ['No1', 'No2', 'No3', 'No4'])
print(data) # , type(data)
print()
'''
for i in range(1,5):
    print('No',i, '컬럼의 평균', data['No' + str(i)].mean())

print()
'''

print(data.mean(axis=0))
print()

'''
pandas 문제 2)
numbers
a    10
b    20
c    30
d    40
a) DataFrame으로 위와 같은 자료를 만드시오. 컬럼 이름은 numbers, 로우 네임은 a~d, 값은 10~40
'''
    
ex2 = DataFrame([10,20,30,40], index=['a','b','c','d'], columns = ['numbers'])
# aaa = ex2.copy()
print(ex2)
print()
# b) c 로우의 값을 가져오시오.
print(ex2.loc[['c'], :])
print()
# c) a, d 로우들의 값을 가져오시오.
print(ex2.loc[['a','d']])
print() 
# d) numbers의 합을 구하시오.
print('numbers열 의 합 : ', ex2['numbers'].sum())
print()



# e) numbers의 값들을 각각 제곱하시오 아래 결과가 나와야 함.
# numbers
# a 100
# b 400 
# c 900
# d 1600
'''
list = ['a','b','c','d']
for i in list:
    aaa.loc[i,['numbers']] = ex2.loc[i,['numbers']] ** 2
print(aaa)
'''
# print(pow(ex2, 2)) # 아래와 같음
print(ex2 ** 2)

print()
# f) floats 라는 이름의 칼럼을 추가하시오. 값은 1.5, 2.5, 3.5, 4.5    아래 결과가 나와야 함.
#     numbers    floats 
# a    10        1.5
# b    20        2.5
# c    30        3.5
# d    40        4.5

ex2['floats'] = Series([1.5,2.5,3.5,4.5], index = ['a','b','c','d'])
print(ex2)

print()
# g) names라는 이름의 다음과 같은 칼럼을 위의 결과에 또 추가하시오.
#     names
# d    길동
# a    오정
# b    팔계
# c    오공
names = Series(['길동','오정','팔계','오공'], index = ['d','a','b','c'])
ex2['names'] = names
print(ex2)
