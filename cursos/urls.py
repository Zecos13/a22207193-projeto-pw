from django.urls import path
from . import views

app_name = 'cursos'

urlpatterns = [
    path('', views.home_view, name='homecursos_url'),
    path('<int:curso_id>/', views.curso_view, name='curso_url'),
    path('disciplina/<int:disciplina_id>/', views.disciplina_view, name='disciplina_url'),
    path('projeto/<str:projeto_nome>/', views.projeto_view, name='projeto_url'),
    path('registo/', views.registo_view, name="registo"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('novo_curso/', views.novo_curso_view, name="novo_curso_url"),
    path('edita_curso/<int:curso_id>/', views.edita_curso_view, name="edita_curso_url"),
    path('nova_disciplina/<int:curso_id>/', views.nova_disciplina_view, name="nova_disciplina_url"),
    path('edita_disciplina/<int:disciplina_id>/', views.edita_disciplina_view, name="edita_disciplina_url"),
    path('novo_projeto/<int:disciplina_id>/', views.novo_projeto_view, name="novo_projeto_url"),
    path('edita_projeto/<int:projeto_id>/', views.edita_projeto_view, name="edita_projeto_url"),
    path('novo_docente/<int:disciplina_id>/', views.novo_docente_view, name="novo_docente_url"),
    path('edita_docente/<int:docente_id>/<int:disciplina_id>/', views.edita_docente_view, name="edita_docente_url"),
]