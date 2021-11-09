from django.core.management.base import BaseCommand
from django.db import models
from datetime import datetime, timedelta
from faker import Faker
from posts.models import Post
# from pywww.posts.models import Post


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

        d = fake.date_time()
        d1 = d + timedelta(5)
        for i in range(n):
            post = Post.objects.create(
                    title=fake.text(30),
                    content=fake.text(400),
                    published=fake.boolean(),
                    created=d,
                    modified= d1,
                    sponsored=fake.boolean(),
              )
            print(post.title)

        self.stdout.write(f"")
        self.stdout.write(f"Added {n} posts to Post")

