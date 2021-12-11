from django import forms

from .models import Post, Comment
from products.widgets import CustomClearableFileInput


class PostForm(forms.ModelForm):
    # Post Form
    class Meta:
        model = Post
        fields = ['title', 'intro', 'image', 'body']

    image = forms.ImageField(
        label="Image",
        required=False,
        widget=CustomClearableFileInput,
        )


class CommentForm(forms.ModelForm):
    # Comment Form
    class Meta:
        model = Comment
        fields = ['body']
