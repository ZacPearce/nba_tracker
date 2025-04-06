from django.shortcuts import redirect, render
from .models import Team, Player, UserFavorite, GameLog
# Create your views here.


def team_list(request):
    teams = Team.objects.all()
    return render(request, 'tracker/team_list.html', {'teams': teams})


def player_list(request):
    players = Player.objects.select_related('team').all()
    return render(request, 'tracker/player_list.html', {'players': players})


def watchlist(request):
    if not request.user.is_authenticated:
        return redirect('login')
    favorites = UserFavorite.objects.filter(user=request.user).select_related
    ('player')
    return render(request, 'tracker/watchlist.html', {'favorites': favorites})


def game_logs(request):
    logs = GameLog.objects.select_realted('team').all()
    return render(request, 'tracker/game_logs.html', {'logs': logs})
