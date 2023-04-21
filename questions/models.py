from django.db import models
from stackoverflow.models import User
# Create your models here.

class Questions(models.Model):
    title = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    date = models.DateField(auto_now=True)
    picture = models.ImageField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)