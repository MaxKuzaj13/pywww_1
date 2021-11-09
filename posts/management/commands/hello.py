from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Say hello'

    def handle(self, *args, **options):
        name = None
        if args:
            name = " ".join(args)
        if name:
            self.stdout.write(f"Hallo {name}")
        else:
            self.stdout.write(f"Hallo World!")

    def add_arguments(self, parser):
        parser.add_argument('args', nargs='*', default='')