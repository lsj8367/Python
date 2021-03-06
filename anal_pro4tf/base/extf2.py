# 변수
import tensorflow as tf
t = tf.Variable(1.0) # 실수/정수 변수형 텐서
v = tf.Variable(tf.ones((2,))) # 1.0짜리 2행
m = tf.Variable(tf.ones((2,)))
print(t, v, m)
print(t.numpy(), v.numpy(), m.numpy())

print()
v1 = tf.Variable(1)
v1.assign(10) # 변수에 값 할당
print('v1 :', v1, v1.numpy(), type(v1))

print()
v2 = tf.Variable(tf.ones(shape = (1)))
v2.assign([20])
print('v2:', v2)

print()
v3 = tf.Variable(tf.ones(shape = (1, 2)))
v3.assign([[30, 40]]) # 세션속 값을 변경하고 싶을때
print('v3:', v3)

print()
v1 = tf.Variable([3])
v2 = tf.Variable([5])
v3 = v1 * v2 + 10
print(v3)

print()
w = tf.Variable(tf.ones(shape = (1, )))
b = tf.Variable(tf.ones(shape = (1, )))
w.assign([2])
b.assign([2])

@tf.function    # auto graph : graph 객체로 만들어 짐. tf.Graph + tf.Session 형태에 맞는 함수 객체가 됨 # 이 데코레이터 없으면 그냥 파이썬의 함수
def func1(x):
    return w * x + b

out_a1 = func1([3])
print('out_a1: ', out_a1)

# 난수
rand = tf.random.uniform([4], 0, 1) # 균등 분포
print(rand)

rand2 = tf.random.normal([4], 0, 1) # 정규분포
print(rand2)


