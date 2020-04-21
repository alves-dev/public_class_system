from django.urls import path
from class_system.core.views import home, about, contact
import class_system

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
