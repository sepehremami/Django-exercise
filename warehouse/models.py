from django.db import models


class Warehouse(models.Model):
    code = models.IntegerField(primary_key=True)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)