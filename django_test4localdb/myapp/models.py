from django.db import models

# Create your models here.
# ORM 기법을 사용 : SQL문 직접 기술 X

class Article(models.Model): # 테이블을 클래스로 정의
    code = models.CharField(max_length = 10) # 칼럼은 속성(멤버변수)으로 부여
    name = models.CharField(max_length = 20) # 문자형
    price = models.IntegerField() # 정수형
    pub_date = models.DateTimeField() # 날짜
    # 칼럼을 변경하거나 생성할때 Make Migrations 눌러서 application 선택후 생성 해준다

