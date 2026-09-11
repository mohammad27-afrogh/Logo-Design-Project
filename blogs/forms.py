from django import forms

from .models import Blog, CommentBlog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'name',
            'slug',
            'cover_blog',
            'description',
            'date_time_create',
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentBlog
        fields = [
            'body_comment',
            ]
