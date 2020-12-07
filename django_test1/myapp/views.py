from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def indexFunc(request):
    return HttpResponse('인덱스 요청 처리')

def helloFunc(request):
    msg = 'Hello'
    ss = '<html><body>Nice %s</body></html>'%(msg)
    return HttpResponse(ss)

def hello_temp_Func(request): # 요청 받을때 view의 from 값 settings INSTALLED_APPS에 넣어줘라
    msg = '홍길동'
    return render(request, 'show.html', {'name': msg}) # dict type으로 뒤에 가져가면 키 값으로 html에서 받을수있음, 여기서의 키값을 html에서 {{}} 식으로 받아주자

def worldFunc(request):
    return render(request, 'disp.html')