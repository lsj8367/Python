# constant(), Variable(), function
import tensorflow as tf
import numpy as np

a = 10
print(type(a))
b = tf.constant(10) # 묵시적 Graph 객체에 포함된 멤버
print(b, type(b))
c = tf.Variable(10)
print(c, type(c))

print()
'''
g1 = tf.Graph()
with g1.as_default():
    #bb = tf.constant(10)
    bb = tf.Variable(10)
    print(bb)
    print(type(bb))
    print(bb.op)
    print('---')
    print(g1.as_graph_def())
'''
node1 = tf.constant(3.0, tf.float32)
node2 = tf.Variable(3.0)
print(node1, node1.numpy()) # tensor에서 numpy로 바꾸고싶을때 .numpy()
print(node2, node2.numpy())
node3 = node1 + node2
print(node3)
node4 = tf.add(node1, node2)
print(node4)

print('--------------------')
v = tf.Variable(1)

@tf.function
def find_next_odd():
    v.assign(v + 1)
    if tf.equal(v % 2, 0): # 2로 나눈값이 0 일때
        v.assign(v + 10)

find_next_odd()
print(v, ' ', v.numpy())

print('--------------------')
def func():
    #imsi = tf.constant(0) # imsi = 0도 상관없음
    imsi = tf.Variable(0)
    su = 1
    for _ in range(3):
        imsi = tf.add(imsi, su)
        #imsi = imsi + su
        #imsi += su # 참조형(Variable)일 경우 동작하지 않음.
        print(imsi)
    return imsi

kbs = func()
print(kbs.numpy(), ' ', np.array(kbs))

print('***************')

imsi = tf.constant(0)

@tf.function
def func2():
    global imsi
    su = 1
    for _ in range(3):
        imsi = tf.add(imsi, su)
    return imsi

mbc = func2()
print(mbc.numpy(), ' ', np.array(mbc))

print('***************')

def func3():
    imsi = tf.Variable(0)
    su = 1
    for _ in range(3):
        #imsi = tf.add(imsi, su)
        imsi.assign_add(su)
    return imsi

ytn = func3()
print(ytn.numpy(), ' ', np.array(ytn))

print('***************')
imsi = tf.Variable(0)
@tf.function
def func4():
#     imsi = tf.Variable(0)
    su = 1
    for _ in range(3):
        #imsi = tf.add(imsi, su)
        imsi.assign_add(su)
    return imsi

tvn = func4()
print(tvn.numpy(), ' ', np.array(tvn))

print('구구단 출력')
@tf.function # auto_graph 내에선 서식사용 불가
def gugu1(dan): 
    su = 0
    for _ in range(9):
        su = tf.add(su, 1)
        print(su)
        #print(su.numpy()) # tf.function일때 에러
        #print('{} * {} = {:2}'.format(dan, su, dan * su)) # auto-graph니까 서식 불가
        
gugu1(3)
