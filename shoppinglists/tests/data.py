import json
from django.test import TestCase
from graphene.test import Client
from ..fixtures.user.create_user import query_login, query_create_user, query_login_invalid
from django.contrib.auth import get_user_model
from shoppinglistapi.schema import schema
from django.test import Client as DjangoTestClient
from shoppinglists.models import Shoppinglist, Item

# Inherit from this in your test cases
User = get_user_model()

class BaseTest(TestCase):
    

    def setUp(self):
        self.test_client = Client(schema)
        self.client = DjangoTestClient()
        self.maxDiff = None

        test_user = User(
            username="Jackson",
            email="jacks@gmail.com"
        )
        test_user.set_password(123)
        test_user.save()

        test_shoppinglist = Shoppinglist(
            name="Breakfast",
            description="First meal of the day"
        )
        test_shoppinglist.save()

        test_item = Item(
            shoppinglist_id=test_shoppinglist.id,
        name="Rolex"
        
        )
        test_item.save()

        

        self.login_query = query_login
        self.invalid_credentials_query= query_login_invalid
        test_login =  self.test_client.execute(self.login_query)
        self.test_token = ("JWT {}".format(test_login["data"]["loginUser"]["token"]))