from django.shortcuts import render ,get_object_or_404, redirect
from django.http import HttpResponse
from.models import Question, Answer
from django.utils import timezone
# Create your views here.

def index(request):
    question_list = Question.objects.order_by('-create_date') # 최신순 정렬하기 위해 내림차순 - 붙임
    context = {"question_list":question_list}
    return render(request, 'pybo/question_list.html',context)
    # Templates 경로는 c:\chang_git\mysite\templates이다.
    # 위에서 렌더링은 'pybo\question_list.html'로 지정했다 -> 'pybo/' 경로를 직접 생성하는 과정이 필요하다.
    # 그러면 'pybo/question_list.html'이 아니라 'question_list.html이 렌더링 경로로 설정되면 되는거 아니냐? 싶지만
    # 브라우저에서 접속시에 www.naver.com/blog 처럼 나오게 하기 위해서 위처럼 파일경로를 생성하여 만든다.

    # 해당 문자열을 Http방식으로 반환해주는 메소드
    #return HttpResponse("<h1>안녕하세요. Pybo 메인 페이지 입니다.</h1>")

def detail(request, question_id):
    #question = Question.objects.get(id=question_id) # 그냥 받을 때

    question = get_object_or_404(Question, pk = question_id)#에러 처리 할때
    context = {'question' : question}
    return render(request,'pybo/question_detail.html',context)

def answer_create(request, question_id):
    question = get_object_or_404(Question,pk = question_id)
    request.POST.get("content")
    # save() 랑 동일한 기능이고 create안에 들어가는 값이 만들어지는 값임
    question.answer_set.create(content = request.POST.get("content") , create_date= timezone.now())
    return redirect("pybo:detail", question_id = question_id)