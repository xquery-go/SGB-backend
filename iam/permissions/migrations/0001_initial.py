# Generated by Django 4.1 on 2023-11-26 15:46

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('CreatedBy', models.PositiveIntegerField(blank=True, null=True, verbose_name='Create by')),
                ('CreationTime', models.DateTimeField(auto_now_add=True, verbose_name='Time of Creation')),
                ('UpdatedOn', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('AccountId', models.IntegerField(default=1, verbose_name='Account Id')),
                ('ModuleId', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('Title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Module',
                'verbose_name_plural': 'Modules',
                'db_table': 'Module',
            },
        ),
        migrations.CreateModel(
            name='ModulePermission',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='auth.group')),
                ('CreatedBy', models.PositiveIntegerField(blank=True, null=True, verbose_name='Create by')),
                ('CreationTime', models.DateTimeField(auto_now_add=True, verbose_name='Time of Creation')),
                ('UpdatedOn', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('AccountId', models.IntegerField(default=1, verbose_name='Account Id')),
                ('ModulePermissionId', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('Title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title')),
                ('Module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ModulePermissions', to='permissions.module')),
            ],
            options={
                'verbose_name': 'Module Permission',
                'verbose_name_plural': 'Modules Permissions',
                'db_table': 'ModulePermission',
            },
            bases=('auth.group', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('CreatedBy', models.PositiveIntegerField(blank=True, null=True, verbose_name='Create by')),
                ('CreationTime', models.DateTimeField(auto_now_add=True, verbose_name='Time of Creation')),
                ('UpdatedOn', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('AccountId', models.IntegerField(default=1, verbose_name='Account Id')),
                ('PermissionId', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('Title', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Permission',
                'verbose_name_plural': 'Permissions',
                'db_table': 'Permission',
            },
        ),
        migrations.CreateModel(
            name='UserModulePermission',
            fields=[
                ('CreatedBy', models.PositiveIntegerField(blank=True, null=True, verbose_name='Create by')),
                ('CreationTime', models.DateTimeField(auto_now_add=True, verbose_name='Time of Creation')),
                ('UpdatedOn', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('AccountId', models.IntegerField(default=1, verbose_name='Account Id')),
                ('UserModulePermissionId', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('ModulePermission', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='UserAuthModulesPermissions', to='permissions.modulepermission')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UsersAuthModulePermission', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User auth module permission',
                'verbose_name_plural': 'User auth module permissions',
                'db_table': 'UserAuthModulePermission',
            },
        ),
        migrations.AddField(
            model_name='modulepermission',
            name='Permission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ModulesPermission', to='permissions.permission'),
        ),
    ]
