from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'name', 'email', 'cpf', 'cnpj_company', 'date_registration',
                    'date_last_access', 'status', 'is_staff']
    search_fields = ['name', 'email', 'cpf', 'cnpj_company']
    prepopulated_fields = {'name': ('username',)}


admin.site.register(User, UserAdmin)
