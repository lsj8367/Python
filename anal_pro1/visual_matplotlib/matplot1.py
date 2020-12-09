# 시각화 모듈
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family = 'malgun gothic') # 한글 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False # 음수 부호 깨짐 방지
# %matplotlib inline ipython 기반 명령어 를 쓰면 show()명령어 안써도됨
'''
#x = [0, 1, 2]
#x = ['서울', '인천', '천안'] # list type(순서 O) x축에 순서로 표현
x = ('서울', '인천', '천안') # tuple type(순서 O)
#x = {'서울', '인천', '천안'} # set type(순서 X)
y = [5, 3, 7]
plt.xlim([-1, 3]) # x축 최대 최소 구간 설정
plt.ylim([0, 10])
plt.yticks(list(range(0, 11, 3))) # 인위적으로 y값 간격 조정

plt.plot(x, y) # x,y값 plt.scatter(x, y) 
plt.show()
'''

'''
data = np.arange(1, 11, 2)
print(data)
plt.plot(data) # y축에만 값을 부여
x = [0, 1, 2, 3, 4]
for a, b in zip(x, data):
    plt.text(a, b, str(b))

plt.show()

plt.plot(data)
plt.plot(data, data, 'r')
for a, b in zip(data, data):
    plt.text(a, b, str(b))
plt.show()
'''

'''
# 사인곡선
x = np.arange(10)
y = np.sin(x)
print(x, y)
#plt.plot(x, y, 'bo') # style 파랑 동그라미 형식 => bo
#plt.plot(y, 'r+')
plt.plot(x, y, 'go-.', marker= 'o', ms = 15, mec='g', mew = 5, mfc='r') #mec 바깥 색상, mfc 안쪽 색상

plt.show()
'''

"""
# hold명령 : 복수의 plot 명령을 하나의 그림에 겹쳐서 출력
x = np.arange(0, np.pi * 3, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin, 'r')
plt.scatter(x, y_cos)

plt.xlabel('x축')
plt.ylabel('y축')

plt.title('sin & cosine')
plt.legend(['sin', 'cosine'])
plt.show()
"""
"""
# subplot : Figure를 여러개의 영역으로 분리
x = np.arange(0, np.pi * 3, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.subplot(2, 1, 1) # 그래프 2행 1열 중 1번째 행에 포커스
plt.plot(x, y_sin)
plt.title('sine')

plt.subplot(2, 1, 2) # 그래프 2행 1열 중 1번째 행에 포커스
plt.plot(x, y_cos)
plt.title('cosine')
plt.show()
"""

# 꺾은선 차트를 그린 후 이미지 파일로 저장
irum = ['a','b','c','d','e']
kor = [80, 60, 70, 70, 90]
eng = [40, 70, 80, 70, 60]
plt.plot(irum, kor, 'ro-') # 빨강색 점에 실선
plt.plot(irum, eng, 'bs--') # 파랑 사각형에 점선
plt.ylim([30, 100])
plt.title('시험 점수')
plt.legend(['국어', '영어'], loc = 4) # loc 시계반대방향 위치주는것
plt.grid(True)

# 차트를 이미지로 저장하기
# fig = plt.gcf() # 저장준비 선언
# plt.show()
# fig.savefig('plot1.png')

# 이미지 읽기
from matplotlib.pyplot import imread
img = imread('plot1.png')
plt.imshow(img)
plt.show()





