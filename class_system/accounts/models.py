from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
import re
from django.core import validators


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Usuário', max_length=30, unique=True,
                                validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
                                                                      'O nome de usuário só pode conter letras, digitos ou os '
                                                                      'seguintes caracteres: @/./+/-/_', 'invalid')]
                                )
    name = models.CharField('Nome', max_length=50, blank=True)
    email = models.EmailField('E-mail', unique=True)
    cpf = models.CharField('CPF', unique=True, max_length=12)
    cnpj_company = models.CharField('CNPJ da Empresa', max_length=14, blank=False)
    date_registration = models.DateField('Data de registro', auto_now_add=True)
    date_last_access = models.DateTimeField('Último acesso', blank=True, null=True)
    status = models.CharField('Status', default='Aguardando', max_length=30)

    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
