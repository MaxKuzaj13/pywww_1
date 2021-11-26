from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # fields = ['title']