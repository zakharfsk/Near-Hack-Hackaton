from django.contrib import admin
from .models import *

# Register your models here.
class NFTCardsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'nft_storage_url', 'price_card', 'is_published', 'selected')
    list_display_links = ('name',)
    search_fields = ('name', 'nft_storage_url', 'price_card', 'is_published', 'selected',)
    list_filter = ('name', 'is_published', 'selected',)
    list_editable = ('is_published', 'selected')

admin.site.register(SelectNFT, NFTCardsAdmin)