from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import Movie


import requests
import json


# Create your views here.

### Home Page
def index(request):

    return render(request, "main.html")


def overview(request):

    return render(request, "overview.html")

def rooms(request):

    return render(request, "rooms.html")

def dvd(request):

    return render(request, "dvd.html")

def process_movie_entry(request):
    if request.method == 'POST':

        title = request.POST.get('title')
        year = request.POST.get('year')
        description = request.POST.get('description')
        director = request.POST.get('director')
        type = request.POST.get('type')
        picture_description = request.POST.get('picture_description')
        picture = request.FILES.get('picture')

        movie = Movie(title=title, year=year, description=description, director=director,type=type, picture_description=picture_description,picture=picture)

        movie.save()
    

        return render(request, "movie_success.html")
    else:
        return HttpResponse("Invalid request method!")