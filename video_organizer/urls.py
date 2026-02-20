from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

#urlpatterns is a variable that is used for the urls.py in the Quiz_Game folder 
#basically for pathing and rendering different templates
urlpatterns = [
    path("", views.index, name="main"),
    path("overview/", views.overview, name="overview"),
    path("rooms/", views.rooms, name="rooms"),
    path("dvd", views.dvd, name="dvd"),
    path("movie/add", views.process_movie_entry, name="process_movie_entry"),
    path("dvd/update/<int:id>", views.update_movie_entry, name="update_movie_entry"),
    path("dvd/update", views.dvd_update, name="dvd_update")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
