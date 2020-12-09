from django.shortcuts import render
def Main(request):
    ss = "<div><b style='text-size: 24pt'>메인화면</b></div>"
    # <script>alert('hi');</script> 스크립트도 사용가능!!!
    return render(request, 'main.html', {'head' : ss})