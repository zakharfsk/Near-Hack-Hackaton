from django.db import models

# Create your models here.

class NewsList(models.Model):
    title = models.CharField(max_length = 255, verbose_name = 'Заголовок')
    description = models.TextField(verbose_name = 'Текст публікації')
    time_created = models.DateTimeField(auto_now_add = True, verbose_name = 'Час створення')
    photo_url = models.ImageField(upload_to = "photos/%Y/%m/%d/", verbose_name = 'Фото')
    is_published = models.BooleanField(default = False, verbose_name = 'Публікація')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новини'
        verbose_name_plural = 'Новини'