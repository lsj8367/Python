from django.db import models

# Create your models here.
class Guest(models.Model):
    #myno = models.AutoField(auto_created = True, primary_key = True) # 기본적으로 생성되는 id칼럼 생성안됨
    title = models.CharField(max_length = 50)
    content = models.TextField()
    regdate = models.DateTimeField()
    
    def __str__(self):  # 시스템을 제어하는 명령어 __str__
        return self.title # QuerySet<Guest: 장고>이렇게 보여주게 하는것
    
    # 정렬방법 2:
    class Meta:
        #ordering = ('title',) # title 별 오름차순 정렬 tuple타입이어야 한다. {} set [] list
        #ordering = ('title', 'id') # n차키 부여 가능 우선은 왼쪽부터
        #ordering = ('-title',) # 내림차순 정렬
        ordering = ('-id',)
        