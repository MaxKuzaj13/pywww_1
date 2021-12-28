from django.contrib.admin.widgets import AdminFileWidget
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from slugify import slugify
import string
import random
from django.db import models
from sorl.thumbnail import get_thumbnail
from django.contrib import admin


def get_rand_text(n):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(n))


class Gallery(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    STATUS_TYPES_CHOICES = (('new', 'New'), ('hide', 'Hide'), ('published', 'Published'))
    status = models.CharField(max_length=20, choices=STATUS_TYPES_CHOICES, default='new')

    class Meta:
        verbose_name = "Galeria"
        verbose_name_plural = "Galerje"

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        if self._state.adding and not self.slug:
            slug = slugify(self.title)
            slugs = self.__class__.objects.values_list('slug', flat=True)
            if slugs:
                while True:
                    if slug in slugs:
                        slug += get_rand_text(5)
                    else:
                        break
                self.slug = slug
        if self.status == 'hide':
            self.photos.update(status='hide')
        return super().save(*args, *kwargs)

    # changed to
    @property
    def photo_count(self):
        return self.photos.count()


def upload_to(instance, filename):
    return f'galleries/{instance.gallery.slug}/{filename}'


class Photo(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=355, blank=True, null=True)
    short_description = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to=upload_to)
    gallery = models.ForeignKey('Gallery', on_delete=models.CASCADE, related_name='photos')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    STATUS_TYPES_CHOICES = (('new', 'New'), ('hide', 'Hide'), ('published', 'Published'))
    status = models.CharField(max_length=20, choices=STATUS_TYPES_CHOICES, default='new')

    class Meta:
        verbose_name = "Zdjęcie"
        verbose_name_plural = "Zdjęcia"

    def __str__(self):
        return f"{self.title}"


    def save(self, *args, **kwargs):
        if self._state.adding and not self.slug:
            slug = slugify(self.title)
            slugs = self.__class__.objects.values_list('slug', flat=True)
            if slugs:
                while True:
                    if slug in slugs:
                        slug += get_rand_text(5)
                    else:
                        break
                self.slug = slug
        return super().save(*args, *kwargs)

    @property
    def is_published(self):
        return self.status == 'published'



