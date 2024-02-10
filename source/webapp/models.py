from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


status_choices = [
    ('модерация', 'На модерацию'),
    ('опубликовано', 'Опубликовано'),
    ('отклонено', 'Отклонено'),
    ('удаление', 'На удаление'),
]


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name="Название")

    def __str__(self):
        return self.name


class Announcement(models.Model):
    img = models.ImageField(upload_to='static/img/', blank=True, null=True, verbose_name="Фотография")
    heading = models.CharField(max_length=50, blank=False, null=False, verbose_name="Заголовок ")
    description = models.TextField(blank=True, null=True, verbose_name="Описание ")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='announcement', verbose_name="Автор ")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория ")
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False, verbose_name="Цена ")
    status = models.CharField(max_length=50, null=False, blank=False, verbose_name="Статус", choices=status_choices, default='модерация')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Дата-время создания")
    date_publications = models.DateTimeField(null=True, blank=True, verbose_name="Дата-время публикации")
    date_update = models.DateTimeField(auto_now=True, verbose_name="Дата-время редактирования")

    def __str__(self):
        return self.heading

    def get_absolute_url(self):
        return reverse('webapp:announcement_detail', kwargs={'pk': self.pk})


@receiver(post_save, sender=Announcement)
def set_date_publications(sender, instance, **kwargs):
    if instance.status == 'Опубликовано' and not instance.date_publications:
        instance.date_publications = models.DateTimeField(auto_now_add=True)
        instance.save()


class Comment(models.Model):
    text = models.TextField(blank=False, null=False, verbose_name="Текст ")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='commet', verbose_name="Автор ")
    announcement_com = models.ForeignKey(Announcement, related_name='comments', on_delete=models.CASCADE, verbose_name="Объявление ")
    date_creation_com = models.DateTimeField(auto_now_add=True, verbose_name="Дата-время создания")

    def __str__(self):
        return self.text

