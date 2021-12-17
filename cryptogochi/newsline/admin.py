from django.contrib import admin
from .models import *

# Register your models here.

class NewsListsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_created', 'photo_url', 'views', 'is_published')
    list_display_links = ('title',)
    search_fields = ('title', 'time_created', 'is_published',)
    list_filter = ('title', 'time_created', 'is_published')
    list_editable = ('is_published',)

admin.site.register(NewsList, NewsListsAdmin)