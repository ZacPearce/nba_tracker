from django.db import models


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)


class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
