from django.urls import path, include
from .views import *

urlpatterns = [
    path('homepage/', general, name = 'homepage'),
]