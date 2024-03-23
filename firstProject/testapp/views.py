from django.shortcuts import render
from django.http import HttpResponse

def greetings(request):
    s = "<h1>Hello and Welcome to first view</h1>"
    return HttpResponse(s)