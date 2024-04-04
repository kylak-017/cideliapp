from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
    return HttpResponse("Hello, welcome to CI Deli Pre-Order System.") #getting an html page

# Create your views here.
