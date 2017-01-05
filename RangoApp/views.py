from django.shortcuts import render
#from django.http import HttpResponse

def index(request):
    #return HttpResponse("Rango says 'Hey there world!'<br/> "
    #                    "<a href='/RangoApp/about'>About</a><br/>"
    #                    "<a href='/RangoApp/contact'>Contact</a>")
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'RangoApp/index.html', context_dict)
