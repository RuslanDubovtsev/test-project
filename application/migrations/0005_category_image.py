# Generated by Django 5.1.2 on 2024-10-18 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_tour_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.CharField(default=1, max_length=500, verbose_name='URL-фото'),
            preserve_default=False,
        ),
    ]
