from django.db import models
from pytils.translit import slugify
from datetime import datetime
# Create your models here.

class Category(models.Model):
    name = models.CharField("Название категории", max_length=255)
    slug = models.SlugField(unique=True, editable=False, blank=True)
    image = models.CharField("URL-фото", max_length=1000)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, *kwargs)


class Tour(models.Model):
    title = models.CharField("Название", max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Выберите категорию")
    town = models.CharField("Город", max_length=100)
    stars = models.CharField("Звезды", max_length=100)
    image = models.CharField("URL-фото", max_length=500)
    price = models.CharField("Цена", max_length=80, default="Не указано")
    description = models.TextField("Описание")
    nights = models.CharField("Количество ночей", max_length=255)
    created_at = models.DateTimeField("Дата и время публикации", default=datetime.now)

    class Meta:
        verbose_name = 'Тур поездка'
        verbose_name_plural = 'Туры'

    def __str__(self):
        return self.title