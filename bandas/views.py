from django.shortcuts import render, redirect
from .models import Band, Album, Song
from django.contrib.auth import models
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from functools import wraps
from django.http import HttpResponseForbidden
from django.contrib.auth.models import Group
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test
from .forms import bandForm, albumForm, songForm



def album_view(request, album_id):
    album = Album.objects.get(pk=album_id)
    context = {'album': album}
    return render(request, 'bandas/album.html', context)

def band_view(request, band_id):
    band = Band.objects.get(pk=band_id)
    albums = band.album_set.all()
    context = {'band': band, 'albums': albums}
    return render(request, 'bandas/band.html', context)

def song_view(request, song_id):
    song = Song.objects.get(pk=song_id)
    context = {'song': song}
    return render(request, 'bandas/song.html', context)

def bandList_view(request):
    bands = Band.objects.all()
    context = {'bands': bands}
    return render(request, 'bandas/bandList.html', context)

def registo_view(request):
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('bandas:login')

    return render(request, 'bandas/registo.html')


def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('bandas:bandas_url')
        else:
            render(request, 'bandas/login.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'bandas/login.html')

def logout_view(request):
    logout(request)
    return redirect('bandas:login')

def group_required(*group_names):
    def in_groups(user):
        if user.is_authenticated:
            if bool(user.groups.filter(name__in=group_names)) | user.is_superuser:
                return True
        raise PermissionDenied
    return user_passes_test(in_groups)

#Bandas

@group_required('Editor de Bandas', 'Admin')
def nova_banda_view(request):

    form = bandForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('bandas:bandas_url')

    context = {'form': form}
    return render(request, 'bandas/nova_banda.html', context)

@group_required('Editor de Bandas', 'Admin')
def edita_banda_view(request, band_id):
    band = Band.objects.get(pk=band_id)

    if request.method == 'POST':
        form = bandForm(request.POST, request.FILES, instance=band)
        if form.is_valid():
            form.save()
            return redirect('bandas:banda_url', band.id)
    else:
        form = bandForm(instance=band)

    context = {'form': form, 'band': band}
    return render(request, 'bandas/edita_banda.html', context)

@group_required('Admin')
def apaga_band_view(request, band_id):
    band = Band.objects.get(pk=band_id)
    context = {'band': band}
    band.delete()
    return render(request, 'bandas/band.html', context)

#Albuns

@group_required('Editor de Bandas', 'Admin')
def novo_album_view(request, band_id):
    band = Band.objects.get(pk=band_id)

    if request.method == 'POST':
        form = albumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save(commit=False)
            album.band = band
            album.save()
            return redirect('bandas:band_url', band.name)
    else:
        form = albumForm(initial={'band': band})

    context = {'form': form, 'band':band}
    return render(request, 'bandas/novo_album.html', context)

@group_required('Editor de Bandas', 'Admin')
def edita_album_view(request, album_id):
    album = Album.objects.get(pk=album_id)
    band = album.band

    if request.method == 'POST':
        form = albumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('bandas:album_url', album.title)
    else:
        form = albumForm(instance=album)

    context = {'form': form, 'album': album, 'band': band}
    return render(request, 'bandas/edita_album.html', context)

@group_required('Admin')
def apaga_album_view(request, album_id):
    album = Album.objects.get(pk=album_id)
    context = {'album': album}
    album.delete()
    return render(request, 'bandas/album.html', context)

#musicas

@group_required('Editor de Bandas', 'Admin')
def nova_musica_view(request, album_id):
    album = Album.objects.get(pk=album_id)

    if request.method == 'POST':
        form = songForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.album = album
            song.save()
            return redirect('bandas:album_url', album.id)
    else:
        form = songForm(initial={'album': album})

    context = {'form': form, 'album':album}
    return render(request, 'bandas/nova_musica.html', context)

@group_required('Editor de Bandas', 'Admin')
def edita_musica_view(request, song_id):
    song = Song.objects.get(pk=song_id)
    album = song.album

    if request.method == 'POST':
        form = songForm(request.POST, request.FILES, instance=song)
        if form.is_valid():
            form.save()
            return redirect('bandas:song_url', song.id)
    else:
        form = songForm(instance=song)

    context = {'form': form, 'album': album, 'song': song}
    return render(request, 'bandas/edita_musica.html', context)

@group_required('Admin')
def apaga_musica_view(request, song_id):
    song = Song.objects.get(pk=song_id)
    context = {'song': song}
    song.delete()
    return render(request, 'bandas/song.html', context)
