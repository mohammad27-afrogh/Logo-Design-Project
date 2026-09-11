from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Blog
from .forms import CommentForm

def blog_page_view(request):
    blog = Blog.objects.all()
    
    NUMBER_PAGINATOR = 10
    paginator = Paginator(blog, NUMBER_PAGINATOR)
    page_number = request.GET.get('page', 1)

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'blogs/blog.html', context={
        'blogs': page_obj.object_list,
        'page_obj': page_obj,
        'paginator': paginator,
        'is_paginated': page_obj.has_other_pages(),
    })


def blog_detail_view(request, blog_slug):
    blog = Blog.objects.all()

    blog_detail = get_object_or_404(Blog, slug=blog_slug)
    blog_detail.view_count += 1
    blog_detail.save()

    blog_comments = blog_detail.comments.all()
    total_comment = len(blog_comments)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blog = blog_detail
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(request, 'blogs/blog_detail.html', {
        'blog': blog_detail,
        'comments': blog_comments,
        'total_comment': total_comment,
        'comment_form': comment_form,
    })