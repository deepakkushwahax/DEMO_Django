from django.shortcuts import render
from django.http import HttpRequest

def greetings(request):
    s = "Hello and Welcome to first view"
    return HttpRequest(s)