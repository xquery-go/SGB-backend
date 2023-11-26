from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import AuthenticationFailed
from core import choices
from core.models import BaseModel, BaseAuthUserModel
from tokens.base_tokens import BaseRefreshToken, BaseAccessToken
from users.manager import CustomUserManager


class User(BaseAuthUserModel):
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
    def authenticate(cls, username, password):
        try:
            USER = cls.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed('Incorrect Credentials.')
        if not USER.check_password(password):
            raise AuthenticationFailed(' Please check your password')

        refresh = BaseRefreshToken()

        data = {}
        user_token = refresh.for_user(USER)
        data['refresh_token'] = str(user_token)  # Query is run to create a new refresh token
        data['access_token'] = str(user_token.access_token)  # Query is run to create a new refresh token
        data['user'] = USER
        return data

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
        obj = BaseAccessToken(token)
        obj.verify()
        return obj.payload

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
