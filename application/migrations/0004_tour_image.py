# Generated by Django 5.1.2 on 2024-10-17 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_tour_delete_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='image',
            field=models.CharField(default=1, max_length=500, verbose_name='URL-фото'),
            preserve_default=False,
        ),
    ]
