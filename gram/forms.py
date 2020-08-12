from django import forms
from django.contrib.auth.models import User
from .models import Post,Image,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'caption')

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude =['likes','profile']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['image', 'comment_owner']
