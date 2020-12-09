# -*- coding: utf-8 -*-
"""exnp3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_JOSJt2fGu909asHLzBSs2utOFQHTjdA
"""

# 배열 연산 : +,-,*,/ 또는 numpy의 add, subtract, multiply, divide 함수 사용도 가능함.
import numpy as np

x = np.array([[1,2],[3,4]], dtype = np.float64)
y = np.arange(5, 9).reshape((2, 2)) # 1행4열 모양을 2행2열로 변경함
y = y.astype(np.float64) # 구조를 바꿈
print(x, x.dtype)
print(y, y.dtype)
print()
print(x + y)
print(np.add(x,y))

print()
print(x - y)
print(np.subtract(x,y))

print()
print(x * y)
print(np.multiply(x,y))

print()
print(x / y)
print(np.divide(x,y))

# 계산 속도 참고
big_arr = np.random.rand(1000000)
print(big_arr)

# Commented out IPython magic to ensure Python compatibility.
# %timeit sum(big_arr) # 파이썬 내장함수

# Commented out IPython magic to ensure Python compatibility.
# %timeit np.sum(big_arr) # numpy 내장함수

# 행렬곱, 벡터 내적 연산
print(x)
print(y)
v = np.array([9, 10])
w = np.array([11, 12])
print(v)
print(w)
print()
print(v * w) # 벡터의 곱
print(v.dot(w))  # R : v %*% w
print(np.dot(v, w))
print()
print(x.dot(v))
print(np.dot(x, v))
print()
print(np.dot(x, y))

# min(), max(), argmin() 인덱스값만 얻는것, sqrt() 루트, cumsum() 누적합, cumprod() 누적곱, ...

names = np.array(['tom', 'james', 'tom', 'oscar'])
names2 = np.array(['tom', 'page', 'john'])
print(np.unique(names)) # 중복 배제
print(np.intersect1d(names, names2)) # 교집합, 중복 허용 X
print(np.intersect1d(names, names2, assume_unique=True)) # 교집합, 중복 허용됨
print(np.union1d(names, names2)) # 합집합

print(x)
print(x.T) # 전치함수
print(x.transpose()) # 행과 열을 바꿔줌
print(x.swapaxes(0, 1)) # 행과 열을 바꿔줌

# Broadcasting : 크기가 다른 배열간의 자동 연산
x = np.arange(1, 10).reshape(3,3)
print(x)
y = np.array([1, 0, 1])
z = np.empty_like(x) # x행렬과 같은크기의 배열 만들기
print(y)
print(z)
print() # 반복문을 사용해 x의 각 행에 y벡터를 더해서 z에 기억
for i in range(3):
  z[i] = x[i] + y
print(z)

print("numpy는 broadcasting 연산")
# 행 + 열 하면 그 행과열 최대크기에 맞춰서 연산함
z = x + y
print(z)

print(x)
np.save('test', x) # 단수객체 #배열객체 file i/o
np.savez('test', x) # 복수객체
np.savetxt('test.txt', x)
imsi = np.load('test.npy')
print(imsi)
print()
ourdata = np.loadtxt('our.txt', delimiter=',')
print(ourdata)