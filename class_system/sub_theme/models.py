# -*- coding: utf-8 -*-
from django.db import models
from class_system.theme.models import Theme
# Create your models here.


class Sub_themeManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name_icontains=query) |
            models.Q(theme_icontains=query)
        )


class Sub_theme(models.Model):
    name = models.CharField('Nome', max_length=20)
    slug = models.SlugField('slug')
    theme = models.ForeignKey(Theme, on_delete=models.SET(0))

    objects = Sub_themeManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sub Tema'
        verbose_name_plural = 'Sub Temas'
        ordering = ['name']
