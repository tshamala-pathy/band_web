from django.db import models

# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    description = models.TextField(default='')
    
    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
