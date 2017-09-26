from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):
        new_group, created = Group.objects.get_or_create(name='customer')
        self.stdout.write('created customer' if created else 'customer has been created')
        new_group, created = Group.objects.get_or_create(name='store')
        self.stdout.write('created store' if created else 'store has been created')
        new_group, created = Group.objects.get_or_create(name='mockup')
        self.stdout.write('created mockup' if created else 'mockup has been created')
