from django.db import models

class Band(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='bandas/', null=True, blank=True)
    info = models.TextField()
    biography = models.TextField(null=True, blank=True)
    yearFormation = models.PositiveIntegerField(blank=True)
    genre = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=100)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='bandas/', null=True, blank=True)
    releaseDate = models.DateField()
    label = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    linkSpotify = models.URLField()
    duration = models.DurationField()
    lyrics = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
