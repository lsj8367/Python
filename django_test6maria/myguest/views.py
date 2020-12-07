from django.shortcuts import render
from myguest.models import Guest
from django.http.response import HttpResponseRedirect
from datetime import datetime

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def ListFunc(request):
    #gdata = Guest.objects.all()
    #print(gdata) # <QuerySet [<Guest: 차가워진 날씨>, <Guest: 방문>, <Guest: 장고>]>
    #print(Guest.objects.get(id=1)) # 차가워진 날씨 unique 한 값
    #print(Guest.objects.filter(id=1)) # <QuerySet [<Guest: 차가워진 날씨>]>
    #print(Guest.objects.filter(title__contains ='장고')) # 제목에 장고가 들어간 오브젝트 출력 <QuerySet [<Guest: 장고>]>
    
    # 정렬 방법 1:
    #gdata = Guest.objects.all().order_by('title') # title별 ascending sort 오름차순
    #gdata = Guest.objects.all().order_by('-title') # orderby에 -값을 주면 descending sort
    #gdata = Guest.objects.all().order_by('-id') # id별 내림차순 정렬
    #gdata = Guest.objects.all().order_by('-id')[0:3] # 상위 3개만 보여줌 슬라이싱 slicing 처리
    
    gdata = Guest.objects.all()
    context = {'gdatas' : gdata}
    return render(request, 'list.html', context)

def InsertFunc(request):
    return render(request, 'insert.html')

def InsertFuncOk(request):
    if request.method == 'POST':
        #print(request.POST.get('title'))
        #print(request.POST['title']) # 위의 결과와 값은 동일
        Guest(
            title = request.POST.get('title'),
            content = request.POST['content'],
            regdate = datetime.now()
            ).save() # 경우에따라 등록, 수정이 된다. update, insert into myguest_guest values(... 와 같음
        
        '''
        # 수정
        g = Guest.objects.get(id = 1) # id값이 1번인애 값 다가져옴
        g.title = request.POST.get('title')
        g.save() # update myguest_guest set title=... 
        
        # 삭제
        g = Guest.objects.get(id = 1)
        g.delete() # 삭제함수 delete from myguest_guest where id = 1
        
        
        '''
        
    return HttpResponseRedirect('/guest') # 추가 후 목록보기













