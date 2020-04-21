# -*- coding: utf-8 -*-
from .models import Classes
from django.contrib import admin

# Register your models here.


class ClasseAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'creation_date', 'slug', 'sub_theme']
    search_fields = ['title', 'description', 'slug', 'sub_theme']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Classes, ClasseAdmin)
