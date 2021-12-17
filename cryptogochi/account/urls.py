from django.urls import path, include
from .views import *

urlpatterns = [
    path('', user_login, name = 'user_login'),
    path('logout/', user_logout, name = 'logout'),
    path('social-auth/', include('social_django.urls', namespace = 'social')),
]