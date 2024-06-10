from django.urls import path
from . import views

app_name = 'meteo'

urlpatterns = [
    path('', views.index_view, name='index_url'),
    path('cinco_dias/', views.cinco_dias_view, name='cinco_dias_url'),
    path('api_meteo/', views.api_meteo_view, name='api_meteo_url'),
]