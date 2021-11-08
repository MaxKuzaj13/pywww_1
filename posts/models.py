from django.db import models
# from django.db.models import Model
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modifie = models.DateTimeField(auto_now=True)
