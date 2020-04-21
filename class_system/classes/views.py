# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Classes, Assisted
from class_system.theme.models import Theme
from class_system.sub_theme.models import Sub_theme


@login_required
def list_classes(request):
    classes = Classes.objects.all()
    theme = Theme.objects.all()
    sub_theme = Sub_theme.objects.all()
    context = {'company': settings.NAME_COMPANY,
               'classes': classes,
               'theme': theme,
               'sub_theme': sub_theme}
    return render(request, 'list_classes.html', context)


@login_required
def assisted(request, slug):
    classe = get_object_or_404(Classes, slug=slug)
    assisted, created = Assisted.objects.get_or_create(user=request.user, classe=classe)

    context = {'company': settings.NAME_COMPANY,
               'classe': classe}
    return render(request, 'details.html', context)
