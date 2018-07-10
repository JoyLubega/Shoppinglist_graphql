from django.db import models

# Create your models here.
from django.db import models


class Shoppinglist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Items(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    shoppinglist = models.ForeignKey(
        Shoppinglist, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.name