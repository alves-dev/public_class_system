from django.urls import path
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import views
from class_system.accounts.views import register
from class_system.accounts.views import dashboard

app_name = 'accounts'

company_context = {'company': settings.NAME_COMPANY}
context_login = {
    'extra_context': company_context,
    'authentication_form': AuthenticationForm,
    'template_name': 'login.html',
}
context_logout = {
    'extra_context': company_context,
    'next_page': 'core:home',
}

urlpatterns = [
    path('login/', views.LoginView.as_view(**context_login), name='login'),
    path('logout/', views.LogoutView.as_view(**context_logout), name='logout'),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
]
