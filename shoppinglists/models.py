from django.db import models
from datetime import datetime
from django.conf import settings

# Create your models here.
# from django.db import models

class Shoppinglist(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, default="desc")
    date_created = models.DateTimeField(
        default=datetime.now, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    shoppinglist = models.ForeignKey(
        Shoppinglist, on_delete=models.CASCADE)
    date_created = models.DateTimeField(
        default=datetime.now, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name