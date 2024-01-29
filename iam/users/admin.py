
from django.contrib import admin
from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from users import models


@register(models.User)
class UserAdmin(AuthUserAdmin):
    list_display = (
        'username',
        'email',
        'pk',
    )
