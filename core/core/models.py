
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework import permissions
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


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


class BaseAuthUserModel(BaseModel, AbstractBaseUser):
    """
    Do not use it other than for managing User objects for a microservice.
    """
    is_staff = models.BooleanField(
        _("Is staff"),
    )

    class Meta:
        abstract = True


class UserBusinessModel(BaseModel):
    IAMUserId = models.BigIntegerField(
        _('IAM User Id'),
        unique=True,
    )

    class Meta:
        abstract = True
