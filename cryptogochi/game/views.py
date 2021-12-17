from django.shortcuts import render

# Create your views here.

def show_menu_game(request):
    content = {
        'title': 'Tamagochi Game'
    }
    return render(request, 'game.html', content)