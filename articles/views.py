from django.shortcuts import render, redirect
from .models import Article, Author, Comment, Rating
from django.contrib.auth import models
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from functools import wraps
from django.http import HttpResponseForbidden
from django.contrib.auth.models import Group
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test
from .forms import authorForm, articleForm, commentForm

# Create your views here.
def article_view(request, article_id):
    article = Article.objects.get(pk=article_id)
    comments = Comment.objects.filter(article=article_id)
    ratings = Rating.objects.filter(article_rated=article_id)
    context = {
        'article': article,
        'comments': comments,
        'ratings':ratings
        }
    return render(request, 'articles/article.html', context)

def author_view(request, author_id):
    author = Author.objects.get(pk=author_id)
    articles = Article.objects.filter(author=author)
    context = {
        'author': author,
        'articles': articles
        }
    return render(request, 'articles/author.html', context)

def main_view(request):
    articles = Article.objects.all()
    authors = Author.objects.all()
    context = {
        'articles': articles,
        'authors': authors
        }
    return render(request, 'articles/mainarticles.html', context)

def registo_view(request):
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('articles:login')

    return render(request, 'articles/registo.html')


def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('articles:mainarticles_url')
        else:
            render(request, 'articles/login.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'articles/login.html')

def logout_view(request):
    logout(request)
    return redirect('articles:login')


def group_required(*group_names):
    def in_groups(user):
        if user.is_authenticated:
            if bool(user.groups.filter(name__in=group_names)) | user.is_superuser:
                return True
        raise PermissionDenied
    return user_passes_test(in_groups)


#Author

@group_required('Editor de Artigos', 'Admin')
def novo_autor_view(request):

    form = authorForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('articles:mainarticles_url')

    context = {'form': form}
    return render(request, 'articles/novo_autor.html', context)

@group_required('Editor de Artigos', 'Admin')
def edita_autor_view(request, author_id):
    author = Author.objects.get(pk=author_id)

    if request.method == 'POST':
        form = authorForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            return redirect('articles:author_url', author.name)
    else:
        form = authorForm(instance=author)

    context = {'form': form, 'author': author}
    return render(request, 'articles/edita_autor.html', context)

@group_required('Admin')
def apaga_autor_view(request, author_id):
    author = Author.objects.get(pk=author_id)
    context = {'author': author}
    author.delete()
    return render(request, 'articles/mainarticles.html', context)


#Article

@group_required('Editor de Artigos', 'Admin')
def novo_artigo_view(request, author_id):

    form = articleForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('articles:mainarticles_url')

    context = {'form': form}
    return render(request, 'articles/novo_artigo.html', context)

@group_required('Editor de Artigos', 'Admin')
def edita_artigo_view(request, article_id):
    article = Article.objects.get(pk=article_id)

    if request.method == 'POST':
        form = articleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:article_url', article.title)
    else:
        form = articleForm(instance=article)

    context = {'form': form, 'article': article}
    return render(request, 'articles/edita_artigo.html', context)

@group_required('Admin')
def apaga_artigo_view(request, article_id):
    article = Article.objects.get(pk=article_id)
    context = {'article': article}
    article.delete()
    return render(request, 'articles/mainarticles.html', context)


#Comment

@group_required('Editor de Artigos', 'Admin')
def novo_comentario_view(request, article_id):
    article = Article.objects.get(pk=article_id)

    if request.method == 'POST':
        form = commentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('article:article', article.title)
    else:
        form = commentForm(initial={'article': article})

    context = {'form': form, 'article':article}
    return render(request, 'articles/novo_comentario.html', context)

@group_required('Editor de Artigos', 'Admin')
def edita_comentario_view(request, author_id):
    author = Author.objects.get(pk=author_id)

    if request.method == 'POST':
        form = authorForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            return redirect('articles:author_url', author.name)
    else:
        form = authorForm(instance=author)

    context = {'form': form, 'author': author}
    return render(request, 'articles/edita_autor.html', context)

@group_required('Admin')
def apaga_comentario_view(request, author_id):
    author = Author.objects.get(pk=author_id)
    context = {'author': author}
    author.delete()
    return render(request, 'articles/mainarticles.html', context)


#Rating

@group_required('Editor de Artigos', 'Admin')
def novo_rating_view(request):

    form = articleForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('articles:mainarticles_url')

    context = {'form': form}
    return render(request, 'articles/novo_artigo.html', context)

@group_required('Editor de Artigos', 'Admin')
def edita_rating_view(request, author_id):
    author = Author.objects.get(pk=author_id)

    if request.method == 'POST':
        form = authorForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            return redirect('articles:author_url', author.name)
    else:
        form = authorForm(instance=author)

    context = {'form': form, 'author': author}
    return render(request, 'articles/edita_autor.html', context)

@group_required('Admin')
def apaga_rating_view(request, author_id):
    author = Author.objects.get(pk=author_id)
    context = {'author': author}
    author.delete()
    return render(request, 'articles/mainarticles.html', context)