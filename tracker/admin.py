from django.contrib import admin
from .models import Team, Player, GameLog, UserFavorite

# Register your models here.

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(GameLog)
admin.site.register(UserFavorite)
