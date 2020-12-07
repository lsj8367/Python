from django.shortcuts import render
from exajax.models import Jikwon, Buser
from django.http.response import HttpResponse
import json
# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def ListFunc(request):
    return render(request, 'list.html')

def SearchFunc(request):
    jikwon = Jikwon.objects.filter(jikwon_jik = request.GET['jikwon_jik'])
    
    datas = []
    for j in jikwon:
        #print(j.jikwon_no)
        buser = Buser.objects.get(buser_no = j.buser_num)
        #print(buser.buser_name)
        dic = {'jikwon_no' : j.jikwon_no, 'jikwon_name' : j.jikwon_name, 'buser_name' : buser.buser_name}
        datas.append(dic)
    #print(datas)
    return HttpResponse(json.dumps(datas), content_type = "application/json")