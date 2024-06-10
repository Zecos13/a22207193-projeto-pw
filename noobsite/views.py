# noobsite/views.py

from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")

def index_view2(request):
    return HttpResponse("Olá Acr, tens o nariz grande")

def index_view3(request):
    return HttpResponse("Olá Richards, já foste")

def index_view4(request):
    return HttpResponse("Olá DannyBoy, és Azeiteiro")
