from django.db import models

# Create your models here.
# from django.db import models

class Shoppinglist(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, default="desc")
    
    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    shoppinglist = models.ForeignKey(
        Shoppinglist, on_delete=models.CASCADE)

    def __str__(self):
        return self.name