from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Inside the app")


INSERT INTO flights (origin, destination, duration) VALUES ("New York", "London", 425);
