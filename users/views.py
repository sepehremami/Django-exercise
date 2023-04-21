from django.shortcuts import render
from .models import Customer, Athur
from library.models import Book
from basket.models import Basket
from django.http import HttpResponse


def get_customer_list(request):
    customer = Customer.objects.all()
    return render(request, "customer.html", {"customers": customer})


def get_author_book(request, slug):
    print(slug)
    author = Athur.objects.get(slug=slug)
    print(author)
    book_list = Book.objects.filter(author_id = author.name)
    return HttpResponse(book_list)

def get_customer_book_list(request, slug):
    customer = Customer.objects.get(slug=slug)
    # basket = Basket.objects.get(customer=customer)
    book = Book.objects.filter(basket__customer_id=customer.email)
    return HttpResponse(book)

from django.views import generic

class AuthorListView(generic.ListView):
    model = Athur
    template_name = 'customer.html'