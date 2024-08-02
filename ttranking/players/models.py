# ttranking/players/models.py
from django.db import models


class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    ranking = models.IntegerField()
    photo = models.ImageField(upload_to='player_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
