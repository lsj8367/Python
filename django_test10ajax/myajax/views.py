from django.shortcuts import render
import json
from django.http.response import HttpResponse
#dict data
lan = {
    'id' : 111,
    'name' : '파이썬',
    'history' : [
        {'date' : '2010-7-20', 'exam' : 'basic'},
        {'date' : '2010-10-20', 'exam' : 'django'},
    ]
}
# Create your views here.
def indexFunc(request):
    #print(type(lan)) # <class 'dict'>
    # json Encoding : dict, list, tuple 등 => str(문자열)로 변환하는 작업
    #jsonString = json.dumps(lan) # dump로 json을 str로 변환함
    
    #print(jsonString) # {"id": 111, "name": "\ud30c\uc774\uc36c", "history": [{"date": "2010-7-20", "exam": "basic"}, {"date": "2010-10-20", "exam": "django"}]}
    #print(type(jsonString)) # <class 'str'>
    
    # 들여쓰기가 있는 형태로 변환
    #jsonString = json.dumps(lan, indent = 4) # 들여쓰기 indent 메모리를 많이 잡아먹음
    #print(jsonString)
    
    #print("*****" * 20)
    
    # json Decoding : str(문자열 반드시 key : value 형태여야함) => dict, tuple, list등의 형태로 변환하는것.
    #dictData = json.loads(jsonString)
    
    #print(dictData)
    #print(type(dictData))
    #print(dictData['name']) # 파이썬의 dict class 관련 명령어를 사용할 수 있다.
#     for h in dictData['history']:
#         print(h['date'], h['exam'])

    return render(request, 'abc.html')

def Func1(request):
    msg = request.GET['msg']
    #print(msg)
    msg = msg + ' 아작스'
    context = {'key' : msg}
    return HttpResponse(json.dumps(context), content_type = "application/json") # json형식을 넘기고있음.
    
def Func2(request):
    datas = [
        {'irum' : '홍길동', 'nai' : 22},
        {'irum' : '고길동', 'nai' : 32},
        {'irum' : '신길동', 'nai' : 27}
    ]
    return HttpResponse(json.dumps(datas), content_type = "application/json") # json형식을 넘기고있음. datatype: 의 값

