from django.shortcuts import render
from myapp.models import Article

# Create your views here.
def Main(request):
    return render(request, 'main.html')

def DbShow(request):
    # ORM을 통한 QuerySet 얻기
    datas = Article.objects.all() # 내부적으로 select문이 수행됨
    #print(datas)  # <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
    #print(datas[0].name) # 마우스
    
    #return render(request, 'articlelist.html')
    return render(request, 'articlelist.html', {'articles': datas}) #QuerySet 전달
