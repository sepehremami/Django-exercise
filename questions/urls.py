from django.urls import path
from . import views
urlpatterns = [
    path('newquestion/', views.newquestion)
]