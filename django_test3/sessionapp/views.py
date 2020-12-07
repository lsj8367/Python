from django.shortcuts import render
from django.http.response import HttpResponseRedirect

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')

def setosFunc(request):
    if 'favorite_os' in request.GET:
        #print(request.GET['favorite_os'])
        request.session['f_os'] = request.GET['favorite_os'] # request.session['key'] = value 세션읽기/쓰기
        # kbs = request.session['f_os'] = request.GET['favorite_os']
        return HttpResponseRedirect('/showos') # redirect 방식 showos요청 발생
    else:
        return render(request, 'setos.html') # forward 방식

def showosFunc(request):
    context = {} # dict type
    
    if 'f_os' in request.session: # 세션 키값중 f_os가 있다면~
        context['dict_f_os'] = request.session['f_os'] # 세션값 읽기
        context['message'] = '당신이 선택한 운영체제는 %s'%request.session['f_os']
    else:
        context['dict_f_os'] = None
        context['message'] = '운영체제를 선택하지 못했네요'
        
    request.session.set_expiry(5) # 5초동안 클라이언트의 활동이 없으면 세션 삭제
    return render(request, 'show.html', context)
        
        