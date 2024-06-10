from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from .forms import GameForm
from .models import Game
import random

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def games(request):
    mygames = Game.objects.all().values()
    template = loader.get_template('all_games.html')
    context = {
        'mygames': mygames,
        'view' : "Choose here"
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mygame = Game.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mygame': mygame
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def alphabetically(request):
    mygames = Game.objects.order_by('name')
    template = loader.get_template('all_games.html')
    context = {
        'mygames': mygames,
        'view' : "Alphabetically"
    }
    return HttpResponse(template.render(context, request))

def shortest(request):
    mygames = Game.objects.order_by('time')
    template = loader.get_template('all_games.html')
    context = {
        'mygames': mygames,
        'view' : "Shortest"
    }
    return HttpResponse(template.render(context, request))

def longest(request):
    mygames = Game.objects.order_by('-time').values()
    template = loader.get_template('all_games.html')
    context = {
        'mygames': mygames,
        'view' : "Longest"
    }
    return HttpResponse(template.render(context, request))

def owner(request):
    mygames = Game.objects.order_by('owner').values()
    template = loader.get_template('all_games.html')
    context = {
        'mygames': mygames,
        'view' : "Owner"
    }
    return HttpResponse(template.render(context, request))

def leastplayers(request):
    mygames = Game.objects.order_by('max_players').values()
    template = loader.get_template('all_games.html')
    context = {
        'mygames': mygames,
        'view' : "Least Players"
    }
    return HttpResponse(template.render(context, request))

def mostplayers(request):
    mygames = Game.objects.order_by('-max_players').values()
    template = loader.get_template('all_games.html')
    context = {
        'mygames': mygames,
        'view' : "Most Players"
    }
    return HttpResponse(template.render(context, request))

def profile(request):
    myinfo = User.get_user(request)
    print(myinfo)
    template = loader.get_template('profile.html')
    context = {
        'myinfo' : myinfo
    }
    return HttpResponse(template.render(context, request))

def add_game(request):
    form1 = GameForm(request.POST or None)
    games = Game.objects.all() 

    if request.method == 'POST':
        if form1.is_valid():
            game_instance = form1.save(commit=False)
            game_instance.save()
            
            return redirect('games') 

    return render(request, 'login.html', {'form': form1, 'games': games})