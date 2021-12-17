import time

import celery
from celery import Celery
from datetime import timedelta
from django.http.response import HttpResponse
from django.shortcuts import render

from .models import *

# Create your views here.

app = Celery()

app.conf = {
    # Executes every day at  12:30 pm.
    'add-every-30-second': {
        'task': 'tasks.elast',
        'schedule': timedelta(seconds = 3),
        'args': (),
    },
}
@app.task()
def news_list(request):
    count = 0
    news = NewsList.objects.all()
    count += 1
    print(count)
    
    return render(request, 'newsline/list.html', {'news': news, 'title': 'Новини', 'count': count})

