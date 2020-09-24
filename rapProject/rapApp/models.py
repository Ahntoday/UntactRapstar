from django.db import models

# Create your models here.

class Beat(models.Model):
    beat_title = models.CharField(max_length=90)
    beat_producer = models.CharField(max_length=60)
    beat_file = models.FileField(blank=True, upload_to="beat")
    def __str__(self):
        return self.beat_title

class Lyrics(models.Model):
    subject = models.CharField(max_length=90)
    lines = models.TextField()
    def __str__(self):
        return self.subject

class Vote(models.Model):
    user = models.CharField(max_length=60)
    vote = models.ForeignKey("User", on_delete=models.CASCADE, related_name='vote')
    def __str__(self):
        return self.user

class User(models.Model):
    nickname =  models.CharField(max_length=120)
    lyrics = models.ForeignKey("Lyrics", on_delete=models.CASCADE, related_name='lyrics')
    beat = models.ForeignKey("Beat", on_delete=models.CASCADE, related_name='beat')
    rap = models.CharField(max_length=120)
    image = models.TextField()
    def __str__(self):
        return self.nickname