from django.shortcuts import render, redirect, get_object_or_404
from .models import Team, Player, GameLog, UserFavorite
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import PlayerForm, TeamForm, GameLogForm
from django.shortcuts import get_object_or_404


def team_list(request):
    teams = Team.objects.all()
    return render(request, 'tracker/team_list.html', {'teams': teams})

# Teams
@login_required
def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team-list')
    else:
        form = TeamForm()
    return render(request, 'tracker/form.html', {'form': form, 'title': 'Add Team'})

@login_required
def delete_team(request, team_id):
    Team.objects.filter(id=team_id).delete()
    return redirect('team-list')


def player_list(request):
    players = Player.objects.select_related('team').all()
    favorites = []
    if request.user.is_authenticated:
        favorites = UserFavorite.objects.filter(user=request.user).values_list('player_id', flat=True)
    return render(request, 'tracker/player_list.html', {
        'players': players,
        'favorites': favorites
    })

# Players
@login_required
def create_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('player-list')
    else:
        form = PlayerForm()
    return render(request, 'tracker/form.html', {'form': form, 'title': 'Add Player'})


@login_required
def delete_player(request, player_id):
    Player.objects.filter(id=player_id).delete()


@login_required
def watchlist(request):
    favorites = UserFavorite.objects.filter(user=request.user).select_related
    ('player__team')
    return render(request, 'tracker/watchlist.html', {'favorites': favorites})


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


def game_logs(request):
    logs = GameLog.objects.select_related('team').all()
    return render(request, 'tracker/game_logs.html', {'logs': logs})

# Game Logs
@login_required
def create_game_log(request):
    if request.method == 'POST':
        form = GameLogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('game-logs')
    else:
        form = GameLogForm()
    return render(request, 'tracker/form.html', {'form': form, 'title': 'Add Game Log'})

@login_required
def delete_game_log(request, log_id):
    GameLog.objects.filter(id=log_id).delete()
    return redirect('game-logs')
