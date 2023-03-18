
from django.core.management.commands.runserver import Command as RunserverCommand
from django.core.management import call_command


class Command(RunserverCommand):
    def __init__(self, Commands):
        super().__init__()
        self.Commands = Commands

    def handle(self, *args, **options):
        for command in self.Commands:
            call_command(str(command))
        super().handle(*args, **options)
