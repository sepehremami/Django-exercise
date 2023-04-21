
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView
from django.http import HttpResponse
from .models import User
from questions.models import Questions, Response
from django.db.models import Count
class NewUser(View):
    def get(self, request, *args, **kwargs):
        user = User.objects.all()
        return render(request, 'stackoverflow/sing-in.html')
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        try:
            user = User.objects.create(username=username, password=password, email=email)
        except:
            raise Exception
        return redirect(f'http://127.0.0.1:8000/stackoverflow/profile/{user.pk}')


class ProfileView(DetailView):
    model = User
    template_name='stackoverflow/user_detail.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['questions'] = Questions.objects.filter(author=context['user'])
        return context

        
class UserAskedQuestion(ListView):
    model = User
    context_object_name = 'users'
    template_name = "stackoverflow/useraskedquestion_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] =  Questions.objects.all()
        print(context['questions'].values())
        return context
    
class UserWithMostRsponse(ListView):
    model = User 
    
    template_name = 'stackoverflow/userwithmostresponse_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        response = Response.objects.values('author__username').annotate(count=Count('author')).order_by('-count')
        context['responses'] = response
        print(response.values())
        return context