
from django.contrib import admin
from django.contrib.admin import register

from users import models


@register(models.User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'UserId',
        'ActiveStatus',
    )
    readonly_fields = ('password',
                       )
    # inlines = [UserGroupModelAdmin]


@register(models.Group)
class GroupModelAdmin(admin.ModelAdmin):
    list_display = (
        'GroupId',
        'Name',
        'ActiveStatus',
    )

    # inlines = [UserGroupModelAdmin]

