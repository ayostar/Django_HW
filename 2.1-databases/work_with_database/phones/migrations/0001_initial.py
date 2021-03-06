# Generated by Django 4.0.3 on 2022-03-22 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Модель')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('image', models.URLField(max_length=150, verbose_name='Изображение')),
                ('release_date', models.DateField(verbose_name='Дата')),
                ('lte_exists', models.BooleanField(verbose_name='Модуль LTE')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Slugify URL')),
            ],
        ),
    ]
