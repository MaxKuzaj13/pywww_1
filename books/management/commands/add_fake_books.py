from django.core.management.base import BaseCommand
from django.db import models
from datetime import datetime, timedelta
from faker import Faker
from books.models import BookModel
import random


class Command(BaseCommand):
    help = 'Adding fake posts using faker provide number to change from default 10 posts like args'

    def add_arguments(self, parser):
        parser.add_argument(
            '-n', '--number',
            type=int, default=10,
            dest='number', help='Amount of post to create'
        )

    def handle(self, *args, **options):
        n = options.get('number', 10)
        fake = Faker('pl_PL')

        for i in range(n):
            d = fake.date_time_this_decade()
            d1 = d + timedelta(random.randint(1, 100))

            book = BookModel.objects.create(
                title=fake.text(random.randint(10, 50)),
                description=fake.text(random.randint(100, 255)),
                available=fake.boolean(),
                publication_year=fake.random_int(1500, 2021),
                author=fake.name(),
                created=d,
                modified=d1,
              )
            print(book.title)

        self.stdout.write(f"")
        self.stdout.write(f"Added {n} posts to Post")

