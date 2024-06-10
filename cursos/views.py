from django.shortcuts import render, redirect
from .models import Curso, AreaCientifica, Disciplina, Projeto, LinguagemProgramacao, Docente
from django.contrib.auth import models
from django.contrib.auth import authenticate, login, logout
from functools import wraps
from django.http import HttpResponseForbidden
from django.contrib.auth.models import Group
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test
from .forms import cursoForm, disciplinaForm, projetoForm, areaCientificaForm, docenteForm, linguagemProgramacaoForm

def home_view(request):

    cursos = Curso.objects.all()
    context = {
        'cursos': cursos,
        }

    return render(request, 'cursos/homecursos.html', context)

def curso_view(request, curso_id):

    curso = Curso.objects.get(pk=curso_id)
    disciplinas = Disciplina.objects.filter(curso=curso)
    context = {
        'curso': curso,
        'disciplinas': disciplinas,
        }

    return render(request, 'cursos/curso.html', context)

def disciplina_view(request, disciplina_id):

    disciplina = Disciplina.objects.get(pk=disciplina_id)
    try:
        projeto = Projeto.objects.get(disciplina=disciplina)
    except Projeto.DoesNotExist:
        projeto = None

    linguagens = LinguagemProgramacao.objects.filter(projetos=projeto)

    docentes = Docente.objects.filter(disciplinas=disciplina)

    context = {
        'disciplina': disciplina,
        'projeto': projeto,
        'linguagens': linguagens,
        'docentes': docentes
        }

    return render(request, 'cursos/disciplina.html', context)


def projeto_view(request, projeto_nome):

    projeto = Projeto.objects.get(nome=projeto_nome)
    linguagens = LinguagemProgramacao.objects.filter(projetos=projeto)

    context = {
        'projeto': projeto,
        'linguagens': linguagens,
        }

    return render(request, 'cursos/projeto.html', context)


def registo_view(request):
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('cursos:login')

    return render(request, 'cursos/registo.html')


def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('cursos:homecursos_url')
        else:
            render(request, 'cursos/login.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'cursos/login.html')

def logout_view(request):
    logout(request)
    return redirect('cursos:login')


def group_required(*group_names):
    def in_groups(user):
        if user.is_authenticated:
            if bool(user.groups.filter(name__in=group_names)) | user.is_superuser:
                return True
        raise PermissionDenied
    return user_passes_test(in_groups)



#Curso

@group_required('Editor de Cursos', 'Admin')
def novo_curso_view(request):

    form = cursoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('cursos:homecursos_url')

    context = {'form': form}
    return render(request, 'cursos/novo_curso.html', context)

@group_required('Editor de Cursos', 'Admin')
def edita_curso_view(request, curso_id):
    curso = Curso.objects.get(pk=curso_id)

    if request.method == 'POST':
        form = cursoForm(request.POST, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos:curso_url', curso.name)
    else:
        form = cursoForm(instance=curso)

    context = {'form': form, 'curso': curso}
    return render(request, 'cursos/edita_curso.html', context)

@group_required('Admin')
def apaga_curso_view(request, curso_id):
    curso = Curso.objects.get(pk=curso_id)
    context = {'curso': curso}
    curso.delete()
    return render(request, 'cursos/homecursos.html', context)

#Disciplinas

@group_required('Editor de Cursos', 'Admin')
def nova_disciplina_view(request, curso_id):
    curso = Curso.objects.get(pk=curso_id)

    if request.method == 'POST':
        form = disciplinaForm(request.POST, request.FILES)
        if form.is_valid():
            disciplina = form.save(commit=False)
            disciplina.curso = curso
            disciplina.save()
            return redirect('cursos:curso_url', curso.id)
    else:
        form = disciplinaForm(initial={'curso': curso})

    context = {'form': form, 'curso':curso}
    return render(request, 'cursos/nova_disciplina.html', context)

@group_required('Editor de Cursos', 'Admin')
def edita_disciplina_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(pk=disciplina_id)
    curso = disciplina.curso

    if request.method == 'POST':
        form = disciplinaForm(request.POST, request.FILES, instance=disciplina)
        if form.is_valid():
            form.save()
            return redirect('cursos:disciplina_url', disciplina.id)
    else:
        form = disciplinaForm(instance=disciplina)

    context = {'form': form, 'disciplina': disciplina, 'curso': curso}
    return render(request, 'cursos/edita_disciplina.html', context)

@group_required('Admin')
def apaga_disciplina_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(pk=disciplina_id)
    context = {'disciplina': disciplina}
    disciplina.delete()
    return render(request, 'cursos/disciplina.html', context)

#Projetos

@group_required('Editor de Cursos', 'Admin')
def novo_projeto_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(pk=disciplina_id)

    if request.method == 'POST':
        form = projetoForm(request.POST, request.FILES)
        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.disciplina = disciplina
            projeto.save()
            return redirect('cursos:disciplina_url', disciplina.id)
    else:
        form = projetoForm(initial={'disciplina': disciplina})

    context = {'form': form, 'disciplina': disciplina}
    return render(request, 'cursos/novo_projeto.html', context)

@group_required('Editor de Cursos', 'Admin')
def edita_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(pk=projeto_id)
    disciplina = projeto.disciplina

    if request.method == 'POST':
        form = projetoForm(request.POST, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('cursos:projeto_url', projeto.nome)
    else:
        form = projetoForm(instance=projeto)

    context = {'form': form, 'projeto': projeto, 'disciplina': disciplina}
    return render(request, 'cursos/edita_projeto.html', context)

@group_required('Admin')
def apaga_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(pk=projeto_id)
    context = {'projeto': projeto}
    projeto.delete()
    return render(request, 'cursos/projeto.html', context)


#Docentes

@group_required('Editor de Cursos', 'Admin')
def novo_docente_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(pk=disciplina_id)

    if request.method == 'POST':
        form = docenteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cursos:disciplina_url', disciplina.id)
    else:
        form = docenteForm(initial={'disciplina': disciplina})

    context = {'form': form, 'disciplina':disciplina}
    return render(request, 'cursos/novo_docente.html', context)

@group_required('Editor de Cursos', 'Admin')
def edita_docente_view(request, docente_id, disciplina_id):
    docente = Docente.objects.get(pk=docente_id)
    disciplinas = docente.disciplinas
    disciplina = Disciplina.objects.get(pk=disciplina_id)

    if request.method == 'POST':
        form = docenteForm(request.POST, request.FILES, instance=docente)
        if form.is_valid():
            form.save()
            return redirect('cursos:disciplina_url', disciplina.id)
    else:
        form = docenteForm(instance=docente)

    context = {'form': form, 'docente': docente, 'disciplinas': disciplinas, 'disciplina': disciplina}
    return render(request, 'cursos/edita_docente.html', context)

@group_required('Admin')
def apaga_docente_view(request, docente_id):
    docente = Docente.objects.get(pk=docente_id)
    context = {'docente': docente}
    docente.delete()
    return render(request, 'cursos/disciplina.html', context)