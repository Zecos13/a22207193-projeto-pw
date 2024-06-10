from django.urls import path
from . import views

app_name = 'bandas'

urlpatterns = [
    path('', views.bandList_view, name='bandas_url'),
    path('band/<int:band_id>/', views.band_view, name='banda_url'),
    path('album/<int:album_id>/', views.album_view, name='album_url'),
    path('song/<int:song_id>/', views.song_view, name='song_url'),
    path('registo/', views.registo_view, name="registo"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('nova_banda/', views.nova_banda_view, name="nova_banda_url"),
    path('edita_banda/<int:band_id>/', views.edita_banda_view, name="edita_banda_url"),
    path('novo_album/<int:band_id>/', views.novo_album_view, name="novo_album_url"),
    path('edita_album/<int:album_id>/', views.edita_album_view, name="edita_album_url"),
    path('nova_musica/<int:album_id>/', views.nova_musica_view, name="nova_musica_url"),
    path('edita_musica/<int:song_id>/', views.edita_musica_view, name="edita_musica_url"),
]