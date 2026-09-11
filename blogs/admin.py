from django.contrib import admin

from .models import Blog, CommentBlog

class CommentsInline(admin.TabularInline):
    model = CommentBlog
    fields = [
        'user',
        'body_comment',
    ]

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'name',
        'slug',
        'date_time_create',
    ]

    prepopulated_fields = {
        'slug': ['name',]
    }

    inlines = [
        CommentsInline,
    ]


@admin.register(CommentBlog)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'blog',
        'time_release_comment',
    ]
