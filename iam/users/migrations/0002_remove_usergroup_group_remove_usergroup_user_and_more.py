# Generated by Django 4.1 on 2024-01-29 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usergroup',
            name='Group',
        ),
        migrations.RemoveField(
            model_name='usergroup',
            name='User',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='UserGroup',
        ),
    ]
