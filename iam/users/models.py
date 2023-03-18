
from django.db import models
from core.models import BaseModel, BaseUserModel
from core.models import CustomUserManager
from django.utils.translation import gettext_lazy as _
from core import choices
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class User(BaseUserModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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
    )
    ActiveStatus = models.PositiveSmallIntegerField(
        _('Active Status'),
        choices=choices.UserActiveStatus.choices(),
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
        choices=choices.UserActiveStatus.choices(),
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


