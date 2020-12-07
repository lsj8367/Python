'''
메인 urls에 의해 위임된 각 application의 urls 중 하나
여기서는 gpapp/ 이 다음에 들어간느 페이지

'''
from django.urls import path
from gpapp import views

urlpatterns = [
    path('insert/', views.InsertFunc, name = 'InsertFunc'), # Function views //gpapp/insert
    
]
