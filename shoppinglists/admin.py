from django.contrib import admin
from .models import Shoppinglist, Item

# Register your models here.
admin.site.register(Shoppinglist)
admin.site.register(Item)