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

create_shoppinglist_mutation='''
mutation{
	createShoppingliist(name:"Wedding", description:"Jackie"){
		shoppinglist{
			id
			name
			description
		}
	}
}'''

create_shoppinglist_response={
	"data": {
		"createShoppingliist": {
			"shoppinglist": {
				"id": "17",
				"name": "Wedding",
				"description": "Jackie"
			}
		}
	}
}