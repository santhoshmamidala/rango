from django.shortcuts import render
from django.http import HttpResponse

def first(request):
    #return HttpResponse("Rango says 'Here is about page'.<br/><a href='/RangoApp/'>Index</a>")
    context_dict = {'message': "This is about page."}
    return render(request, 'RangoApp/about.html', context_dict)