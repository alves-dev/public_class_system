# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class CompanyManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name_icontains=query)
        )


class Company(models.Model):
    name = models.CharField('Nome', max_length=70)
    cnpj = models.CharField('CNPJ', max_length=14)
    contact = models.CharField('Contato', max_length=30)

    objects = CompanyManager

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['name']
