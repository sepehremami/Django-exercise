from django.db import models
from django.utils.text import slugify


class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs)-> None:
        self.slug = slugify(self.username)
        return super().save(*args, **kwargs)\
        
    def __str__(self) -> str:
        return f'{self.slug}: {self.email}'