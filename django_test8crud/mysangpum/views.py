from django.shortcuts import render
from mysangpum.models import Sangdata
import MySQLdb
from django.http.response import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

conn = MySQLdb.connect(**config)
# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def ListFunc(request): # 목록보기
    #SQL문 직접 사용
    '''
    sql = 'select * from sangdata'
    cursor = conn.cursor()
    cursor.execute(sql)
    datas = cursor.fetchall()
    #print(type(datas))      # <class 'tuple'>
    '''
    # django의 ORM 지원 함수 이용
    """ 페이징 처리 없는 경우
    datas = Sangdata.objects.all()
    #print(type(datas2))     # <class 'django.db.models.query.QuerySet'>
    return render(request, 'list.html', {'sangpums' : datas})
    """
    
    
    datas = Sangdata.objects.all().order_by('-code') # descending sort
    paginator = Paginator(datas, 5) # 한 페이지당 3행씩 출력해줌
    try:
        page = request.GET.get('page')
    except:
        page = 1
    
    try:
        data = paginator.page(page)
        
    except PageNotAnInteger: # 페이지가 정수가 아닌경우
        data = paginator.page(1)
        
    except EmptyPage: # page가 없는 경우 (받아지지 않는 경우)
        data = paginator.page(paginator.num_pages())
    
    # 개별페이지 표시용
    allpage = range(paginator.num_pages + 1) # 전체페이지수 + 1
    
    
    return render(request, 'list2.html', {'sangpums' : data, 'allpage' : allpage}) 
    

def InsertFunc(request): # 추가하기
    return render(request, 'insert.html')

def InsertOkFunc(request):
    if request.method == 'POST':
        # 잘 넘어왔는지 확인이 필요하다 !!!
        #print(request.POST.get('code'))
        #print(request.POST['su'])        
        # insert into sangdata values() 가능
        # return 으로  a = sangdata().save() 도 가능
        
        # 신상 코드 번호 검증 작업 필요함!!
        #Sangdata.objects.filter(code = 14).exists()
        if Sangdata.objects.filter(code = request.POST.get('code')).exists(): # 존재한다면
            return render(request, 'insert.html', {"msg" : "이미있는 번호!!!"}) # 중복메세지
            
        else:
            Sangdata(
                code = request.POST.get('code'),
                sang = request.POST.get('sang'),
                su = request.POST.get('su'),
                dan = request.POST.get('dan'),
                ).save()
            return HttpResponseRedirect('/sangpum/list') # 추가 후 상품보기
        
def UpdateFunc(request): # 수정하기
    data = Sangdata.objects.get(code = request.GET['code'])
    return render(request, 'update.html', {'sang_one' : data })
    

def UpdateOkFunc(request):
    if request.method == 'POST':
        # update sangdata set ... SQL문 사용도 가능
        updateRec = Sangdata.objects.get(code = request.POST.get('code'))
        updateRec.sang = request.POST.get('sang')
        updateRec.su = request.POST.get('su')
        updateRec.dan = request.POST.get('dan')
        updateRec.save()
        
        return HttpResponseRedirect('/sangpum/list')  # 수정완료후 상품보기


def DeleteFunc(request): # 삭제하기
    delRec = Sangdata.objects.get(code = request.GET.get('code'))
    delRec.delete()
    return HttpResponseRedirect('/sangpum/list') # 삭제 후 상품보기






