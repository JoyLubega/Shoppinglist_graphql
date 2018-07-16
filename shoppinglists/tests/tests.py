from django.test import TestCase
from ..fixtures.query_shoppinglists import query_all_shoppiglists,expected_query_response
from ..data import initialize
from shoppinglistapi.schema import schema
import json


import pytest
# Create your tests here.

pytestmark = pytest.mark.django_db

class ApiTestCase(TestCase):
    def test_mutations(self):
        initialize() 
        result = schema.execute(query_all_shoppiglists)
        assert not result.errors
        assert json.dumps(result.data) == json.dumps(expected_query_response.get('data'))