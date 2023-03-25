from users.models import Group
from django.core.management.commands.runserver import Command as RunserverCommand
from settings import GROUPS_ALLOWED
from core import choices


class Command(RunserverCommand):
    help = 'Create a group if one does not already exist'
    import ipdb
    ipdb.set_trace()
    GROUP_DATA = (
        choices.UserGroup.choices[GROUPS_ALLOWED[0] - 1][1],
        choices.UserGroup.choices[GROUPS_ALLOWED[1] - 1][1],
        choices.UserGroup.choices[GROUPS_ALLOWED[2] - 1][1],
    )

    def handle(self, *args, **options):
        for group in self.GROUP_DATA:
            group_name = group
            try:
                Group.objects.get(Name=group_name)
                self.stdout.write(self.style.WARNING(f'Group with name {group_name} already exists.'))
            except Group.DoesNotExist:
                Group.objects.create(Name=group_name, )
                self.stdout.write(self.style.SUCCESS(f'Group with name {group_name} created successfully.'))
