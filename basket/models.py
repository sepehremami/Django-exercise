from django.db import models
from users.models import Customer
from library.models import Book


class Basket(models.Model):
    customer = models.ForeignKey(Customer, to_field='email', on_delete=models.CASCADE)
    book = models.ManyToManyField(Book, related_name="book")

