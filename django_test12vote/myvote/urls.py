from django.urls.conf import path
from myvote import views


urlpatterns = [
    path('', views.DispFunc, name = 'disp'), # /gogo/
    
    # int 타입 요청을 받을때 <int:question_id>/ 인데 int: 뒤에 내가 설정할 변수 넣으면 됨
    path('<int:question_id>/', views.DetailFunc, name = 'detail'), # /gogo/1 <== gogo/ 뒤의 숫자 
    path('<int:question_id>/vote/', views.VoteFunc, name = 'vote'), # /gogo/1/vote 여기 name값은 고유해야한다
    path('<int:question_id>/results/', views.ResultFunc, name = 'results'), # /gogo/1/results/ 여기 name값은 고유해야한다
    

]    