from django.db import models

# album red primary key has 1
class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=500)
    album_logo = models.CharField(max_length=1000)

    #string representation of the pbject
    def __str__(self):
        return self.album_title + ' - ' + self.artist

class Songs(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
