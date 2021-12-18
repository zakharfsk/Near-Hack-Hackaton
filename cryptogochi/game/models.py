from django.db import models

# Create your models here.

class SelectNFT(models.Model):
    name = models.CharField(max_length = 250)
    health = models.IntegerField(blank = True)
    satiety = models.IntegerField(blank = True)
    happiness = models.IntegerField(blank = True)
    #photo_url = models.ImageField(upload_to = "photos/NFT", verbose_name = 'Фото')
    nft_storage_url = models.CharField(blank = True, max_length = 500)
    price_card = models.IntegerField(blank = True)
    is_published = models.BooleanField(default = False)
    selected = models.BooleanField(default = False)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'NFS карточки'
        verbose_name_plural = 'NFS карточки'