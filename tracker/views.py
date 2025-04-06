from django.shortcuts import render, redirect, get_object_or_404
from .models import Team, Player, GameLog, UserFavorite
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


def team_list(request):
    teams = Team.objects.all()
    return render(request, 'tracker/team_list.html', {'teams': teams})


def player_list(request):
    players = Player.objects.select_related('team').all()
    favorites = []
    if request.user.is_authenticated:
        favorites = UserFavorite.objects.filter(user=request.user).values_list('player_id', flat=True)
    return render(request, 'tracker/player_list.html', {'players': players, 'favorites': favorites})


@login_required
def watchlist(request):
    favorites = UserFavorite.objects.filter(user=request.user).select_related
    ('player__team')
    return render(request, 'tracker/watchlist.html', {'favorites': favorites})


def game_logs(request):
    logs = GameLog.objects.select_related('team').all()
    return render(request, 'tracker/game_logs.html', {'logs': logs})


@login_required
def add_to_watchlist(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    UserFavorite.objects.get_or_create(user=request.user, player=player)
    return redirect('player-list')

@login_required
@require_POST
def remove_from_watchlist(request, player_id):
    UserFavorite.objects.filter(user=request.user, player_id=player_id).delete()
    return redirect('watchlist')
