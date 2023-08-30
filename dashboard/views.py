from django.http import HttpResponse
import requests
from requests import get, auth
import environ
env = environ.Env()


client_id = env('client_id')
client_secret = env('client_secret')
a = auth.HTTPBasicAuth(client_id, client_secret)
url = "https://api.seatgeek.com/2/taxonomies"
res = requests.get(url, auth=a)
data = res.json()


def index(request):
      
    return HttpResponse(data)


def baseball(request, team):
    return HttpResponse("Baseball page")


def basketball(request):
    return HttpResponse("basketball page")


def football(request):
    return HttpResponse("football page")
