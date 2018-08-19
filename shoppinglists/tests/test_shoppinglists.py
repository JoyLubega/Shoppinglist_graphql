from shoppinglistapi.schema import schema
import json
from django.test import TestCase
from django.test import Client
from .data import BaseTest
from ..fixtures.query_shoppinglists import (create_shoppinglist_mutation,
                create_shoppinglist_response,query_all_shoppiglists, expected_query_response)
from ..fixtures.user.create_user import query_create_user,query_login




class ShoppinglistsTestCase(BaseTest):

    def test_create_shoppinglists(self):
        '''
        Test for creating a shoppinglist with all attributes
        '''
        query = self.client.post(
            '/shoppinglists?query='+create_shoppinglist_mutation,
            HTTP_AUTHORIZATION=self.test_token,
            content_type='application/json'
        )
        jresp = json.loads(query.content.decode())
        self.assertEquals(jresp,create_shoppinglist_response)
    def test_query_all_shoppinglist(self):
        '''
        Test for query all shoppinglists 
        '''
        query_create = self.client.post(  # create a shoppinglist
            '/shoppinglists?query='+create_shoppinglist_mutation,
            HTTP_AUTHORIZATION=self.test_token,
            content_type='application/json'
        )
        query = self.client.post(
        '/shoppinglists?query='+query_all_shoppiglists,
            HTTP_AUTHORIZATION=self.test_token,
            content_type='application/json'
        )
        jresp = json.loads(query.content.decode())
        
        self.assertEquals(jresp,expected_query_response)

        
        
        
