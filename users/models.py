from django.db import models
from django.utils.text import slugify


class Person(models.Model):
    name = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    slug = models.SlugField(null=True, blank=True,editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        abstract = True

class Customer(Person):
    phone = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.name

class Athur(Person):
    name = models.CharField(max_length=255, primary_key=True)
    address = models.CharField(max_length=255)
    url = models.CharField(max_length=255, null=True)

class Publisher(Person):
    name = models.CharField(max_length=255, primary_key=True)
    phone = models.CharField(max_length=255, null=True)
    url = models.CharField(max_length=255, null=True)
