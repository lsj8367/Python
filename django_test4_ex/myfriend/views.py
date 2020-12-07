from django.shortcuts import render
from myfriend.models import Friend

# Create your views here.
def MainFunc(request):
    if request.method == 'GET':
        return render(request, 'main.html')
    elif request.method == 'POST':
        friend_list = Friend.objects.all()
        return render(request, 'main.html', {'friend': friend_list})
    
    
