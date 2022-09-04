from django.db import models
from django.urls import reverse


class Movies(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    # slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    tag_line = models.TextField(blank=True,verbose_name="Слоган")
    content = models.TextField(blank=True, verbose_name="Сюжет")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    # cat = models.ManyToManyField('Category', verbose_name="Категория")
    # cast = models.ManyToManyField('Actors', verbose_name="Актеры")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = "Фильмы"
        verbose_name_plural = "Фильмы"
        ordering = ['id']

class Category(models.Model):
    title_cat = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name="Категории"
        verbose_name_plural="Категории"
        ordering = ['id']


class Actors(models.Model):
    title = models.CharField(max_length=255, verbose_name="Имя")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото актера")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время обновления")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('actors', kwargs={'actors_slug': self.slug})

    class Meta:
        verbose_name = "Актеры и режиссеры"
        verbose_name_plural = "Актеры и режиссеры"
        ordering = ['id']









