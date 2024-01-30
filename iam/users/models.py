from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from core import choices
from core.models import BaseAuthUserModel


class User(BaseAuthUserModel):
    email = models.EmailField(
        _('Email Address'),
        max_length=255,

    )
    username = models.CharField(
        _('Username'),
        unique=True,
        max_length=500,
        validators=[RegexValidator(regex=r'^[^@]*$',
                                   message="Sorry, but use of '@' symbol is not allowed",
                                   )]
    )  # r'^.*@.*$' to put a condition that '@' MUST be present in the string
    active_status = models.PositiveSmallIntegerField(
        _('Active Status'),
        choices=choices.UserActiveStatus.choices,
        default=choices.UserActiveStatus.INACTIVE,
    )
    mobile_number = models.CharField(
        _('Mobile Number'),
        null=True,
        blank=True,
        max_length=12,
    )
    country = models.PositiveIntegerField(
        _('Country'),
        null=True,
        blank=True,
        validators=[MinValueValidator(limit_value=1),
                    MaxValueValidator(limit_value=400)]
    )

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'User'

    def __str__(self):
        return f'{self.username}'
