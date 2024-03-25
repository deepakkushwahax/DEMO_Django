from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def testpaper(request):
    que="who Developed Python?"
    a="Dennis Ritchie"
    b="Guido Van Rossum"
    c="Ken Thompson"
    d="Bjarne Stroutrup"
    context={
        'que':que,
        'a':a,
        'b':b,
        'c':c,
        "d":d,
    }
    template = loader.get_template('testpaper.html')
    res = template.render(context,request)
    return HttpResponse(res)

def result(request):
    s = "<h1>This is your test result</h1>"
    return HttpResponse(s)

