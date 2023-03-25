from django.db import models
from django.contrib.auth.models import Permission
from core.models import BaseModel, BaseUserModel
from users.manager import CustomUserManager
from django.utils.translation import gettext_lazy as _
from core import choices
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import Group as ProjectGroup

from django.conf import settings


# Create your models here.


class User(BaseUserModel):
    UserId = models.BigAutoField(
        _('Id'),
        primary_key=True
    )
    email = models.EmailField(
        _('Email Address'),
        max_length=255
    )
    username = models.CharField(
        _('Username'),
        unique=True,
        max_length=500,
        validators=[RegexValidator(regex=r'^[^@]*$',
                                   message="Sorry, but use of '@' symbol is not allowed",
                                   )]
    )  # r'^.*@.*$' to put a condition that '@' MUST be present in the string
    ActiveStatus = models.PositiveSmallIntegerField(
        _('Active Status'),
        choices=choices.UserActiveStatus.choices,
        default=choices.UserActiveStatus.INACTIVE,
    )
    MobileNumber = models.CharField(
        _('Mobile Number'),
        null=True,
        blank=True,
        max_length=12,
    )
    Country = models.PositiveIntegerField(
        _('Country'),
        null=True,
        blank=True,
        validators=[MinValueValidator(limit_value=1),
                    MaxValueValidator(limit_value=400)]
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'User'

    def __str__(self):
        return f'{self.username}'


class Group(BaseModel):
    GroupId = models.BigAutoField(
        _('Id'),
        primary_key=True
    )
    Name = models.CharField(
        _('Name'),
        max_length=255,
        null=True,
        blank=True
    )
    ActiveStatus = models.PositiveSmallIntegerField(
        _('Active Status'),
        choices=choices.UserActiveStatus.choices,
        default=choices.UserActiveStatus.ACTIVE,
    )

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'
        db_table = 'Group'

    def __str__(self):
        return f'{self.Name}'


class UserGroup(BaseModel):
    UserGroupId = models.BigAutoField(
        _('Id'),
        primary_key=True
    )
    User = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='UserGroups'
    )
    Group = models.ForeignKey(
        'Group',
        on_delete=models.CASCADE,
        related_name='UsersGroup'
    )

    class Meta:
        verbose_name = 'UserGroup'
        verbose_name_plural = 'UsersGroups'
        db_table = 'UserGroup'

