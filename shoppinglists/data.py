from .models import Shoppinglist, Item
# import django
# django.setup()

def initialize():
    shoppinglist = Shoppinglist(
        name='Trip to London',
        description='vacation of this year'
    )
    shoppinglist.save()


     