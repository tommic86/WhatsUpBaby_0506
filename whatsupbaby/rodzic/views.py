from django.shortcuts import render, render_to_response
from rodzic.models import Dziecko, Rodzic

def dziecko_szczegoly(request, *args, **kwargs):
    pk = kwargs['pk']
    dziecko = Dziecko.objects.get(pk=pk)
    rodzice = Rodzic.objects.filter(dziecko=pk)

    return render_to_response('dziecko_szczegoly.html', {
        "dziecko": dziecko,
        "rodzice": rodzice,
    })

def home(request):
    #return render_to_response('home.html',
    #                         {'full_name': request.user.username})
    return render(request, 'home.html', {'full_name': request.user.username})