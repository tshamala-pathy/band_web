from django.db import models

class Band(models.Model):
    """
    Model representing a music band.

    Attributes:
    - name (str): The name of the band.
    - genre (str): The genre of the band's music.
    - description (str): A brief description of the band.
    """

    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    description = models.TextField(default='')

    def __str__(self):
        """
        Returns a string representation of the band.
        """
        return self.name


class Album(models.Model):
    """
    Model representing a music album.

    Attributes:
    - title (str): The title of the album.
    - release_date (Date): The release date of the album.
    - band (ForeignKey): A foreign key to the Band model, indicating the band that produced the album.
    """

    title = models.CharField(max_length=100)
    release_date = models.DateField()
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns a string representation of the album.
        """
        return self.title
