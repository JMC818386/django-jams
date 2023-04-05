from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id','name']

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id','name']

class SongSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    album = AlbumSerializer()
    class Meta:
        model = Song
        fields = ['id', 'name', 'artist', 'album']

class UpdateSongSerializer(serializers.ModelSerializer):
    artist = serializers.PrimaryKeyRelatedField(queryset=Artist.objects.all())
    album = serializers.PrimaryKeyRelatedField(queryset=Album.objects.all())
    #genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True)
    class Meta:
        model = Song
        fields = ['id', 'name', 'artist', 'album']


