from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from .models import Movie


import requests
import json


# Create your views here.

### Home Page
def index(request):

    return render(request, "main.html")


def overview(request):

    context = {}

    context["movies"] = Movie.objects.all().order_by('title')

    return render(request, "overview.html", context)

def rooms(request):

    return render(request, "rooms.html")

def dvd(request):
    

    return render(request, "dvd.html")

def process_movie_entry(request):
    if request.method == 'POST':

        title = request.POST.get('title')
        year = request.POST.get('year')
        genre = request.POST.get('genre')
        description = request.POST.get('description')
        director = request.POST.get('director')
        runtime = request.POST.get('runtime')
        type = request.POST.get('type')
        viewed = request.POST.get('viewed')
        picture_description = request.POST.get('picture_description')
        picture = request.FILES.get('picture')

        movie = Movie(title=title, year=year, genre=genre, description=description, director=director, runtime=runtime, type=type, viewed=viewed, picture_description=picture_description,picture=picture)

        if not Movie.objects.filter(title=request.POST.get('title')).first():
            movie.save()
        else:
            messages.error(request, "Dieser Film ist bereits gespeichert")
            return HttpResponseRedirect(reverse_lazy("dvd"))
    

        messages.success(request, "Der Film wurde erfolgreich gespeichert")

        url = reverse("dvd")
        return HttpResponseRedirect(url)
    else:
        return HttpResponse("Invalid request method!")
    


def update_movie_entry(request, id):
    context = {}

    movie = Movie.objects.get(id=id)

    context["movie"] = movie


    return render(request, "dvdupdate.html", context)


def dvd_update(request):
    if request.method == 'POST':

        id = request.POST.get('movie_id')

        movie = get_object_or_404(Movie, id=id)

        new_title = request.POST.get('title')
        new_year = request.POST.get('year')
        new_genre = request.POST.get('genre')
        new_description = request.POST.get('description')
        new_director = request.POST.get('director')
        new_runtime = request.POST.get('runtime')
        new_type = request.POST.get('type')
        new_viewed = request.POST.get('viewed')
        new_picture_description = request.POST.get('picture_description')

        
        if request.FILES.get('picture'):
            new_picture = request.FILES.get('picture')

            movie.picture = new_picture

        if not request.FILES.get('picture') and movie.title == new_title and movie.year == int(new_year) and movie.genre == new_genre and movie.description == new_description and movie.director == new_director and movie.runtime == int(new_runtime) and movie.type == new_type and movie.viewed == new_viewed and movie.picture_description == new_picture_description:
            messages.error(request, "Diese Daten sind bereits gespeichert")
            url = reverse("update_movie_entry", kwargs={'id': id})
            return HttpResponseRedirect(url)


        movie.title = new_title
        movie.year = new_year
        movie.genre = new_genre
        movie.description = new_description
        movie.director = new_director
        movie.runtime = new_runtime
        movie.type = new_type
        movie.viewed = new_viewed
        movie.picture_description = new_picture_description

        movie.save()
    

        messages.success(request, "Änderungen erfolgreich gespeichert")

        url = reverse("update_movie_entry", kwargs={'id': id})
        return HttpResponseRedirect(url)
    else:
        return HttpResponse("Invalid request method!")
    

def delete_movie(request, id):
    
    movie = Movie.objects.get(id=id)

    movie.delete()

    messages.success(request, f"{movie.title} wurde erfolgreich gelöscht")

    url = reverse("overview")
    return HttpResponseRedirect(url)