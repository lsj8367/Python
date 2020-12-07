from django.shortcuts import render, get_object_or_404
from myvote.models import Question, Choice
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.urls.base import reverse # url 패턴으로부터 url 스트링 얻기

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def DispFunc(request):
    q_list = Question.objects.all().order_by("pub_date", 'id')  # 1차키 2차키 순으로 정렬
    context = {'q_list' : q_list}
    return render(request, 'display.html', context)

def DetailFunc(request, question_id):
    # question_id 는 <int : 에서 받아온값
    #return HttpResponse("question_id %s"%question_id) # 결과 : question_id 1 또는 2
    """
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404("Question Does Not Exist")
    """
    question = get_object_or_404(Question, pk = question_id) # 위 주석과 같은 의미
    
    #print(question.question_text) # 좋아하는 운동경기는?
    #print(question) # 좋아하는 운동경기는? 둘다 같은값 출력
    #print(question.pub_date) # 2020-11-06 05:54:39+00:00
    
    return render(request, "detail.html", {'question' : question})

def VoteFunc(request, question_id):
    #return HttpResponse("voting on question_id %s"%question_id)
    
    question = get_object_or_404(Question, pk = question_id)
    try:
        sel_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {'question': question, 'error_msg' : '1개의 항목을 반드시 선택하세요'}) 

    #제대로 값이 들어간다면 누적을 시켜줘야함
    sel_choice.votes += 1 # 선택된 항목에 득표 1씩 누적시킴
    sel_choice.save() # Choice 테이블의 votes 수정 완료
    print(reverse('results', args = (question_id,)))  # results값에 url을  튜플타입으로 값을줌    축구를 선택한 경우 /gogo/1/results/
    return HttpResponseRedirect(reverse('results', args = (question_id,))) # /gogo/1/results/값으로 넘어감

def ResultFunc(request, question_id):
    print("result of question_id %s"%question_id)
    
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'result.html', {'question' : question })





