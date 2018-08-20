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
				"id": "7",
				"name": "Wedding"
			}
		]
	}
}

create_shoppinglist_mutation='''
mutation{
	createShoppinglist(name:"Wedding", description:"Jackie"){
		shoppinglist{
			id
			name
			description
		}
	}
}'''

create_shoppinglist_response={
	"data": {
		"createShoppinglist": {
			"shoppinglist": {
				"id": "5",
				"name": "Wedding",
				"description": "Jackie"
			}
		}
	}
}

query_single_shoppinglist='''
{
	shoppinglist(id:8)
	{
		id
		name
	}
		
}'''