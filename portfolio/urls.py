from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutme/', views.aboutme_view, name='aboutme'),
    path('webtools/', views.webtools_view, name='webtools'),
]