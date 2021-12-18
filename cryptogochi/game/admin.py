from django.contrib import admin
from .models import *

# Register your models here.
class NFTCardsAdmin(admin.ModelAdmin):
    list_display = ('name', 'nft_storage_url', 'price_card', 'is_published')
    list_display_links = ('name',)
    search_fields = ('name', )
    list_filter = ('name', )
    list_editable = ('is_published',)

admin.site.register(SelectNFT, NFTCardsAdmin)