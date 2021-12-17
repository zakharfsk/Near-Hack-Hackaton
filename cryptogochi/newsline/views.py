import random
import celery
from celery import Celery

from django.shortcuts import render

from .models import *

# Create your views here.

def news_list(request):
    
    if request.method == 'GET':
        news = NewsList.objects.all()[:3]
    
        return render(request, 'newsline/list.html', {'news': news, 'title': 'Головна сторінка'})
    elif request.method == 'POST':
        print('test')

def test_page(request):
    return render(request, 'newsline/test_page.html')