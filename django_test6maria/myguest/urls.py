from django.urls import path
from myguest import views

urlpatterns = [
    path('', views.ListFunc), # 미니방명록 보기 눌렀을때라서 ''로준다
    path('insert/', views.InsertFunc),
    path('insertok/', views.InsertFuncOk),
    
]