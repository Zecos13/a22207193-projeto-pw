from django.shortcuts import render
from datetime import datetime

def index_view(request):
    return render(request, "pwsite/index.html", {
        'ano': datetime.today().year
        })

def sobre_view(request):
    return render(request, "pwsite/sobre.html", {
        'ano': datetime.today().year
        })

def interesses_view(request):
    return render(request, "pwsite/interesses.html", {
        'ano': datetime.today().year
        })