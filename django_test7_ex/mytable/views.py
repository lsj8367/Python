from django.shortcuts import render
from mytable.models import Gogek, Jikwon, Buser
from django.db.models.aggregates import Count

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def BuserFunc(request):
    busers = Buser.objects.all()
    return render(request, 'buser.html', {'busers' : busers})

def JikwonFunc(request):
    b_no = request.GET.get('buser_no')
    #print(b_no)
    jikwons = Jikwon.objects.filter(buser_num = b_no)
    
    for j in jikwons:
        #j.jikwon_no
        gogeks = Gogek.objects.filter(gogek_damsano = j.jikwon_no)
        j.count = len(gogeks)
        #print(j.jikwon_no)
    #print(j_no)
    return render(request, 'jikwon.html', {'jikwons' : jikwons})

def GogekFunc(request):   
    j_no = request.GET.get('jikwon_no')
    gogeks = Gogek.objects.filter(gogek_damsano = j_no).order_by('gogek_name')
    for list in gogeks:
        if int(list.gogek_jumin[7]) == 1 or int(list.gogek_jumin[7]) == 3:
            list.gogek_gen = '남'
        else:
            list.gogek_gen = '여'
    gogeks.order_by('gogek_name')
    
    return render(request, 'gogek.html', {'glist' : gogeks})
