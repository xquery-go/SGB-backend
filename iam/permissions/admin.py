from django.contrib import admin
from permissions import models
from django.contrib.admin import register
# Register your models here.

@register(models.Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = (
        'ModuleId',
        'Title'
    )


@register(models.Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = (
        'PermissionId',
        'Title'
    )


# @register(models.UserModulePermissions)
# class UserModulePermissionsAdmin(admin.ModelAdmin):
#     list_display = (
#         'User',
#     )

