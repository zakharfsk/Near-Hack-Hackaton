from django.urls import path, include
from .views import *

urlpatterns = [
    path('game/', show_menu_game, name = 'game'),
    path('market/', show_market, name = 'market'),
    path('profile/', show_profile, name = 'profile'),
]