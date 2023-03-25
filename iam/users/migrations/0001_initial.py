# Generated by Django 4.0.6 on 2023-03-25 07:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('CreatedBy', models.PositiveIntegerField(blank=True, null=True, verbose_name='Create by')),
                ('CreationTime', models.DateTimeField(auto_now_add=True, verbose_name='Time of Creation')),
                ('UpdatedOn', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('AccountId', models.IntegerField(default=1, verbose_name='Account Id')),
                ('GroupId', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('Name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('ActiveStatus', models.PositiveSmallIntegerField(choices=[(1, 'Active'), (2, 'Deactivated'), (3, 'Blocked'), (4, 'Inactive')], default=1, verbose_name='Active Status')),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
                'db_table': 'Group',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('CreatedBy', models.PositiveIntegerField(blank=True, null=True, verbose_name='Create by')),
                ('CreationTime', models.DateTimeField(auto_now_add=True, verbose_name='Time of Creation')),
                ('UpdatedOn', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('AccountId', models.IntegerField(default=1, verbose_name='Account Id')),
                ('is_staff', models.BooleanField(verbose_name='Is staff')),
                ('UserId', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('email', models.EmailField(max_length=255, verbose_name='Email Address')),
                ('username', models.CharField(max_length=500, unique=True, validators=[django.core.validators.RegexValidator(message="Sorry, but use of '@' symbol is not allowed", regex='^[^@]*$')], verbose_name='Username')),
                ('ActiveStatus', models.PositiveSmallIntegerField(choices=[(1, 'Active'), (2, 'Deactivated'), (3, 'Blocked'), (4, 'Inactive')], default=4, verbose_name='Active Status')),
                ('MobileNumber', models.CharField(blank=True, max_length=12, null=True, verbose_name='Mobile Number')),
                ('Country', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(limit_value=1), django.core.validators.MaxValueValidator(limit_value=400)], verbose_name='Country')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('CreatedBy', models.PositiveIntegerField(blank=True, null=True, verbose_name='Create by')),
                ('CreationTime', models.DateTimeField(auto_now_add=True, verbose_name='Time of Creation')),
                ('UpdatedOn', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('AccountId', models.IntegerField(default=1, verbose_name='Account Id')),
                ('UserGroupId', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('Group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UsersGroup', to='users.group')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserGroups', to='users.user')),
            ],
            options={
                'verbose_name': 'UserGroup',
                'verbose_name_plural': 'UsersGroups',
                'db_table': 'UserGroup',
            },
        ),
    ]
