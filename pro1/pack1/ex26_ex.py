'''
연습문제
'''
class Animal:
    def move(self):
        pass

class Dog(Animal):
    name = '개'
    def move(self):
        print('dog move')

class Cat(Animal):
    name = "고양이"
    def move(self):
        print('cat move')

class Wolf(Dog, Cat):
    pass

class Fox(Dog, Cat):
    def move(self):
        print('fox move')
    def foxMethod(self):
        print('fox 고유 메소드')
dog = Dog()
cat = Cat()
wolf = Wolf()
fox = Fox()

# ani = [dog, cat, wolf, fox]
# ani = {dog, cat, wolf, fox} # 출력순서 무작위
ani = (dog, cat, wolf, fox)
for i in ani:
    i.move()