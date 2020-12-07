'''
클래스의 상속
'''
class Animal:
    age = 0
    def __init__(self):
        print('Animal 생성자')
        
    def move(self):
        print('움직이는 생물')

class Dog(Animal): # 클래스명 뒤에 ()안에 클래스 넣어주면 상속
    def __init__(self): # 자식이 생성자를 갖고 있다면 부모생성자는 호출하지 않는 이상 수행되지 않는다.
        print('Dog 생성자')
    
    def my(self):
        print('댕댕이라 불러줘')

dog1 = Dog()
dog1.my()
dog1.move()

print()
class Horse(Animal):
    pass
horse1 = Horse()
horse1.move()