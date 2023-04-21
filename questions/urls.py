from django.urls import path
from . import views
urlpatterns = [
    path('newquestion/', views.newquestion),
    path('question/<int:question_id>', views.question),
    path('questions/', views.QuestionListView.as_view()),

]