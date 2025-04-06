from django.urls import path
from . import views


urlpatterns = [
        path('teams/', views.team_list, name='team-list'),
        path('players/', views.player_list, name='player-list'),
        path('watchlist/', views.watchlist, name='watchlist'),
        path('game-logs/', views.game_logs, name='game-logs'),

]
