
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework import permissions
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email address is required')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self.create_user(email, password, **extra_fields)


class BaseModel(models.Model):
    CreatedBy = models.PositiveIntegerField(
        _("Create by"),
        null=True,
        blank=True,
    )
    CreationTime = models.DateTimeField(
        _("Time of Creation"),
        auto_now_add=True,
    )
    UpdatedOn = models.DateTimeField(
        _("Updated on"),
        auto_now=True
    )
    AccountId = models.IntegerField(
        _('Account Id'),
        default=1
    )

    class Meta:
        abstract = True


class BaseUserModel(BaseModel, AbstractBaseUser):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    is_staff = models.BooleanField(
        _("Is staff"),
    )

    class Meta:
        abstract = True

