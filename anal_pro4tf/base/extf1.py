# 텐서플로우 기본 이해
import tensorflow as tf
print('즉시 실행모드 : ', tf.executing_eagerly())
print('GPU 사용 가능 여부 : ', tf.config.list_physical_devices('GPU'))
print(tf.test.is_gpu_available())
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices()) # 현재 CPU/GPU 목록확인

# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # AVX를 지원하지 않는다는 에러 발생시 기술

# 상수정의
print(1)
print(tf.constant(1))  #tf.Tensor(1, shape=(), dtype=int32) scala 0-D Tensor
print(tf.constant([1])) # tf.Tensor([1], shape=(1,), dtype=int32) vector 1-D Tensor 
print(tf.constant([[1]])) # tf.Tensor([[1]], shape=(1, 1), dtype=int32) matrix 2-D Tensor

print()
print(tf.rank(tf.constant([1])), ' ', tf.constant([1]).get_shape())

print()
a = tf.constant([1, 2])
b = tf.constant([3, 4])
c = a + b
print(c, type(c))
c = tf.add(a, b)
print(c, type(c))

print()
#d = 3
#d = tf.constant(3)
d = tf.constant([[3]])
e = c + d
print(e)

print()
print(7)
print(tf.convert_to_tensor(7))
print(tf.convert_to_tensor(7, dtype = tf.float32))
print(tf.cast(7, dtype = tf.float32))

print('numpy의 ndarray와 tensor 사이의 type 변환 ')
import numpy as np
arr = np.array([1, 2])
print(arr, ' ', type(arr))

tfarr = tf.add(arr, 5) # ndarray to tensor 자동 형변환
print(tfarr)
print(tfarr.numpy()) # tensor to ndarray 강제 형변환
print(np.add(tfarr, 3))
