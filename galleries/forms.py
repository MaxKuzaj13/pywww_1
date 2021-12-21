from django import forms
from .models import Gallery, Photo


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('title', 'description', )


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('title', 'short_description', 'image', )

