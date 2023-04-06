from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny]

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class UpdateSongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = UpdateSongSerializer
    http_method_names = ('get', 'post', 'put', 'patch', 'delete')

class ArtistViewSet(viewsets.ModelViewSet):
        queryset = Artist.objects.all()
        serializer_class = ArtistSerializer

class AlbumViewSet(viewsets.ModelViewSet):
        queryset = Album.objects.all()
        serializer_class = AlbumSerializer

class GenreViewSet(viewsets.ModelViewSet):
        queryset = Genre.objects.all()
        serializer_class = GenreSerializer

class PlaylistViewSet(viewsets.ModelViewSet):
        queryset = Playlist.objects.all()
        serializer_class = PlaylistSerializer

# class UpdatePlaylistViewSet(viewsets.ModelViewSet):
#     queryset = Playlist.objects.all()
#     serializer_class = UpdatePlaylistSerializer
#     http_method_names = ('post', 'put', 'patch', 'delete')