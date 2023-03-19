
from core.models import BaseModel
from django.contrib.auth.models import Group
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
# Create your models here.


class Module(BaseModel):
    ModuleId = models.BigAutoField(
        _('Id'),
        primary_key=True
    )
    Title = models.CharField(
        _('Title'),
        max_length=255,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.Title}'

    class Meta:
        verbose_name = _('Module')
        verbose_name_plural = _('Modules')
        db_table = 'Module'


class Permission(BaseModel):
    PermissionId = models.BigAutoField(
        _('Id'),
        primary_key=True
    )
    Title = models.CharField(
        _('Title'),
        max_length=255,
        null=True,
        blank=True,
        default=''
    )

    def __str__(self):
        return f'{self.Title}'

    class Meta:
        verbose_name = _('Permission')
        verbose_name_plural = _('Permissions')
        db_table = _('Permission')


# class ModulePermission(BaseModel):
#     ModulePermissionId = models.BigAutoField(
#         _('Id'),
#         primary_key=True
#     )
#     Title = models.CharField(
#         _('Title'),
#         max_length=255,
#         null=True,
#         blank=True
#     )
#     User = models.ForeignKey(
#         'users.User',
#         on_delete=models.CASCADE,
#         related_name='UserModulesPermissions'
#     )
#     Module = models.ForeignKey(
#         'Module',
#         on_delete=models.CASCADE,
#         related_name='ModulePermissions'
#     )
#     Permission = models.ForeignKey(
#         'Permission',
#         on_delete=models.CASCADE,
#         related_name='ModulesPermission'
#     )
#
#     def __str__(self):
#         return f'{self.Title}'
#
#     class Meta:
#         verbose_name = _('User Module Permission')
#         verbose_name_plural = _('User Modules Permissions')
#         db_table = 'UserModulePermission'


class UserModulePermissions(BaseModel):
    User = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='module_permissions'
    )
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('user module groups'),
        blank=True,
        help_text=_('The groups this user belongs to.'),
        related_name='user_module_permissions'
    )

    class Meta:
        verbose_name = _('User module permissions')
        verbose_name_plural = _('User module permissions')
        db_table = 'UserModulePermission'
