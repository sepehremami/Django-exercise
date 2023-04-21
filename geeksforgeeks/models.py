from django.db import models

class GeeksModel(models.Model):
    title = models.CharField(max_length=200)    
    description=  models.TextField()

    def __str__(self) -> str:
        return self.title 
    
    