from django.shortcuts import render
from django.http import HttpResponse

def first(request):
    return HttpResponse("Rango says 'Here is about page'.<br/><a href='/RangoApp/'>Index</a>")
