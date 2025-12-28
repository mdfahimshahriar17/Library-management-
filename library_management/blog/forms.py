from .models import Post
from django import forms

class BlogFrom (forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']