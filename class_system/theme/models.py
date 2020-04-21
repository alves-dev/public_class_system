# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class ThemeManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name_icontains=query)
        )


class Theme(models.Model):
    name = models.CharField('Nome', max_length=20)
    slug = models.SlugField('slug')

    objects = ThemeManager

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tema'
        verbose_name_plural = 'Temas'
        ordering = ['name']
