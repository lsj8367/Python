# 연산자와 함수 일부 확인
import tensorflow as tf
import numpy as np

x = tf.constant(7)
y = 3
# tf.cond(조건, 함수1, 함수2) 3항연산
result1 = tf.cond(x > y, lambda: tf.add(x, y), lambda: tf.subtract(x, y))
print(result1.numpy())

print()
f1 = lambda:tf.constant(1)
print(f1())
f2 = lambda:tf.constant(2)
a = tf.constant(3)
b = tf.constant(4)
result2 = tf.case([(tf.less(a, b), f1)], default = f2) # if a < b return 1 else 2
print(result2.numpy())
 
print()
print(tf.equal(1, 2).numpy())
print(tf.not_equal(1, 2))
print(tf.less(1, 2))
print(tf.greater(1, 2))
print(tf.greater_equal(1, 2))

print()
# and, or, not
print(tf.logical_and(True, False).numpy())
print(tf.logical_or(True, False))
print(tf.logical_not(True))

print()
ar = [[1, 2], [3, 4]]
print(tf.reduce_mean(ar).numpy())
print(tf.reduce_mean(ar, axis = 0).numpy())
print(tf.reduce_mean(ar, axis = 1).numpy())

print()
t = np.array([[[0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]])
print(t.shape) # 2면 2행 3열
print(tf.reshape(t, shape = [2, 6])) # 차원축소
print(tf.reshape(t, shape = [-1, 6]))
print(tf.reshape(t, shape = [2, -1]))

print()
print(tf.squeeze(t)) # 차원축소 함수 (열 요소수가 1개인 경우만 해당)
print()
aa = np.array([[1],[2],[3],[4]])
print(aa, aa.shape)
bb = tf.squeeze(aa) # 차원축소
print(bb.numpy(), bb.shape)

print()
tarr = tf.constant([[1, 2, 3], [4, 5, 6]])
print(tarr.shape) # (2, 3)
sbs = tf.expand_dims(tarr, 0) # 첫번째 차원을 추가해 확장함     # 면 행 열 순서대로 면 =0, 행 =1, 열 =2를 dims에 인자로 넣어줌 원래 행렬 사이로 들어감
print(sbs.numpy(), sbs.shape)

print()
sbs = tf.expand_dims(tarr, 1) # 두번째 차원을 추가해 확장함
print(sbs.numpy(), sbs.shape) # (1, 2, 3)

print()
sbs = tf.expand_dims(tarr, 2) # 세번째 차원을 추가해 확장함
print(sbs.numpy(), sbs.shape)

print()
sbs = tf.expand_dims(tarr, -1) # 세번째 차원을 추가해 확장함
print(sbs.numpy(), sbs.shape)
