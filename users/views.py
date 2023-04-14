from django.shortcuts import render
from .models import Customer, Athur
from library.models import Book
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


    