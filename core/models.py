"""
Created on 05-Jun-2022
@author: Abdulkadir
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email address")
        email = self.normalize_email(email)
        user = User(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Email'), max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.name if self.name else self.email

    @classmethod
    def check_user_exist(cls, email, password):
        user = cls.objects.filter(email=email)
        if user.exists() and user.first().check_password(password):
            return user.first()
        else:
            return None


class Book(models.Model):

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")

    isbn = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=255, blank=False, null=False)
    author = models.CharField(max_length=255)
    quantity = models.IntegerField()
    available = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return self.title