from django.shortcuts import render
from django.views.generic.edit import CreateView

from geeksforgeeks.models import GeeksModel

class GeeksCreateView(CreateView):
    model = GeeksModel

    fields = ['title', 'description']
   