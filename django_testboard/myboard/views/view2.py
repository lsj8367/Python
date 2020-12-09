from django.shortcuts import render, redirect
from myboard.models import BoardTab
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http.response import HttpResponseRedirect
from datetime import datetime

def ListFunc(request): # 목록보기
    #datas = BoardTab.objects.all().order_by('-id')
    datas = BoardTab.objects.all().order_by('-gnum', 'onum') # 댓글이 달린 경우
    paginator = Paginator(datas, 5)
    page = request.GET.get('page')
    
    try: # 페이징 처리
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages())
    
    return render(request, 'board.html', {'data' : data})

def Get_ip_address(request): # client의 ip 얻기용
    x_forwarded = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded:
        ip = x_forwarded.split(',')[0]
    else:
        #ip = request.META.get('REMOTE_ADDR')
        ip = request.META['REMOTE_ADDR']
    return ip

def InsertFunc(request): # 글쓰기
    return render(request, 'insert.html')

def InsertokFunc(request): #글 쓰기 저장완료
    if request.method == "POST":
        try:
            gbun = 1
            datas = BoardTab.objects.all() # group 번호 구하기
            if datas.count() != 0:
                gbun = BoardTab.objects.latest('id').id + 1 # 가장 마지막 id 번호 + 1
                
            BoardTab(
                name = request.POST['name'],
                passwd = request.POST.get('passwd'),
                mail = request.POST['email'],
                title = request.POST['title'],
                cont = request.POST['cont'],
                bip = Get_ip_address(request),
                bdate = datetime.now(),
                readcnt = 0,
                gnum = gbun,
                onum = 0,
                nested = 0,
            ).save()
            
        except Exception as e:
            print('추가 오류 : '+ str(e))
    
        #return HttpResponseRedirect('/board/list/') # 추가 후 목록 보기
        return redirect('/board/list/') # 위와 같은의미 
    
def ContentFunc(request): # 글내용 상세보기
    data = BoardTab.objects.get(id = request.GET['id'])
    data.readcnt = data.readcnt + 1
    data.save() # 조회수 저장
    page = request.GET.get('page')
    return render(request, 'content.html', {'data_one' : data, 'page' : page})
    
def UpdateFunc(request): # 글 수정하기
    try:
        data = BoardTab.objects.get(id = request.GET['id'])
        # page도 달고다녀야한다.
        return render(request, 'update.html', {'data_one' : data})
    
    except Exception as e:
        print('UpdateFunc err : ' + str(e))

def UpdateokFunc(request): # 수정확인
    if request.method == "POST":
        upRec = BoardTab.objects.get(id=request.POST.get('id'))
        # 비밀번호 비교
        if upRec.passwd == request.POST['up_passwd']: # 기존 비밀번호와 받은 비밀번호 같을때
            upRec.name = request.POST['name']
            upRec.mail = request.POST['mail']
            upRec.title = request.POST['title']
            upRec.cont = request.POST['cont']
            upRec.save()
            
        else:  #원래 비밀번호와 받은 비밀번호가 다르면
            return render(request, 'error.html')
            
        return HttpResponseRedirect('/board/list/') # 수정 후 목록보기

def DeleteFunc(request): # 삭제하기
    try:
        data = BoardTab.objects.get(id = request.GET['id'])
        # page도 달고다녀야한다.
        return render(request, 'delete.html', {'data_one' : data})
    
    except Exception as e:
        print('DeleteFunc err : ' + str(e))

def DeleteokFunc(request):
    if request.method == "POST":
        delRec = BoardTab.objects.get(id=request.POST.get('id'))
        # 비밀번호 비교
        if delRec.passwd == request.POST['del_passwd']: # 기존 비밀번호와 받은 비밀번호 같을때
            delRec.delete() # delete from BoardTab where id = 받은 id

        else:  #원래 비밀번호와 받은 비밀번호가 다르면
            return render(request, 'error.html')
            
        return HttpResponseRedirect('/board/list/') # 삭제 후 목록보기

def SearchFunc(request): # 검색 : 작성자별 또는 제목별 검색
    if request.method == 'POST':
        s_type = request.POST['s_type']   # 분류
        s_value = request.POST['s_value'] # 검색단어
        #print('s_type :', s_type , ', s_value : ', s_value)

        if s_type == 'title':
            datas = BoardTab.objects.filter(title__contains = s_value).order_by('-id') # __contains 특정 단어 포함
        elif s_type == 'name':
            datas = BoardTab.objects.filter(name__contains = s_value).order_by('-id')

        paginator = Paginator(datas, 5)
        page = request.GET.get('page')

        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages())

        return render(request, 'board.html', {'data' : data})
    
def ReplyFunc(request): # 댓글달기
    try:
        data = BoardTab.objects.get(id = request.GET['id']) # 댓글 대상자료 읽기

    except Exception as e:
        print("ReplyFunc err : ", str(e))

    return render(request, 'reply.html', {'data_one' : data})

def ReplyokFunc(request):
    if request.method == "POST":
        try:
            regnum = int(request.POST.get('gnum')) # 계산해야해서 int casting
            reonum = int(request.POST.get('onum'))
            temRec = BoardTab.objects.get(id = request.POST.get('id'))
            
            old_gnum = temRec.gnum
            old_onum = temRec.onum
            
            if old_onum >= reonum and old_onum == regnum:
                old_onum = old_onum + 1     # onum 갱신
            
            # 댓글 저장
            BoardTab(
                name = request.POST['name'],
                passwd = request.POST.get('passwd'),
                mail = request.POST['mail'],
                title = request.POST['title'],
                cont = request.POST['cont'],
                bip = request.META['REMOTE_ADDR'],
                bdate = datetime.now(),
                readcnt = 0,
                gnum = regnum,
                onum = old_onum,
                nested = int(request.POST.get('nested')) + 1,
            ).save()
            
            
        except Exception as e:
            print("ReplyokFunc err : ", str(e))
        
    return redirect('/board/list/') # 댓글 입력 후 목록 보기