from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# These are the endpoints

def home(request):
    return  HttpResponse("RS3 Home")