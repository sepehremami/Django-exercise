from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)

    class Meta:
        abstract = True

class Customer(Person):
    phone = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, primary_key=True)

class Athur(Person):
    name = models.CharField(max_length=255, primary_key=True)
    address = models.CharField(max_length=255)
    url = models.CharField(max_length=255, null=True)

class Publisher(Person):
    name = models.CharField(max_length=255, primary_key=True)
    phone = models.CharField(max_length=255, null=True)
    url = models.CharField(max_length=255, null=True)