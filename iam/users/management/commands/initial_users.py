
from users.models import User
from django.core.management.commands.runserver import Command as RunserverCommand


class Command(RunserverCommand):
    help = 'Create a superuser if one does not already exist'
    USER_DATA = (
        ('admin.co', 'admin@admin.com', 'root'),
        ('naruto', 'naruto@cakes.com', 'root'),
    )

    def handle(self, *args, **options):
        for user in self.USER_DATA:
            username, email, password = user
            try:
                User.objects.get(username=username)
                self.stdout.write(self.style.SUCCESS('Superuser already exists.'))
            except User.DoesNotExist:
                User.objects.create_superuser(username=username, email=email, password=password)
                self.stdout.write(self.style.SUCCESS('Superuser created successfully.'))
