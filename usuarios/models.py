from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, email, password, administrador, is_superuser, **extra_fields):
        now = timezone.now()
        email = self.normalize_email(email)
        if not email:
            raise ValueError('O email é obrigatório.')
        user = self.model(email=email, administrador=administrador, is_superuser=is_superuser, last_login=now, data_criacao=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)
    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(_('Nome'), max_length=50)
    sobrenome = models.CharField(_("Sobrenome"), max_length=254, blank=True, null=True)
    email = models.EmailField(_('Email'),max_length=254, unique=True)
    administrador = models.BooleanField(_('Administrador'), default=False)
    is_active = models.BooleanField(_('Ativo'), default=True)
    data_criacao = models.DateTimeField(_('Data de criação'), auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']
    objects = UserManager()

    @property
    def is_staff(self):
        return self.administrador

    class Meta:
        verbose_name = _('Usuário')
        verbose_name_plural = _('Usuários')

    def __str__(self):
        return f'Nome: {self.nome} Email: {self.email}'
