# 연습문제
from abc import *

class Employee(metaclass = ABCMeta):
    def __init__(self, irum, nai):
        self.irum = irum
        self.nai = nai
    
    @abstractmethod
    def pay(self):
        pass
    
    @abstractmethod
    def data_print(self):
        pass
    
    def irumnai_print(self):
        print(self.irum + "님의 나이" + self.nai)
        
class Temporary(Employee):
    def __init__(self,irum, nai, ilsu, ildang):
        Employee.__init__(self, irum, nai)
        self.ilsu = ilsu
        self.ildang = ildang
        
    def pay(self):
        return self.ilsu * self.ildang
        
    def data_print(self):
        print(self.irumnai_print() + str(self.pay()))
        
        
    def irumnai_print(self):
        return "이름 : " + str(self.irum) +", 나이 : " + str(self.nai) + ", 월급 : "
    
    
class Regular(Employee):
    def __init__(self, irum, nai, salary):
        Employee.__init__(self, irum, nai)
        self.salary = salary
    
    def pay(self):
        return self.salary
    
    def data_print(self):
        print("이름 : " + str(self.irum) +", 나이 : " + str(self.nai) + ", 급여 : " + str(self.pay()))
    
class Salesman(Regular):
    def __init__(self, irum, nai, salary, sales, commission):
        Regular.__init__(self, irum, nai, salary)
        self.sales = sales
        self.commission = commission
    def pay(self):
        return int(self.salary + (self.sales * self.commission))
        
    def data_print(self):
        print("이름: " + self.irum + ", 나이 : " + str(self.nai) + ", 수령액: " + str(self.pay()))
        
        
t = Temporary("홍길동", 25, 20, 15000)
r = Regular("한국인", 27, 3500000)        
s = Salesman("손오공", 29, 1200000, 5000000, 0.25)
t.data_print()
r.data_print()
s.data_print()

    

