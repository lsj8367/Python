from django.db import models

# Create your models here.
class Maker(models.Model):
    mname = models.CharField(max_length = 10)
    tel = models.CharField(max_length = 30)
    addr = models.CharField(max_length = 50)
    
    class Meta:
        ordering = ('-id',) # id 내림차순정렬
        
    def __str__(self):
        return self.mname
        
        
        
class Product(models.Model):
    pname = models.CharField(max_length = 10)
    price = models.IntegerField()
    maker_name = models.ForeignKey(Maker, on_delete = models.CASCADE) # 이렇게 설정해놓으면 Maker의 pk인 아이디값을 참조한다.
    # on_delete Maker가 지워지면 foreignkey도 같이 지워진다.
    