from django.db import models

# Create your models here.

class Beat(models.Model):
    beat_genre = models.CharField(max_length=60)
    beat_file = models.CharField(max_length=120)

class Lyrics(models.Model):
    subject = models.CharField(max_length=90)
    lines = models.TextField()

class Vote(models.Model):
    user = models.CharField(max_length=60)
    vote = models.ForeignKey("User", on_delete=models.CASCADE, related_name='vote')

class User(models.Model):
    nickname =  models.CharField(max_length=120)
    lyrics = models.ForeignKey("Lyrics", on_delete=models.CASCADE, related_name='lyrics')
    beat = models.ForeignKey("Beat", on_delete=models.CASCADE, related_name='beat')
    rap = models.CharField(max_length=120)
    image = models.TextField()