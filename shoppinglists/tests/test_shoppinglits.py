from shoppinglistapi.schema import schema
import json
from django.test import TestCase
from django.test import Client
from .data import GraphQLTestCase
from ..tests.test_auth import AuthTestCase
from ..fixtures.query_shoppinglists import create_shoppinglist_mutation,create_shoppinglist_response
from ..fixtures.user.create_user import query_create_user,query_login




class ShoppinglistsTestCase(TestCase):
    def setUp(self):
        self._client = Client()

    def test_create_shoppinlists(self):
        '''
        Test for creating a shoppinglist with all attributes
        '''
        GraphQLTestCase.query_auth(self,query=query_create_user) # Register a user
        GraphQLTestCase.query_auth(self,query=query_login)
        resp=GraphQLTestCase.query_auth(self, query=create_shoppinglist_mutation)
        self.assertEquals(resp, create_shoppinglist_response)

        
