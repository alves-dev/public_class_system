# -*- coding: utf-8 -*-
from django.db import models
from class_system.sub_theme.models import Sub_theme
from django.conf import settings


class ClassesManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name_icontains=query) |
            models.Q(theme_icontains=query)
        )


class Classes(models.Model):
    title = models.CharField('Título', max_length=40)
    description = models.CharField('Descrição', max_length=150)
    creation_date = models.DateField('Data de criação', auto_now_add=True)
    slug = models.SlugField('slug')
    sub_theme = models.ForeignKey(Sub_theme, on_delete=models.SET(0))
    link = models.CharField('Link', max_length=150, default='')

    objects = ClassesManager

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'
        ordering = ['title']


class Assisted(models.Model):
    STATUS_CHOICES = (
        (0, 'Iniciada'), (1, 'Acabada')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='user', related_name='assisted', on_delete=models.CASCADE)
    classe = models.ForeignKey(Classes, verbose_name='classe', related_name='assisted', on_delete=models.CASCADE)
    status = models.IntegerField('status', choices=STATUS_CHOICES, default=0, blank=True)
    date_assisted = models.DateField('Data que assistiu', auto_now_add=True)

    class Meta:
        verbose_name = 'Assistida'
        verbose_name_plural = 'Assistidas'
        unique_together = (('user', 'classe'),)
