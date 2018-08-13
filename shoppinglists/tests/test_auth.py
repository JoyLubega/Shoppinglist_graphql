from django.test import TestCase
from ..fixtures.user.create_user import query_create_user, create_user_response,query_login,login_reponse
from .data import Base

from shoppinglistapi.schema import schema
import json
from django.test import Client


# import pytest
# # Create your tests here.

# pytestmark = pytest.mark.django_db


class AuthTestCase(TestCase):
    def setUp(self):
        self._client = Client()

    def test_create_user_mutation(self):
        '''
        Test for creating a user with all attributes
        '''
        q= Base.query_auth(self,query=query_create_user)
        self.assertEquals(q, create_user_response)
    
    def test_login_user_mutation(self):
        '''
        Test for login a user with all attributes
        '''
        Base.query_auth(self,query=query_create_user) # Register a user
        q= Base.query_auth(self,query=query_login) # Login
        self.assertIn("token", q['data']['loginUser'].keys())
        
    