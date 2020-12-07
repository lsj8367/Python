from django.db.models.query_utils import Q
from django.shortcuts import render
from exapp.models import Gogek, Jikwon, Buser
import datetime
from django.contrib import messages

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def JikwonFunc(request):
    damsano = 0
    name = request.POST['gogek_name']
    tel = request.POST['gogek_tel']
    num = 0
    if Gogek.objects.filter(Q(gogek_name = name) & Q(gogek_tel = tel)).exists():
        gogeks = Gogek.objects.filter(Q(gogek_name = name) & Q(gogek_tel = tel))
        #print(gogeks.gogek_damsano_id)
        for g in gogeks:
            #print(g.gogek_damsano_id)
            damsano = g.gogek_damsano_id
        #print(damsano)
            
        jikwons = Jikwon.objects.filter(jikwon_no = damsano)
        for j in jikwons:
            num = j.buser_num
            if j.jikwon_rating == 'a':
                j.jikwon_rating = '최우수'
            elif j.jikwon_rating == 'b':
                j.jikwon_rating = '우수'
            elif j.jikwon_rating == 'c':
                j.jikwon_rating = '일반'
            
            now = datetime.datetime.now()
            nowDate = now.strftime('%Y')
        #print(nowDate)
        #print(str(j.jikwon_ibsail)[0:4])
            j.jikwon_ibsail = str(int(nowDate) - int(str(j.jikwon_ibsail)[0:4]))
        #print(j.jikwon_ibsail)
        busers = Buser.objects.get(buser_no = num)
        return render(request, 'jikwon.html', {'jikwons' : jikwons, 'busers' : busers})
              
    else:
        #print("번호가 맞지않음")
        messages.add_message(request, messages.INFO, '고객정보가 일치하지 않음!')    
        return render(request, 'jikwon.html')
