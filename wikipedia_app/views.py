from django.http import HttpResponse
from django.shortcuts import render
import wikipedia

def home(request):
    if request.method =="POST":
        search = request.POST['search']
        print(search)
        try:
            result = wikipedia.summary(search, sentences=3)

        except:
            return HttpResponse('wrong input!')
        return render(request, 'wikipedia/index.html', {"result":result})
    return render(request, 'wikipedia/index.html')