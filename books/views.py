from django.shortcuts import render, redirect
import requests
import json

def index(request):
	url = "http://127.0.0.1:8000/inventory/"

	headers = {
	    'authorization': "Token f7fbc4fd95db09db63b21e23dd1b07c521ab11c9",
	    'cache-control': "no-cache",
	    'postman-token': "bc61ac56-7eea-b712-fed8-73b5f67a01da"
	    }

	response = requests.request("GET", url, headers=headers)
	return render(request, 'books/index.html',{'data':json.loads(response.text)})
# Create your views here.
