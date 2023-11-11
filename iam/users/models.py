import datetime

import jwt
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from jwt.exceptions import JWTDecodeError
from rest_framework.exceptions import AuthenticationFailed

from core import choices
from core.models import BaseModel, BaseUserModel
from users.manager import CustomUserManager


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

    @classmethod
    def authenticate(cls, *args, **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')
        USER = cls.objects.get(username=username)

        if USER is None:
            raise AuthenticationFailed('Username not found')
        if not USER.check_password(password):
            raise AuthenticationFailed('Incorrect Credentials Please check your password')

        token = cls.generate_token(USER)
        return token

    @classmethod
    def generate_token(cls, user):
        creation_time = datetime.datetime.now(timezone.utc)
        expiry_time = creation_time + datetime.timedelta(seconds=settings.TOKEN_EXPIRATION_TIMEOUT)
        payload = {
            'pk': user.pk,
            'exp': int(expiry_time.timestamp()),
            'iat': int(creation_time.timestamp()),
        }

        jwt_instance = jwt.JWT()
        key = jwt.jwk.OctetJWK(key=settings.HS256_TOKEN_KEY)
        token = jwt_instance.encode(payload=payload, key=key, alg='HS256')
        return token

    @classmethod
    def is_token_valid(cls, token):
        """
        Checks if a given token is valid for the user.
        """
        try:
            result = cls.get_token_details(token)
        except Exception:
            result = None
        if result:
            return True
        return False

    @classmethod
    def get_token_details(cls, token):
        """
        Use Wisely
        """
        octet_key_instance = jwt.jwk.OctetJWK(key=settings.HS256_TOKEN_KEY)
        sliced_token = token.split('.')
        if len(sliced_token) != 3:
            raise AuthenticationFailed('Invalid token')
        try:
            result = jwt.JWT().decode(token, key=octet_key_instance, algorithms=['HS256'])
        except JWTDecodeError:
            raise AuthenticationFailed('Given token either invalid or expired')
        return result

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
