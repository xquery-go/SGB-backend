
from django.db import models
from core.base_items import BaseModel
from django.utils.translation import gettext_lazy as _
from core import choices
# Create your models here.


class User(BaseModel):
    UserId = models.BigAutoField(
        _('Id'),
        primary_key=True
    )
    AccountId = models.IntegerField(
        _('Account Id'),
    )
    UserName = models.CharField(
        _('Username'),
        unique=True,
        max_length=500,
    )
    UserEmail = models.EmailField(
        _('User Email'),
        max_length=200,
    )
    Password = models.CharField(
        _('Password'),
        max_length=500,
    )
    ActiveStatus = models.PositiveSmallIntegerField(
        _('Active Status'),
        choices=choices.UserActiveStatus.choices,
    )

