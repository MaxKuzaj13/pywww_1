
python manage.py shell_plus

from galleries.models import *
gallery = Gallery.objects.all()

Photo.objects.filter(gallery__title__contains="st")


