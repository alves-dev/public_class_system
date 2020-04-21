# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Company

# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'cnpj', 'contact']
    search_fields = ['name', 'cnpj']


admin.site.register(Company, CompanyAdmin)
