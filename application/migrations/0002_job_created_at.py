# Generated by Django 5.1.2 on 2024-10-13 18:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата и время публикации'),
        ),
    ]
