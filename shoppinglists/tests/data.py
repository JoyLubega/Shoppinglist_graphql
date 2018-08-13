import json
from django.test import TestCase
from django.test import Client
from ..fixtures.user.create_user import user_token

# Inherit from this in your test cases
class Base():

    def setUp(self):
        self._client = Client()

    def query_auth(self, query: str):
        '''
        Args:
            query (string) - GraphQL query to run
            
        Returns:
            dict, response from graphql endpoint.  The response has the "data" key.
                  It will have the "error" key if any error happened.
        '''
        body = {'query': query}
        

        resp = self._client.post('/shoppinglists', json.dumps(body),
                                 content_type='application/json')
        jresp = json.loads(resp.content.decode())
        return jresp

    def query_other(self, query: str):
        '''
        Args:
            query (string) - GraphQL query to run
            
        Returns:
            dict, response from graphql endpoint.  The response has the "data" key.
                  It will have the "error" key if any error happened.
        '''
        body = {'query': query}
        

        resp = self._client.post('/shoppinglists', json.dumps(body),
                                 content_type='application/json', HTTP_AUTHORIZATION='JWT '+ user_token)
        jresp = json.loads(resp.content.decode())
        
        return jresp

    def assertResponseNoErrors(self, resp: dict, expected: dict):
        '''
        Assert that the resp (as retuened from query) has the data from
        expected
        '''
        self.assertNotIn('errors', resp, 'Response had errors')
        self.assertEqual(resp, expected, 'Response has correct data')