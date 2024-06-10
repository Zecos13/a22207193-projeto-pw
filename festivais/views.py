from django.shortcuts import render
from .models import Festival, Localizacao

def festivais(request):
    festivais = Festival.objects.all()
    localizacoes = Localizacao.objects.all()
    context = {'festivais': festivais, 'localizacoes': localizacoes}
    return render(request, 'festivais/festivais.html', context)

def festival(request, festival_id):
    festival = Festival.objects.get(pk=festival_id)
    context = {'festival': festival}
    return render(request, 'festivais/festival.html', context)