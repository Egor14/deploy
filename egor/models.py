from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=50)
    leg = models.CharField(max_length=20)
    club = models.CharField(max_length=50)

    def __str__(self):
        return self.name