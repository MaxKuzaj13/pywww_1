from django.db import models

from django.utils.timezone import now, timedelta

# from django.db.models import Model
from django.contrib.auth.models import User


class CheckAgaMixin:
    def is_older_then_n_days(self, n =1):
        delta = timedelta(days=n)
        return now() - self.crated > delta


class Timestapmped(models.Model, CheckAgaMixin):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    sponsored = models.BooleanField(default=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tags = models.ManyToManyField('tags.Tag', related_name="post")

    def __str__(self):
        return f"{self.id} {self.title}"


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    tags = models.ManyToManyField('Post', related_name="post")

    def __str__(self):
        return f"{self.name} {self.description}"
