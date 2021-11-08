from django.db import models


class BookModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    available = models.BooleanField(default=False)
    publication_year = models.IntegerField()
    author = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modifie = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.title}"