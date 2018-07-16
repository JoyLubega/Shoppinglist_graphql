query_all_shoppiglists = '''
    {
	allShoppinglists{
		id
		name
	}
}
'''
expected_query_response = {
	"data": {
		"allShoppinglists": [
			{
				"id": "1",
				"name": "Trip to London"
			}
		]
	}
}