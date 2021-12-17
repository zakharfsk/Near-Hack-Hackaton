from django.urls import path, include
from .views import *

urlpatterns = [
    path('homepage/', news_list, name = 'homepage'),
]