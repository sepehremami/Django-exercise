from django.urls import path, include
from . import views


url_patterns = [
    path('customer/', views.get_user_list)
]