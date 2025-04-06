from django.shortcuts import render
from .models import Team
# Create your views here.

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'tracker/team_list.html', {'teams': teams})