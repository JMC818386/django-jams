from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from musiclibrary import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'songs', views.SongViewSet)
router.register(r'artists', views.ArtistViewSet)
router.register(r'albums', views.AlbumViewSet)
router.register(r'genres', views.GenreViewSet)
router.register(r'playlists', views.PlaylistViewSet)
router.register(r'updatesong', views.UpdateSongViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
