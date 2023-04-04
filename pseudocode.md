# **Django Jams**

## **Description**
- Create a music library database/API with Django

- Set up a Python/Django/Django REST Framework API app
- Create models that can be migrated into the database from a reference to a DB Diagram to serve as the backend for an application like spotify or apple music

Ports served:
- Postgres DB: 5432 (automatic)
- Django server: 8000 (when running manage.py runserver)

## **MVP**
- App should be able to perform CRUD operations on multiple models…
    - Song
    - Album
    - Artist
    - Playlists
- …as well as have routes to display information as JSON
- App should include all migrations for database models

## **Requirements**
- Create and submit (for approval) an object relationship diagram (dbdiagram.io)
	- Diagram should take into consideration:
		- Relationship between different tables
		- Considerations for null, blank fields, default values, other options
		- Account for ManyToMany tables in diagram, but not in Django
- Create models in Django to store data in PostgreSQL database
	- Minimum of (1) foreign key relationship
	- Minimum of (1) many to many relationship
- how READ functionality of all models through url collections from DRF with Thunder Client (VSCode Extension) requests for all models to get all data in each table/model
- Implement full CRUD for (at minimum) one model with at least one relationship
- Use Django REST Framework to build an api and routes for queries
- Use Thunder Client to prove the functionality of the Create, Read, Update, and Delete Routes.
	- You can also test some routes in the browser, as long as they are GET routes

## **Route Requirements**
- GET for all models at `/api/[model-name]/`- returns all objects for that model
	- Nested data is unnecessary for MVP, just FKs in the field data is ok
- GET for single instances of models `/api/[model-name]/[pk]/`- returns a single object
- POST routes for each model at `/api/model-name/pk`
- UPDATE routes for each model at `/api/model-name/pk`
- DELETE routes for each model at `/api/model-name/pk`

## **Tables/columns:**

- song
	- id
	- name
	- artist_id
	- album_id

- artist
	- id
	- name

- album
	- id
	- title

- genre
	- id
	- type

- playlist
	- id
	- title

- song_playlist
	- id
    - song_id
    - playlist_id
#
![image](img/diagram-01.png)
#
## **Models:**

    class Song(model.Model):
        name = models.CharField(max_length=100)
        artist_id = models.ForeignKey(‘Artist’, on_delete=models.PROTECT, null=True)
        album_id = models.ForeignKey(‘Album’, on_delete=models.PROTECT, null=True)
        genre_id =  models.ForeignKey(‘Genre’, on_delete=models.PROTECT, null=True)
        songs_playlists = models.ManyToManyField(‘Playlists’, on_delete=models.PROTECT, null=True)

        def __str__(self):
        return self.name
#
    class Artist(model.Model):
        name = models.CharField(max_length=100)

        def __str__(self):
        return self.name
#
    class Album(model.Model):
        title = models.CharField(max_length=100)

        def __str__(self):
        return self.name
#
    class Genre(model.Model):
        type = models.CharField(max_length=100)

        def __str__(self):
        return self.name
#
    class Playlist(model.Model):
        title = models.CharField(max_length=100)

        def __str__(self):
        return self.name

## **Serializers:**
??????

## **Views**
### **(musiclibrary (PROJECT) folder)**

    from django.shortcuts import render
    from django.http import HttpResponse
    import .models import Song
    import .models import Artist
    import .models import Album
    import .models import Genre
    import .models import Playlist

    def get_song(request, song_id):
        selected_song = Song.objects.get(pk=song_id)
        print(selected_song)
        return HttpResponse('<h1>Song Title: %s</h1>' % selected_song.name)

    def get_artist(request, artist_id):
        selected_artist = Artist.objects.get(pk=artist_id)
        print(selected_artist)
        return HttpResponse('<h1>Artist Name: %s</h1>' % selected_artist.name)

    def get_album(request, album_id):
        selected_album = Album.objects.get(pk=album_id)
        print(selected_album)
        return HttpResponse('<h1>Album Title: %s</h1>' % selected_album.name)

    def get_genre(request, genre_id):
        selected_genre = Genre.objects.get(pk=genre_id)
        print(selected_genre)
        return HttpResponse('<h1>Genre: %s</h1>' % selected_genre.name)

    def get_playlist(request_playlist_id):
        selected_playlist = Playlist.objects.get(pk=playlist_id)
        print(selected_playlist)
        return HttpResponse('<h1>Playlist Name: %s</h1>' % selected_playlist.name)

## **URL's**
### **(djangojams (APP) folder)**

    from django.contrib import admin
    from django.urls import path
    from musiclibrary import views

    urlpatterns = [

    path(‘user/’, admin.site.urls),
    path(‘song/<int:song_id>/’,views.get_song),
    path(‘artist/<int:artist_id>/’,views.get_artist),
    path(‘album/<int:album_id>/’,views.get_album),
    path(‘genre/<int:genre_id>/’,views.get_genre),
    path(‘playlist/<int:playlist_id>/’,views.get_playlist),

    ]