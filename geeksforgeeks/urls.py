from django.urls import path
from .views import GeeksCreateView

urlpatterns = [
    path('geeks/', GeeksCreateView.as_view()),
]