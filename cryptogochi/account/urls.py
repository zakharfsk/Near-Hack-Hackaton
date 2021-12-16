import django
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', user_login, name = 'login'),
    path('social-auth/', include('social_django.urls', namespace = 'social')),
    path('register/', register, name = 'register'),
    path('homepage/', general, name = 'homepage'),
    
]