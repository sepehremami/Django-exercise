from django.shortcuts import render
from users.models import Customer
from .models import Basket
from library.models import Book
from django.http import HttpResponse

def get_user_basket(request, slug):
    customr = Customer.objects.get(slug = slug)
    basket = Basket.objects.get(customr_id = customr.email)
    book_list = Book.objects.filter(isbn = basket.book_id)
    return HttpResponse(book_list)

