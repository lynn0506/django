from django.shortcuts import render 
from django.conf import settings
from django.shortcuts import redirect
from mainPage.models import Question
# .models는 mainPage.models와 같다

def index(request):
    return render(request, 'mainPage/index.html')

def question(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        return render(request, 'mainPage/QApage.html', {'questions': questions})
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Question.objects.create(title=title, content=content)
        return redirect('/main/question')

def show_question(request, id):
    question = Question.objects.get(id = id)
    return render(request, 'mainPage/QAshow.html', {'question': question})

def new_question(request):
    return render(request, 'mainPage/newQA.html')