from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import MyUserManager
from django.utils import timezone


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, default='', unique=True)
    name  = models.CharField(max_length=255, blank=True, default='')

    is_active = models.BooleanField(default=True)
    is_admin =models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateField(default=timezone.now)
    last_login =models.DateField(blank=True, null=True)


    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    # EMAIL_FIELD ='email'
    REQUIRED_FIELDS = []

    #class Meta:
    #    verbose_name ='User'
    #   verbose_name_plural ='Users'


    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name or self.email.split('@')[0]
    