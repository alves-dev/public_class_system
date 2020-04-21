# -*- coding: utf-8 -*-
from .models import Sub_theme

from django.contrib import admin


# Register your models here.


class Sub_themeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'theme']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Sub_theme, Sub_themeAdmin)
