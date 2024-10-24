# Generated by Django 5.1.2 on 2024-10-17 18:19

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_job_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('town', models.CharField(max_length=100, verbose_name='Город')),
                ('stars', models.CharField(max_length=100, verbose_name='Звезды')),
                ('price', models.CharField(default='Не указано', max_length=80, verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание')),
                ('nights', models.CharField(max_length=255, verbose_name='Количество ночей')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата и время публикации')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.category', verbose_name='Выберите категорию')),
            ],
            options={
                'verbose_name': 'Тур поездка',
                'verbose_name_plural': 'Туры',
            },
        ),
        migrations.DeleteModel(
            name='Job',
        ),
    ]
