from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def testpaper(request):
    template = loader.get_template('testpaper.html')
    res = template.render()
    return HttpResponse(res)

def result(request):
    s = "<h1>This is your test result</h1>"
    return HttpResponse(s)

