from django.db import models

#RED pk 1
class Album(models.Model):
    artist=     models.CharField(max_length=250)
    album_title=models.CharField(max_length=500)
    genre=      models.CharField(max_length=150)
    album_logo= models.CharField(max_length=1000)
    def __str__(self):#when ever i want to represent album i see title+arist
        return self.album_title+"-"+self.artist

class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
  #each song is connected to a album_id
  # what on_delete does is is that if
# the album to which the song is linked to
 # is deleted then the song is also deleted
    file_type=models.CharField(max_length=10)
    song_title=models.CharField(max_length=250)
    is_favourite=models.BooleanField(default=False)
#migrations are just the changes to your database
    def __str__(self):#when ever i want to represent album i see title+arist
        return self.song_title
