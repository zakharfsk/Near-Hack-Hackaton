from django.urls import path, include
from .views import *

urlpatterns = [
    path('game/', show_menu_game, name = 'game')
]