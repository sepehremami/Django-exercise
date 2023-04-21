from django.db import models
from stackoverflow.models import User
# Create your models here.

class Questions(models.Model):
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    date = models.DateField(auto_now=True)
    picture = models.ImageField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Response(models.Model):
    description = models.TextField()
    date = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)