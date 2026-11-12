from django.contrib import admin

from .models import Blog, CommentBlog

class CommentsInline(admin.TabularInline):
    model = CommentBlog
    fk_name = 'blog'
    extra = 1
    fields = [
        'user',
        'body_comment',
        'is_approved',
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
        'user',
        'blog',
        'body_comment',
        'is_approved',
        'time_release_comment',
        'parent',
    ]
    list_editable = [
        'is_approved',
    ]
