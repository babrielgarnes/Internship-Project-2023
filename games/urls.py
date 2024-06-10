from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('games/', views.games, name='games'),
    path('games/abc/', views.alphabetically, name='gamesabc'),
    path('games/short/', views.shortest, name='gamesshort'),
    path('games/long/', views.longest, name='gameslong'),
    path('games/least/', views.leastplayers, name='gamesleast'),
    path('games/most/', views.mostplayers, name='gamesmost'),
    path('games/owner/', views.owner, name='gamesowner'),
    path('games/details/<int:id>', views.details, name='details'),
    path('profile/', views.profile, name='profile'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('accounts/login', views.add_game, name='login'),
    path('add_game/', views.add_game, name='add_game'),
    path('about', views.about, name='about'),
    ]   