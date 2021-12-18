from django.shortcuts import render
from .models import *
import random

from faker import Faker

fake = Faker()

# Create your views here.

def show_menu_game(request):
    nft = SelectNFT.objects.all()

    content = {
        'title': 'Tamagochi Game',
        'nfts': nft
    }
    return render(request, 'game.html', content)