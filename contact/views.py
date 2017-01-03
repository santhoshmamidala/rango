from django.shortcuts import render
from django.http import HttpResponse

def info(request):
    return HttpResponse("This is contact info page.<br/><a href=/RangoApp/>Index</a>")
