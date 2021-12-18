from django.shortcuts import render
from .models import *
import random

from faker import Faker

fake = Faker()

# Create your views here.

def show_menu_game(request):
    nft = SelectNFT.objects.all()
    one = SelectNFT.objects.all()[:1]

    content = {
        'title': 'Tamagochi Game',
        'nfts': nft,
        'once': one
    }
    return render(request, 'game.html', content)

def show_market(request):
    nfts = SelectNFT.objects.all()

    return render(request, 'market.html', {'nft': nfts})

def show_profile(request):
    nfts = SelectNFT.objects.all()

    return render(request, 'profile.html', {'nft': nfts})