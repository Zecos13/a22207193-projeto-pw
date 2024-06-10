from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.main_view, name='mainarticles_url'),
    path('author/<int:author_id>/', views.author_view, name='author_url'),
    path('article/<int:article_id>/', views.article_view, name='article_url'),
    path('registo/', views.registo_view, name="registo"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('novo_autor/', views.novo_autor_view, name="novo_autor_url"),
    path('edita_autor/<int:author_id>/', views.edita_autor_view, name="edita_autor_url"),
    path('novo_artigo/<int:author_id>/', views.novo_artigo_view, name="novo_artigo_url"),
    path('edita_artigo/<int:article_id>/', views.edita_artigo_view, name="edita_artigo_url"),
    path('novo_comentario/<int:article_id>/', views.novo_comentario_view, name="novo_comentario_url"),
    path('edita_comentario/<int:comment_id>/', views.edita_comentario_view, name="edita_comentario_url"),
    path('novo_rating/<int:article_id>/', views.novo_rating_view, name="novo_rating_url"),
    path('edita_rating/<int:rating_id>/', views.edita_rating_view, name="edita_rating_url"),
]