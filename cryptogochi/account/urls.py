import django
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', register, name = 'register'),
    path('social-auth/', include('social_django.urls', namespace = 'social')),
    # path('register/', register, name = 'register'),
    path('homepage/', general, name = 'homepage'),
    
]