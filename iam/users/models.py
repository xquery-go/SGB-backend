import datetime
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
import jwt
from django.db import models
from django.utils import timezone
from rest_framework.exceptions import AuthenticationFailed
from core.base.exceptions import TokenExpired
from core.models import BaseModel, BaseUserModel
from users.manager import CustomUserManager
from django.utils.translation import gettext_lazy as _
from core import choices
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

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

    @classmethod
    def authenticate(cls, *args, **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')
        USER = cls.objects.get(username=username)
        if USER is None:
            raise AuthenticationFailed('Username not found')
        if not USER.check_password(password):
            raise AuthenticationFailed('Incorrect Credentials Please check your password')

        payload = {
            'pk': USER.pk,
            'exp': timezone.now() + datetime.timedelta(settings.TOKEN_EXPIRATION_TIMEOUT),
            'iat': timezone.now()
        }

        web_token = jwt.PyJWT()
        token = web_token.encode(payload=payload, key='secret', algorithm='HS256')
        return

    def is_token_valid(self, token):
        """
        Checks if a given token is valid for the user.
        """
        try:
            token_obj = UserToken.objects.get(key=token)
            if token_obj:
                if token_obj.ExpiresAt >= timezone.now():
                    TokenAuthentication().authenticate_credentials(token)
                elif token_obj.ExpiresAt < timezone.now():
                    raise TokenExpired
        except (UserToken.DoesNotExist, AuthenticationFailed, TokenExpired):
            return False
        return token_obj.user == self

    def get_or_create_token(self):
        """
        Use Wisely
        """
        try:
            token = UserToken.objects.get(user=self)
        except UserToken.DoesNotExist:
            token = UserToken.objects.create(
                user=self,
                ExpiresAt=timezone.now() + datetime.timedelta(seconds=settings.TOKEN_EXPIRATION_TIMEOUT)
            )
        return token

    def refresh_user_token(self):
        """
        Use Wisely
        """
        try:
            token = UserToken.objects.get(user=self)
        except UserToken.DoesNotExist:
            token = UserToken.objects.create(
                user=self,
                ExpiresAt=timezone.now() + datetime.timedelta(seconds=settings.TOKEN_EXPIRATION_TIMEOUT)
            )
        return token.save()

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


class UserToken(Token):
    ExpiresAt = models.DateTimeField(
        _('Expires at'),
    )

    @staticmethod
    @receiver(pre_save, sender='users.UserToken')
    def add_expiration_time(sender, instance, **kwargs):
        if instance.pk:
            old_instance = sender.objects.get(pk=instance.pk)
            if old_instance.key != instance.key:
                instance.ExpiresAt = timezone.now() + datetime.timedelta(seconds=settings.TOKEN_EXPIRATION_TIMEOUT)

