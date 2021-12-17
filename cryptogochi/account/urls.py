from django.urls import path, include
from .views import *

urlpatterns = [
    path('', user_login, name = 'user_login'),
    path('social-auth/', include('social_django.urls', namespace = 'social')),
]