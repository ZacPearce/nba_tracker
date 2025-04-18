from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class GameLog(models.Model):
    date = models.DateField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    opponent = models.CharField(max_length=100)
    team_score = models.IntegerField()
    opponent_score = models.IntegerField()
    top_performer = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.team.name} vs {self.opponent} on {self.date}"


class UserFavorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'player')

    def __str__(self):
        return f"{self.user.username} - {self.player.name}"
