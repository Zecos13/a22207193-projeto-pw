from django.shortcuts import render
import requests
from datetime import datetime

# Create your views here.

def index(request):

    url = 'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
    resposta_previsao = requests.get(url)
    resposta_previsao.raise_for_status()
    dados = resposta_previsao.json()

    if not isinstance(dados, dict) or 'data' not in dados:
        raise ValueError("'data'")

    previsao_hoje = dados['data'][0]
    weather_type = previsao_hoje['idWeatherType']

    current_hour = datetime.now().hour
    if 7 <= current_hour < 19:
        nome_icon = f'w_ic_d_{weather_type:02}anim.svg'
    else:
        nome_icon = f'w_ic_n_{weather_type:02}anim.svg'

    url_icon = f'/static/meteo/icons/{nome_icon}'

    context = {
        'icon_url': url_icon,

    }

    return render(request, 'portfolio/index.html', context)


def aboutme_view(request):

    url = 'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
    resposta_previsao = requests.get(url)
    resposta_previsao.raise_for_status()
    dados = resposta_previsao.json()

    if not isinstance(dados, dict) or 'data' not in dados:
        raise ValueError("'data'")

    previsao_hoje = dados['data'][0]
    weather_type = previsao_hoje['idWeatherType']

    current_hour = datetime.now().hour
    if 7 <= current_hour < 19:
        nome_icon = f'w_ic_d_{weather_type:02}anim.svg'
    else:
        nome_icon = f'w_ic_n_{weather_type:02}anim.svg'

    url_icon = f'/static/meteo/icons/{nome_icon}'

    context = {
        'icon_url': url_icon,

    }


    return render(request, 'portfolio/aboutme.html', context)

def webtools_view(request):

    url = 'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
    resposta_previsao = requests.get(url)
    resposta_previsao.raise_for_status()
    dados = resposta_previsao.json()

    if not isinstance(dados, dict) or 'data' not in dados:
        raise ValueError("'data'")

    previsao_hoje = dados['data'][0]
    weather_type = previsao_hoje['idWeatherType']

    current_hour = datetime.now().hour
    if 7 <= current_hour < 19:
        nome_icon = f'w_ic_d_{weather_type:02}anim.svg'
    else:
        nome_icon = f'w_ic_n_{weather_type:02}anim.svg'

    url_icon = f'/static/meteo/icons/{nome_icon}'

    context = {
        'icon_url': url_icon,

    }


    return render(request, 'portfolio/webtools.html', context)

