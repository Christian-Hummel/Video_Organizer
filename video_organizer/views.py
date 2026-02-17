from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash


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