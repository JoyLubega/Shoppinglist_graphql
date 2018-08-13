query_create_user="""mutation{
	createUser(username:"jdo",email:"johndoe@gmail.com",password:"password",firstName:"John",lastName:"Doe"){
		user{
			username
			
		}
	}
	
}"""

create_user_response={
	"data": {
		"createUser": {
			"user": {
				"username": "jdo"
			}
		}
	}
}

query_login='''mutation{
	loginUser(username:"jdo",password:"password"){
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