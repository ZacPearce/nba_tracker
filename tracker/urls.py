from django.urls import path
from . import views


urlpatterns = [
        path('teams/', views.team_list, name='team-list'),
        path('teams/add/', views.create_team, name='add-team'),
        path('teams/delete/<int:team_id>/', views.delete_team, name='delete-team'),
        path('players/', views.player_list, name='player-list'),
        path('players/add/', views.create_player, name='add-player'),
        path('players/delete/<int:player_id>/', views.delete_player, name='delete-player'),
        path('watchlist/', views.watchlist, name='watchlist'),
        path('add-to-watchlist/<int:player_id>/', views.add_to_watchlist, name='add-to-watchlist'),
        path('remove-from-watchlist/<int:player_id>/', views.remove_from_watchlist, name='remove-from-watchlist'),
        path('game-logs/', views.game_logs, name='game-logs'),
        path('game-logs/add/', views.create_game_log, name='add-game-log'),
        path('game-logs/delete/<int:log_id>/', views.delete_game_log, name='delete-game-log'),


]
