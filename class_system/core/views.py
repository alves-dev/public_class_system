# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

# Create your views here.


def home(request):
    context = {'company': settings.NAME_COMPANY}
    return render(request, 'home.html', context)


def about(request):
    context = {'company': settings.NAME_COMPANY}
    return render(request, 'about.html', context)


def contact(request):
    context = {'company': settings.NAME_COMPANY}
    return render(request, 'contact.html', context)
