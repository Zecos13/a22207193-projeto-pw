from django.shortcuts import render
import requests
from datetime import datetime

def index_view(request):

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
        'cidade': 'Lisboa',
        'temperatura_minima': previsao_hoje['tMin'],
        'temperatura_maxima': previsao_hoje['tMax'],
        'icon_url': url_icon,
        'precipita_prob': previsao_hoje['precipitaProb'],
        'pred_wind_dir': previsao_hoje['predWindDir'],
        'class_wind_speed': previsao_hoje['classWindSpeed'],
        'longitude': previsao_hoje['longitude'],
        'latitude': previsao_hoje['latitude'],
        'data': previsao_hoje['forecastDate'],
    }

    return render(request, 'meteo/index.html', context)

def get_nome_cidade(global_id_local):
    cidades_url = 'https://api.ipma.pt/open-data/distrits-islands.json'
    response = requests.get(cidades_url)
    response.raise_for_status()
    cidades_data = response.json()

    for cidade in cidades_data['data']:
        if cidade['globalIdLocal'] == global_id_local:
            return cidade['local']
    return 'Cidade Desconhecida'


def get_cidades():
    cities_url = 'https://api.ipma.pt/open-data/distrits-islands.json'
    response = requests.get(cities_url)
    if response.status_code == 200:
        return response.json()['data']
    else:
        return []


def cinco_dias_view(request):
    global_id_local = request.GET.get('global_id_local')

    try:
        global_id_local = int(global_id_local)
    except (TypeError, ValueError):
        global_id_local = 1110600

    nome_cidade = get_nome_cidade(global_id_local)

    url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{global_id_local}.json'
    response = requests.get(url)
    response.raise_for_status()
    dados = response.json()

    if not isinstance(dados, dict) or 'data' not in dados:
        raise ValueError("Inválido")

    forecasts = []

    for dia in dados['data'][:5]:
        meteorologia_type = dia['idWeatherType']

        current_hour = datetime.now().hour
        if 7 <= current_hour < 19:
            nome_icon = f'w_ic_d_{meteorologia_type:02}anim.svg'
        else:
            nome_icon = f'w_ic_n_{meteorologia_type:02}anim.svg'

        url_icon = f'/static/meteo/icons/{nome_icon}'

        forecasts.append({
            'temperatura_minima': dia['tMin'],
            'temperatura_maxima': dia['tMax'],
            'icon_url': url_icon,
            'precipita_prob': dia['precipitaProb'],
            'pred_wind_dir': dia['predWindDir'],
            'class_wind_speed': dia['classWindSpeed'],
            'longitude': dia['longitude'],
            'latitude': dia['latitude'],
            'data': dia['forecastDate'],
        })

    cities = get_cidades()

    context = {
        'cities': cities,
        'cidade': nome_cidade,
        'forecasts': forecasts,
    }
    return render(request, 'meteo/cinco_dias.html', context)


def api_meteo_view(request):



    return render(request, 'meteo/apimeteo.html')