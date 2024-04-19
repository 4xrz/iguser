import requests
from flask import Flask,request

my_api=Flask('app')
@my_api.route('/')
def hi():
	user = request.args.get("user")
	req = requests.get('https://gramsnap.com/api/ig/userInfoByUsername/'+user)
	if req.status_code == 500:
		av = {'user':user,
		'status':'available'}
		return av
	else:
		unav = {'user':user,
		'status':'unavailable'}
		return unav
my_api.run(host='0.0.0.0', port=8080)