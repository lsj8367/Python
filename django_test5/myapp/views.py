from django.shortcuts import render
from myapp.models import Profile
from django.db.models.aggregates import Avg, Count, Max, Min, Sum
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

# Create your views here.
def IndexFunc(request):
    return render(request, 'index.html')

def CalldictFunc(request):
    profile_list = Profile.objects.all()
    #print(profile_list) #<QuerySet [<Profile: Profile object (1)>...
    
    for row in profile_list.values_list():
        print(row) # tuple type (1, '홍길동', 22)
    
    print("***" * 20)
        
    print(Profile.objects.aggregate(Avg('age'))) # 소계구하는 함수 => aggregate avg(칼럼) {'age__avg': 30.333333333333332}
    print(Profile.objects.aggregate(Max('age'))) # {'age__max': 42}
    print(Profile.objects.aggregate(Sum('age'))) # {'age__sum': 182}
    print(Profile.objects.aggregate(Count('age'))) # {'age__count': 6}\
    print(Profile.objects.aggregate(Min('age'))) # {'age__count': 6}\
    print(len(profile_list))
    
    print(Profile.objects.filter(name='홍길동').aggregate(Avg('age'))) # where 조건 filter
    
    print("***" * 20)
    # values() + annotate()    그룹별 평균 나이는????
    qs = Profile.objects.values('name').annotate(Avg('age'))
    for r in qs:
        print(r)
#         {'name': '신기해', 'age__avg': 33.0}
#         {'name': '한가해', 'age__avg': 33.0}
#         {'name': '홍길동', 'age__avg': 27.666666666666668}
    
    # 결과를 list로 감싸 dict type으로 클라이언트에게 출력하기
    print("***" * 20)
    pro_list = []
    for pro in profile_list:
        pro_dict = {} # 밖에있으면 계속 덮어쓰기때문에 한가지가 길이 늘어나는만큼 덮어씀.
        pro_dict['name'] = pro.name
        pro_dict['age'] = pro.age
        pro_list.append(pro_dict)
        print(pro_list)
        
    context = {'pro_dict':pro_list}   
    
    return render(request , 'abc.html', context)

# GenericView
class MyClass1(TemplateView):
    template_name = 'disp1.html'
    def get(self, request):
        return render(request, self.template_name)

class MyClass2(TemplateView):
    def get(self, request):
        return render(request, 'hi.html')
    
    def post(self, request):
        msg = request.POST.get('msg')
        return render(request, 'hi2.html', {'msg' : msg + '만세'})
    
        

class MyClass3(ListView):
    # 해당 테이블의 자료를 읽어 object_list 키에 담은 후 '현재 App이름 / profile_list.html 파일을 호출
    model = Profile













