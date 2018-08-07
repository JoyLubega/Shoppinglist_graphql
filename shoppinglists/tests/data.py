import json
from django.test import TestCase
from django.test import Client
from ..fixtures.user.create_user import user_token

# Inherit from this in your test cases
class GraphQLTestCase(TestCase):

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
                                 content_type='application/json', Authorization='JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImpveU5hbXUiLCJleHAiOjE1MzM2MjA4NDEsIm9yaWdfaWF0IjoxNTMzNjIwNTQxfQ.F5Hq9UUKUCIut2hVDiC65N3pemXq2V5QT28Pvupn3oA')
        jresp = json.loads(resp.content.decode())
        print(jresp)
        return jresp

    def assertResponseNoErrors(self, resp: dict, expected: dict):
        '''
        Assert that the resp (as retuened from query) has the data from
        expected
        '''
        self.assertNotIn('errors', resp, 'Response had errors')
        self.assertEqual(resp, expected, 'Response has correct data')