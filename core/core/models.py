
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        _("Created at"),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        _("Updated at"),
        auto_now=True
    )
    created_by = models.PositiveBigIntegerField(
        _("Create by"),
        null=True,
        blank=True,
    )
    updated_by = models.PositiveBigIntegerField(
        _("Updated by"),
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class BaseAuthUserModel(BaseModel, AbstractUser):
    """
    Do not use it other than for managing User objects for a microservice.
    """
    class Meta:
        abstract = True


class UserBusinessModel(BaseModel):
    user_id = models.PositiveBigIntegerField(
        _("User ID"),
        null=True,
        blank=True,
    )

    class Meta:
        asbstract = True
