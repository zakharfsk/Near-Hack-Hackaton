import random
import celery
from celery import Celery

from django.shortcuts import render
from faker import Faker


from .models import *
Faker.seed(0)

# Create your views here.

def news_list(request):
    
    if request.method == 'GET':
        faker = Faker('ru_RU')
        print(faker.text())

        
        news = NewsList.objects.all()
        
        # for i in range(10):
        #     NewsList(title = f'{faker.name()}', description = f'{faker.text()}', views = random.randint(78, 1325), is_published = True).save()
        
        return render(request, 'newsline/list.html', {'news': news, 'title': 'Головна сторінка'})
    elif request.method == 'POST':
        print('test')

def test_page(request):
    return render(request, 'newsline/test_page.html')