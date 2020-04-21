from django.urls import path
from class_system.classes.views import list_classes, assisted


app_name = 'classes'


urlpatterns = [
    path('list_classes/', list_classes, name='list_classes'),
    path('<slug:slug>', assisted, name='assisted'),
]
