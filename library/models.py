from django.db import models
from django.core.validators import  MinValueValidator
from users.models import Publisher, Athur
from warehouse.models import Warehouse
# Create your models here.


class Book(models.Model):
    isbn = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    author = models.ForeignKey(Athur, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    warehouse = models.ManyToManyField(Warehouse, through='Warehousebook')


class Warehousebook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    count = models.IntegerField()


