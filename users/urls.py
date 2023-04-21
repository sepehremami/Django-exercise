from django.urls import path, include
from . import views


urlpatterns = [
    path("customers/", views.get_customer_list),
    path("author/<slug:slug>/", views.get_author_book),
    path("customer/<slug:slug>/", view=views.get_customer_book_list),]

