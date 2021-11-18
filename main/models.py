from django.db import models

# from django.db.models import Model
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE) # on_delete=models.CASCADE
    bio = models.TextField()