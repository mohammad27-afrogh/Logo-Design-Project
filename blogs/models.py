from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse

from ckeditor.fields import RichTextField

class Blog(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=False, allow_unicode=True)
    view_count = models.IntegerField(default=0)
    cover_blog = models.ImageField(upload_to='blog/', blank=True)
    description = RichTextField()
    date_time_create = models.DateTimeField(default=timezone.now)
    date_time_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Blog'

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('blog:blog_detail_by_slug', args=[self.slug])
    

class CommentBlog(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    time_release_comment = models.DateTimeField(default=timezone.now)
    body_comment = RichTextField()

    class Meta:
        verbose_name_plural = 'Comment Blog'

    def __str__(self):
        return f'{self.blog}'