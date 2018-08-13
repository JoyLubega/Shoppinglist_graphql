from shoppinglistapi.schema import schema
import json
from django.test import TestCase
from django.test import Client
from .data import Base
from ..fixtures.query_shoppinglists import create_shoppinglist_mutation,create_shoppinglist_response
from ..fixtures.user.create_user import query_create_user,query_login




class ShoppinglistsTestCase(TestCase):
    def setUp(self):
        self._client = Client()

    def test_create_shoppinglists(self):
        '''
        Test for creating a shoppinglist with all attributes
        '''
        Base.query_auth(self,query=query_create_user) # Register a user
        Base.query_auth(self,query=query_login)
        resp=Base.query_other(self, query=create_shoppinglist_mutation)
        print(resp)
        self.assertEquals(resp, create_shoppinglist_response)
        
        
