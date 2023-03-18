
from users.models import User
from django.core.management.commands.runserver import Command as RunserverCommand


class Command(RunserverCommand):
    help = 'Create a superuser if one does not already exist'

    def handle(self, *args, **options):
        username = 'admin.co'
        email = 'admin@admin.com'

        try:
            user = User.objects.get(username=username)
            self.stdout.write(self.style.SUCCESS('Superuser already exists.'))
        except User.DoesNotExist:
            user = User.objects.create_superuser(username=username, email=email, password='root')
            self.stdout.write(self.style.SUCCESS('Superuser created successfully.'))
