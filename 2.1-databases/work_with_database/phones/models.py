from django.db import models
from django.utils.text import slugify


class Phone(models.Model):

    id = models.IntegerField(primary_key = True)
    name = models.CharField(verbose_name = 'Модель', max_length = 100)
    price = models.FloatField(verbose_name = 'Цена')
    image = models.URLField(verbose_name = 'Изображение', max_length = 150)
    release_date = models.DateField(verbose_name = 'Дата')
    lte_exists = models.BooleanField(verbose_name = 'Модуль LTE')
    slug = models.SlugField(verbose_name = 'Slugify URL', max_length = 100, unique = True)

    def __str__(self):
        return self.name

    # def slug_name(self):
    #     return slugify(self.name)
