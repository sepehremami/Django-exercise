from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpRequest
from .models import Questions, Response
from stackoverflow.models import User
from django.views.generic import ListView


def newquestion(request:HttpRequest):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        email = request.POST.get('email')
        user = User.objects.get(email=email)
        if user:
            newquestion = Questions(title=title, description=description, author=user)
            newquestion.save()
    return render(request, 'questions/makequestion.html', {})


def question(request, question_id):
    question = Questions.objects.get(pk = question_id)
    responses = Response.objects.filter(question = question)
    if request.method == 'POST':
        description = request.POST.get('description')
        email = request.POST.get('email')
        user = User.objects.get(email=email)
        if user:
            response = Response(description = description, author = user, question = question)
            response.save()
    return render(request, 'questions/show_question.html', {"question": question, "responses": responses})


class QuestionListView(ListView):
    model = Questions
    template_name= 'questions/questions_list.html'
    context_object_name = 'questions'
    paginate_by = 3

    

