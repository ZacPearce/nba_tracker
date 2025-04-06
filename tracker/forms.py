from django import forms
from .models import Player, Team, GameLog


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'team']


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']


class GameLogForm(forms.ModelForm):
    class Meta:
        model = GameLog
        fields = ['date', 'team', 'opponent', 'team_score', 'opponent_score', 'top_performer']
