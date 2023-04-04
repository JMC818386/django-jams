from django.db import models

class Song(models.Model):
    name = models.CharField(max_length=100)
    #artist = models.ForeignKey('Artist', on_delete=models.PROTECT, null=True)
    #album = models.ForeignKey('Album', on_delete=models.PROTECT, null=True)
    #playlists = models.ManyToManyField('Playlists', on_delete=models.PROTECT, null=True)
    #genres = models.ManyToManyField('Genre', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name
