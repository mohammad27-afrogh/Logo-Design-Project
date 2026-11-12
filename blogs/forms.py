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
        fields = ['body_comment']
        widgets = {
            'body_comment': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Write your comment...',
                'style': 'width: 100% !important; background-color: #1a1a1a !important; color: #ffffff !important; border: 2px solid #666666 !important; border-radius: 8px !important; padding: 15px !important; box-sizing: border-box !important;'
            }),
        }
