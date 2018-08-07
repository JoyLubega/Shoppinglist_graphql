query_create_user="""mutation{
	createUser(username:"joyNamu",email:"joyce@gmail.com",password:"password",firstName:"Joyce",lastName:"Namuli"){
		user{
			id
			username
			
		}
	}
	
}"""

create_user_response={
	"data": {
		"createUser": {
			"user": {
				"id": "1",
				"username": "joyNamu"
			}
		}
	}
}

query_login='''mutation{
	loginUser(username:"joyNamu",password:"password"){
token
	}
	
}'''

login_reponse={
	"data": {
		"loginUser": {
			"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImpveU5hbXUiLCJleHAiOjE1MzM1ODY0MzIsIm9yaWdfaWF0IjoxNTMzNTg2MTMyfQ.yNPIYMC9VKzEGYc5HO4lKXu7QED_NLLWOOzkYrWXm_A"
		}
	}
}

user_token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImpveU5hbXUiLCJleHAiOjE1MzM1ODY0MzIsIm9yaWdfaWF0IjoxNTMzNTg2MTMyfQ.yNPIYMC9VKzEGYc5HO4lKXu7QED_NLLWOOzkYrWXm_A'