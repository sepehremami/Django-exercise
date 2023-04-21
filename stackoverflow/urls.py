from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.NewUser.as_view(), name='user'),
    path('profile/<pk>', views.ProfileView.as_view(), name='profile'),
    path('users-wq', views.UserAskedQuestion.as_view(), name='users-asked-questions'),
    path('users-most-res', views.UserWithMostRsponse.as_view(), name='users-response-most'),
]