from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpRequest
from .models import Questions
from stackoverflow.models import User
# Create your views here.


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
    

