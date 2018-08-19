from django.test import TestCase
from ..fixtures.user.create_user import query_create_user, create_user_response,query_login,login_reponse, query_login_invalid
from .data import BaseTest

from shoppinglistapi.schema import schema
import json
from django.test import Client



class AuthTestCase(BaseTest):

    def test_create_user(self):
        query = self.test_client.execute(query_create_user)
        self.assertEquals(query,create_user_response)
    def test_login_user(self):
        query = self.test_client.execute(self.login_query)
        assert "data" in query
        assert "loginUser" in query["data"]
        assert "token" in query["data"]["loginUser"]
    def test_login_user_with_invalid_credentials(self):
        query = self.test_client.execute(self.invalid_credentials_query)
        print(query)
        self.assertEquals(query['errors'][0]['message'],"Please, enter valid credentials")
        
    