# turtle 모듈을 이용하여 그래픽 처리
import turtle

# a = turtle.Pen() # 펜 객체한개 생성
# a.forward(100) # 오른쪽 100이동
# a.right(90) # 90도 회전
# a.forward(100)
# a.right(90)
# a.forward(100)
# a.right(90)
# a.forward(100)
# a.right(90)
# 
# # a.reset() # 초기화
# a.pencolor('blue')
# a.circle(50, 360) # 반지름, 회전각
# 
# a.up()
# a.forward(100)
# a.write('문자그리기', True, 'left', font=('돋움', 30, 'normal'))
# 
# 
# 
# 
# input()


from turtle import *
p = Pen()
p.color('red', 'yellow')
p.begin_fill()
while True:
    p.forward(200)
    p.left(170)
    if abs(p.pos()) < 1:
        break
p.end_fill()
done()





