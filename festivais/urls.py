from django.urls import path
from . import views

app_name = 'festivais'

urlpatterns = [
    path('festivais/', views.festivais, name='festivais'),
    path('festival/<int:festival_id>/', views.festival, name='festival')
]