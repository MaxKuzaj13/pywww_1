from django.core.management.base import BaseCommand
from django.db import models
from datetime import datetime, timedelta
from faker import Faker
from health.models import Health
from main.models import UserProfile
from random import randint


class Command(BaseCommand):
    help = 'Adding fake observation using faker provide number to change from default 10 health observation like args'

    def add_arguments(self, parser):
        parser.add_argument(
            '-n', '--number',
            type=int, default=10,
            dest='number', help='Amount of fake observation to create'
        )

    def handle(self, *args, **options):
        n = options.get('number', 10)
        fake = Faker('pl_PL')
        post_temp = Health.objects.get(pk=1)
        for i in range(n):
            d = fake.date_time()
            d1 = d + timedelta(5)

            health = Health.objects.create(
                    user=post_temp.user,
                    systolic_blood_pressure=fake.pyint(1,200),
                    diastolic_blood_pressure=fake.pyint(1,200),
                    pulse=fake.pyint(1,200),
                    glucose=fake.pyint(1,200),
                    created=d,
                    modified= d1,
                    comment=fake.text(100),

              )
            print(health.pulse)

        self.stdout.write(f"")
        self.stdout.write(f"Added {n} fake status to Health")

