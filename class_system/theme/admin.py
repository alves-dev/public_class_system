# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Theme


# Register your models here.


class ThemeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Theme, ThemeAdmin)
